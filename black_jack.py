"""
Module for playing BlackJack
"""
import random

class Enter():
    """
Class for proper enrty of input
    """
    def one_eleven():
        """
Picking A's value 1 or 11
        """
        while True:
            value = input("A is 1 or 11: ")
            if value not in ["1", "11"]:
                print("Choose between 1 and 11 only")
                continue
            return int(value)


    def lobby():
        """
Picking Options for lobby
        """
        Options.lobby()
        while True:
            value = input("Choose a number: ")
            if value not in ["1", "2"]:
                Options.lobby()
                continue
            return value


    def round():
        """
Picking Options for round
        """
        Options.round()
        while True:
            value = input("Choose a number: ")
            if value not in ["1", "2"]:
                Options.round()
                continue
            return value

    def game(player, dealer):
        """
Picking Options for game
        """
        Options.game()
        while True:
            print("Player has: {}\n".format(player.cards))
            dealer.show_dealer()
            value = input("Choose a number: ")
            if value not in ["1", "2", "3", "4", "5"]:
                Options.game()
                continue
            return value


    def money():
        """
Entering players money
        """
        while True:
            value = input("Quantity of money: ")
            if not value.isdigit():
                print("Please input only numbers\n")
                continue
            return int(value)

    def bet():
        """
Entering players bet
        """
        while True:
            value = input("Quantity of bet: ")
            if not value.isdigit():
                print("Please input only numbers\n")
                continue
            return int(value)


class Options():
    """
A simple class for info
    """
    def lobby():
        """
info about lobby
        """
        print("""[1] - Play game
[2] - Exit Game\n """)

    def round():
        """
info about round
        """
        print("""\n[1] - Bet
[2] - Quit\n""")

    def game():
        """
info about game
        """
        print("""\n[1] - Hit
[2] - Stand/Stand pat/Stick/Stay
[3] - Double Down(only on first hand)
[4] - Surrender
[5] - Split\n""")

class Deck():
    """
Deck functions and others
    """
    def cards():
        """
Initialising deck
        """
        kards = ["A", "A", "A", "A", "2", "2", "2", "2", "3", "3", "3", "3",
                 "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6",
                 "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9",
                 "10", "10", "10", "10", "J", "J", "J", "J", "Q", "Q", "Q", "Q",
                 "K", "K", "K", "K"]
        random.shuffle(kards)
        return kards

    def take(deck):
        """
Taking from deck
        """
        return deck.pop(0)

