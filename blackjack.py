from random import shuffle
from time import sleep

class Game:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.rank_values = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
            'Jack': 10, 'Queen': 10, 'King': 10
        }


        self.deck = [(rank, suit) for suit in self.suits for rank in self.ranks]

        shuffle(self.deck)

        self.agent_cards = [self.deck.pop(),self.deck.pop()]
        self.agent_score = self.get_score(self.agent_cards)

        self.player_cards = [self.deck.pop(),self.deck.pop()]
        self.player_score = self.get_score(self.player_cards)

        self.dealer_cards = [self.deck.pop()]
        self.dealer_score = self.get_score(self.dealer_cards)

        self.turn = "player"

    def get_score(self, cards):

        score = 0
        
        for i in cards:
            if i[0] == "Ace":
                if score<=10:
                    score+=11
                else:
                    score+=1
            else:
                score += self.rank_values[i[0]]

        return score
    
    def update_score(self,score,card):

        score+= self.rank_values[card[0]]

        return score
    
    def player_move(self):
        while True:
            try:
                action = input("Your move(hit or stand): ")

                assert action.lower() in ["hit","stand"]

                if action == "hit":
                    self.player_cards.append(self.deck.pop())
                    self.player_score = self.update_score(self.player_score,self.player_cards[-1])

                    if self.player_score>21:
                        self.done = True
                        print("Dealer cards:")        
                        print(f"{self.dealer_cards} Score: {self.dealer_score}")
                        print("\nYour cards:")
                        print(f"{self.player_cards} Score: {self.player_score}\n")
                        print("You lost")
                        break
                    print("Dealer cards:")        
                    print(f"{self.dealer_cards} Score: {self.dealer_score}")
                    print("\nYour cards:")
                    print(f"{self.player_cards} Score: {self.player_score}\n")
                elif action == "stand":
                    self.turn = "agent"
                    break
                
            except AssertionError:
                print("Invalid input")
    def agent_move(self):
        print("\nAgent moved\n")
        self.turn = "player"

    def run(self):
        self.done = False

        while not self.done:
            if self.turn == "player":
                sleep(0.5)
                print("Dealer cards:")        
                print(f"{self.dealer_cards} Score: {self.get_score(self.dealer_cards)}")

                print("\nYour cards:")
                print(f"{self.player_cards} Score: {self.get_score(self.player_cards)}\n")

                self.player_move()
            
            elif self.turn == "agent":
                self.agent_move()

            



if __name__ == "__main__":

    a = Game()

    a.run()

