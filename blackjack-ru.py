import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __repr__(self):
        return f"{self.value} ({self.suit})"
    
class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in ["Пики", "Крести", "Червы", "Бубны"]
        for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]
        
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)
            
    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)
        
class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0
        
    def add_card(self, card):
        self.cards.append(card)
        
    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "A":
                    has_ace = True
                    self.value += 11
                else:
                    self.value +=10
            if has_ace and self.value > 21:
                self.value -= 10
                
    def get_value (self):
        self.calculate_value()
        return self.value
    
    def display(self):
        if self.dealer:
            print("[Скрытая карта]")
            print(self.cards[1])
        else:
            for card in self.cards:
                print(card)
            print("Сумма очков: ", self.get_value())
            
class Game:
    def __init__(self):
        pass
    
    def play(self):
        playing = True
        
        while playing:
            self.deck = Deck()
            self.deck.shuffle()
            
            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)
            
            for i in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())
                
            print("Ваши карты:")
            self.player_hand.display()
            print()
            print("Карты дилера:")
            self.dealer_hand.display()
            
            game_over = False
            
            while not game_over:
                player_has_blackjack = self.check_for_blackjack()
                dealer_has_blackjack = self.check_for_blackjack()
                if player_has_blackjack or dealer_has_blackjack:
                    game_over = True
                    self.show_blackjack_results(player_has_blackjack, dealer_has_blackjack)
                    continue
            
                choice = input("Пожалуйста, выберите [Взять / Остановиться] ").lower()
                while choice not in ["в", "х", "взять", "хватит"]:
                    choice = input("Пожалуйста, введите 'взять' или 'хватит' (или В/Х): ").lower()
                
                if choice in ['взять', 'в']:
                    self.player_hand.add_card(self.deck.deal())
                    self.player_hand.display()
                    if self.player_is_over():
                        print("Вы проиграли!")
                        game_over = True
                else:
                    player_hand_value = self.player_hand.get_value()
                    dealer_hand_value = self.dealer_hand.get_value()
                
                    print("Финальные результаты")
                    print("Ваши очки:", player_hand_value)
                    print("Очки дилера:", dealer_hand_value)
                    
                    if player_hand_value > dealer_hand_value:
                        print("Вы победили!")
                    elif player_hand_value == dealer_hand_value:
                        print("Ничья!")
                    else:
                        print("Дилер победил!")
                    game_over = True
                
            again = input("Сыграть ещё раз? [Д/Н] ")
            while again.lower() not in ["д", "н"]:
                again = input("Пожалуйста, введите Д или Н ")
            if again.lower() == "н":
                print("Спасибо за игру!")
                playing = False
            else:
                game_over = False
                
    def player_is_over(self):
        return self.player_hand.get_value() > 21
        
    def check_for_blackjack(self):
        player_has_blackjack = False
        dealer_has_blackjack = False
        if self.player_hand.get_value() == 21:
            player_has_blackjack = True
        if self.dealer_hand.get_value() == 21:
            dealer_has_blackjack = True
                
    def show_blackjack_results(self, player_has_blackjack, dealer_has_blackjack):
        if player_has_blackjack and dealer_has_blackjack:
            print("Блекджек у обоих! Ничья!")
        elif player_has_blackjack:
            print("У вас Блекджек! Вы выиграли!")
        elif dealer_has_blackjack:
            print("У дилера Блекджек! Вы проиграли!")
    
if __name__ == "__main__":
    game = Game()
    game.play()