class Hand():
    """
Detalis about the Dealer or Players
    """
    def __init__(self, name, money):
        """
Initialising player
        """
        self.name = name
        self.money = money
        self.bet = [0]
        self.cards = [[]]
        self.wins = 0
        self.loses = 0
        self.ties = 0

    def start(self, deck):
        """
Staring round
        """
        self.cards = [[]]
        self.cards[0].append(Deck.take(deck))
        self.cards[0].append(Deck.take(deck))

    def won(self, num):
        """
Player won and won count increases
        """
        print(f"{self.cards}\nPlayer wins")
        self.money += self.bet[num]
        self.wins += 1
        print(self)

    def lost(self, num):
        """
Player lost and lost count increases
        """
        print(f"{self.cards}\nPlayer loses")
        self.money -= self.bet[num]
        self.loses += 1
        print(self)

    def tied(self):
        """
Player tied and tied count increases
        """
        print("Player ties")
        self.ties += 1
        print(self)

    def inbet(self, bet):
        """
Player inputs bet
        """
        self.bet.append(bet)

    def hit_p(self, deck, num):
        """
Player hits and take a card from deck
        """
        self.cards[num].append(Deck.take(deck))
        print(self.cards)
        if not deck:
            Deck.cards()
        return deck

    def double_down(self, num):
        """
Player doubles bet
        """
        self.bet[num] *= 2

    def split(self, player, deck, num):
        """
Player splits his hand
        """
        if self.cards[num][0] == self.cards[num][1]:
            self.cards.append([self.cards[num].pop(1)])
            self.hit_p(deck, num)
            self.hit_p(deck, -1)
            player.inbet(Enter.bet())
            return 0
        print("\nCan only split identical hand\n")
        return num

    def check21(self, num):
        """
Checking natural Blackjack
        """
        if len(self.cards[num]) == 2:
            if "A" in self.cards[num] and ("10" in self.cards[num]
                                           or "J" in self.cards[num]
                                           or "Q" in self.cards[num]
                                           or "K" in self.cards[num]):
                print(self.cards[num])
                print("BlacJack")
                return True
        return False

    def total_p(self, num):
        """
Checking player's total
        """
        total = 0
        for value in self.cards[num]:
            if value in ["J", "Q", "K"]:
                value = 10
            elif value == "A":
                value = Enter.one_eleven()
            else:
                value = int(value)
            total += value
        return total

    def bust_p(self, num):
        """
Checking if player busts
        """
        result = self.total_p(num)
        if result > 21:
            print("Busted")
            return True
        print("Safe")
        return False

    def total_comp(cds):
        """
Checking dealer's total
        """
        total = 0
        for value in cds:
            if value in ["J", "Q", "K"]:
                value = 10
            elif value == "A":
                value = 1
            else:
                value = int(value)
            total += value
        if "A" in cds and (total + 10) <= 21:
            total += 10
        return total

    def hit_comp(self, deck):
        """
Increasing dealer's total
        """
        while True:
            kards = self.cards[0]
            kards.append(deck[0])
            if Hand.total_comp(kards) == 17:
                kards.pop(-1)
                deck = self.hit_p(deck, 0)
                break
            elif Hand.total_comp(kards) <= 21:
                kards.pop(-1)
                deck = self.hit_p(deck, 0)
            else:
                kards.pop(-1)
                break
        return deck

    def stay(player, dealer, deck):
        """
Stops hitting and checks for result
        """
        num = 0
        done = 0
        while len(player.cards) > num:
            if player.check21(num):
                if dealer.check21(0):
                    player.tied()
                    done += 1
                else:
                    print("\nPlayer has: {}\n".format(player.cards))
                    print("\nDealer has: {}\n".format(dealer.cards))
                    player.bet = player.bet * 1.5
                    player.won(num)
                    player.bet = player.bet / 1.5
                    done += 1
            num += 1
        num = done
        print("Dealer has: {}\n".format(dealer.cards))
        if dealer.check21(0):
            while len(player.cards) >= num:
                num += 1
                player.lost(num)
        deck = Hand.hit_comp(dealer, deck)
        print("After hitting Dealer has: {}\n".format(dealer.cards))
        dtot = Hand.total_comp(dealer.cards[0])
        print("Dealer's total is {}\n".format(dtot))
        while len(player.cards) > num:
            ptot = player.total_p(num)
            print("\nPlayer's total is {}\n".format(ptot))
            if ptot > dtot:
                player.won(num)
            elif ptot < dtot:
                player.lost(num)
            else:
                player.tied()
            num += 1

    def show_dealer(self):
        """
Shows dealer's cards with on face down
        """
        print("Dealer has: {}\n".format(["X"]+self.cards[0][1:]))

    def __str__(self):
        """
Default string format for Hand object
        """
        return """\nName: {}\nMoney: {}$\nBet: {}$\nCards: {}\nWins: {}
Loses: {}\nTies: {}\n""".format(self.name, self.money,
                                self.bet, self.cards,
                                self.wins, self.loses,
                                self.ties)

def game():
    """
the game itself
    """
    player = Hand(input("Your good name please: "), Enter.money())
    dealer = Hand("Dealer", 0)
    deck = Deck.cards()
    while True:
        num = 0
        player.bet = []
        choice = Enter.round()
        if choice == "1":
            player.inbet(Enter.bet())
            player.start(deck)
            #player.cards = [["10", "10"]]
            dealer.start(deck)
            while True and len(player.cards) > num:
                print("\nPlayer's {} hand\n".format(num + 1))
                decision = Enter.game(player, dealer)
                if decision == "1":
                    deck = player.hit_p(deck, num)
                    if player.bust_p(num):
                        player.lost(num)
                        player.cards.pop(num)
                        player.bet.pop(num)

                elif decision == "2":
                    num += 1
                    if len(player.cards) == num:
                        Hand.stay(player, dealer, deck)
                        break

                elif decision == "3":
                    if len(player.cards[num]) == 2:
                        player.double_down(num)
                        deck = player.hit_p(deck, num)
                        if player.bust_p(num):
                            player.lost(num)
                            player.cards.pop(num)
                            player.bet.pop(num)
                            continue
                        num += 1
                        if len(player.cards) == num:
                            Hand.stay(player, dealer, deck)
                            break
                    else:
                        print("\nCan only double down on first hand\n")

                elif decision == "4":
                    print("\nPlayer surrendered\n")
                    player.bet /= 2
                    player.lost(num)
                    player.cards.pop(num)
                    player.bet.pop(num)

                elif decision == "5":
                    num = player.split(player, deck, num)

        elif choice == "2":
            break

if __name__ == "__main__":
    while True:
        choose = Enter.lobby()
        if choose == "1":
            game()
        elif choose == "2":
            exit()
