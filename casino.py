import random
import json
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
        print(" (b) Roulett-Lite")
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

            wahl = input("Willst du noch eine Karte Ziehen tippe (h) oder keine Karte mehr(s) ")
            if wahl == "h":
                self.Spieler.append(self.hit())
                if self.hand_value(self.Spieler) > 21:
                    break
            elif wahl == "s":
                break
            else:
                print(" Das hat nicht geklappt versuchen sie es erneut!")


    def dealer_turn(self):
        while self.hand_value(self.Dealer) < 17 and self.hand_value(self.Dealer) < self.hand_value(self.Spieler):
            self.Dealer.append(self.hit())



    def end(self, result):
        print("Deine Hand:", self.Spieler)
        print("Dealers Hand:", self.Dealer)
        print(result)
        # casino_instanze = Casino()
        # casino_instanze.show_games()


    def start_game(self):
        print("Willkommen bei BlackJack-Lite")
        print(" Gespiel wird wie folgt:")
        print(" Bei den Karten wird die Farbe nicht berücksichtigt sondern nur der Wert den eine Karte hat")
        print(" Sie Bekommen 2 Karten und müssen entscheiden ob sie noch eine weiter wollen oder nicht")
        print(" Das Ziel ist es so nah an 21 ran zu kommen wie möglich")
        self.Spieler = [self.hit(), self.hit()]
        self.Dealer = [self.hit(), self.hit()]

        self.place_bet()
        self.player_turn()
        self.dealer_turn()
        player_value = self.hand_value(self.Spieler)
        dealer_value = self.hand_value(self.Dealer)

        if dealer_value > 21:
            self.win_bet()
            self.end("Dealer über 21, Du gewinnst")
        elif player_value > 21:
            self.end( " Du bist über 21, Dealer gewinnt, deine Wette geht an die Bank")
        elif player_value < dealer_value:
            self.end("Dealer gewinnt, deine Wette geht an die Bank")
        elif player_value > dealer_value:
            self.win_bet()
            self.end("Du gewinnst")
        else:
           self.end("Unentschieden ") #BANK GEWINNT?

    def place_bet(self):
        self.bet_name = input("Geben sie Ihren Namen ein:  ")
        bet = int(input("Geben sie ein Betrag ein den sie setzten möchten:  "))
        name = self.bet_name
        betrag = bet

        with open("konten.json", "r+") as datei:
            konten = datei.readlines()
            #Funktionsweise von folgenden Code von ChatGPT ↓
            for i, konto in enumerate(konten):
                konto = json.loads(konto)
                if konto["name"] == name:
                    konto["balance"] -= betrag
                    konten[i] = json.dumps(konto) + '\n'
                    datei.seek(0)
                    datei.writelines(konten)
                    print("Du hast", bet, "$ gesetzt viel Glück!. Aktueller Kontostand: " + str(konto["balance"]))

                    return

    def win_bet(self):
        name = self.bet_name
        betrag = 2

        with open("konten.json", "r+") as datei:
            konten = datei.readlines()
            # Funktionsweise von folgenden Code von ChatGPT ↓
            for i, konto in enumerate(konten):
                konto = json.loads(konto)
                if konto["name"] == name:
                    konto["balance"] += betrag
                    konten[i] = json.dumps(konto) + '\n'
                    datei.seek(0)
                    datei.writelines(konten)
                    print("Du hast", betrag, "$ gewonnen!. Aktueller Kontostand: " + str(konto["balance"]))
                    return

class Roulette:
    def __init__(self):
        self.green_numbers = [0]
        self.red_numbers = [1,3,5,7,9,12,14,16,18, 19,21,23,25,27,30,32,34,36 ]
        self.black_numbers =[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]

    def spin(self):
        self.result = random.choice(self.red_numbers + self.green_numbers + self.black_numbers)
        if self.result in self.green_numbers:
            self.color = "Green"
        elif self.result in self.red_numbers:
            self.color = "Red"
        elif self.result in self.black_numbers:
            self.color = "Black"
        else:
            print("ERROR")
        return self.result, self.color
    def play_game(self):
        print("Welcome to Roulette-Lite")
        print("Chose what you want to do:")
        print("(a)Guess on a color ")
        print("(b)Guess on a number")
        wahl = input()

        if wahl == "a":
            print("Bet on a color")
            self.bet_color()
        elif wahl == "b":
            print("Bet on a number")
            self.bet_number()
        else:
            print("Error")



    def bet_number(self):
        number_guess = int(input("Which Number is going to show up?")  )
        self.spin()
        if number_guess == self.result:
            print("You Won!")
        else:
            print("The Ball landed on", self.result, self.color, "you loose")

    def bet_color(self):
        print("Which color is going to show up?")
        print(" Green")
        print(" Red")
        print(" Black")

        wahl_color = input()

        if wahl_color == self.color:
            print("You Won!")
        else:
            print("Ball landed on", self.result, self.color, "you loose")



