import random
#import json#
import bank

class Casino:
    def __init__(self):
        print("Willkommen im Heaven Casino ihrer Wohlfühlplatform")

    def menue(self):
            print("Was möchten sie tun?")
            print("(a) Spiele anzeigen")
            print("(b) Guthaben verwalten")
            print("(c) Beenden")
            eingabe = input()

            if eingabe == "a":
                self.show_games()

            elif eingabe == "b":
                self.balance()

            elif eingabe == "c":
                self.exit()

            else:
                print("Das hat nicht funktioniert versuchen sie es erneut")
                self.menue()

    def show_games(self):
        print("Wählen sie ein Spiel")
        print(" (a) BlackJack-Lite ")
        print(" (b)Roulett-Lite")
        print(" (c) Zurück zum Menue")
        game_wahl = input()

        if game_wahl == "a":
            print("BlackJack-Lite wird gestartet")
            blackjack_game = Blackjack()
            blackjack_game.start_game()
        elif game_wahl == "b":
            print("Roulett-Lite wird gestartet")
        elif game_wahl == "c":
            print("Zurück zum Hauptmenue")
            self.menue()
        else:
            print("Das hat nicht funktioniert versuchen sie es erneut")
            self.show_games()


    def balance(self):
        print("Sie werden zu ihrer Kontoübersicht weitergeleitet")
        bank_instance = bank.Bank()
        bank_instance.main()
    def exit(self):
        print("Danke für ihren besuch im Heaven Casino ")
        raise SystemExit



class Blackjack:
    def __init__(self):
        self.deck = self.Deck()
        self.Spieler = []
        self.Dealer = []

    def Deck(self):
        values = ["2","3","4","5","6","7","8","9","10"]
        deck = values*4
        random.shuffle(deck)
        return deck

    def hit(self):
        card = self.deck.pop()
        return card

    def hand_value(self, hand):
        value = 0
        for card in hand:
            value += int(card)
        return value

    def player_turn(self):
        while True:
            print("Deine Hand ist:", self.Spieler)
            int_dealer_cards = list(map(int, self.Dealer))
            print(f"Dealers Hand ist: {', '.join(self.Dealer)}  - summe der Hand ist -> {sum(int_dealer_cards)}")

            wahl = input("Willst du noch eine Karte Ziehen(hit) oder keine Karte mehr(stand) ")
            if wahl.lower().strip()[0] == "h":
                self.Spieler.append(self.hit())
                if self.hand_value(self.Spieler) > 21:
                    break
            elif wahl.lower().strip()[0] == "s":
                break
            else:
                print(" Das hat nicht geklappt versuchen sie es erneut!")


    def dealer_turn(self):
        while self.hand_value(self.Dealer) < 17:
            self.Dealer.append(self.hit())

    def end(self, result):
        print("Deine Hand:", self.Spieler)
        print("Dealers Hand:", self.Dealer)
        print(result)
        casino_instanze = Casino()
        casino_instanze.show_games()


    def start_game(self):
        print("Willkommen bei BlackJack-Lite")
        print(" Gespiel wird wie folgt:")
        print(" Bei den Karten wird die Farbe nicht berücksichtigt sondern nur der Wert den eine Karte hat")
        print(" Sie Bekommen 2 Karten und müssen entscheiden ob sie noch eine weiter wollen oder nicht")
        print(" Das Ziel ist es so nah an 21 ran zu kommen wie möglich")
        self.Spieler = [self.hit(), self.hit()]
        self.Dealer = [self.hit(), self.hit()]


        self.player_turn()
        self.dealer_turn()
        player_value = self.hand_value(self.Spieler)
        dealer_value = self.hand_value(self.Dealer)

        if dealer_value > 21:
            self.end("Dealer über 21, Du gewinnst")
        elif player_value > 21:
            self.end( " Du bist über 21, Dealer gewinnt")
        elif player_value < dealer_value:
            self.end("Dealer gewinnt")
        elif player_value > dealer_value:
            self.end("Du gewinnst")
        else:
           self.end("Unentschieden ")


