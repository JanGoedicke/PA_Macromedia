import random
import json
import bank
#Casino Hauptklasse
class Casino:
    def __init__(self):
        print("Willkommen im Heaven Casino ihrer Wohlfühlplatform")
    # Menue wo durch die Eingabe von a,b,c jeweils ein Spiel oder funktion ausgeführt wird
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
    # Menue welches die mögliche Spiele zur Auswahl zeigt, durch a,b,c kann gewählt werden
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
            roulette = Roulette()
            roulette.play_game()
        elif game_wahl == "c":
            print("Zurück zum Hauptmenue")
            self.menue()
        else:
            print("Das hat nicht funktioniert versuchen sie es erneut")
            self.show_games()

    # Bei Wahl von Guthaben verwalten wird die bank.py gestartet
    def balance(self):
        print("Sie werden zu ihrer Kontoübersicht weitergeleitet")
        bank_instance = bank.Bank()
        bank_instance.main()
    def exit(self):
        print("Danke für ihren besuch im Heaven Casino ")
        raise SystemExit
#BlackJack Klasse
class Blackjack:
    def __init__(self):
        self.deck = self.Deck()
        self.Spieler = []
        self.Dealer = []
        self.bet_name = ""
        self.bet = 0
    # Erstellt und misscht das BlackJack-Deck jedoch ohen die Farben der Karte, deshalb jeder wert *4
    def Deck(self):
        values = ["2","3","4","5","6","7","8","9","10"]
        deck = values*4
        random.shuffle(deck)
        return deck
    # Funktion zum ziehen neuer Karte aus dem Deck
    def hit(self):
        card = self.deck.pop()
        return card
    # Funktion berechnet den Wert der Hand des Spielers und Dealers
    def hand_value(self, hand):
        value = 0
        for card in hand:
            value += int(card)
        return value
    # Zug des Spielers es wird ihm seine Hand und die des Dealers gezeigt und er hat die möglichkeit
    # weiter karten zu ziehen oder zu stoppen
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

    # Zug des Dealers zieht solange eine karte wie er unter 17 ist und die Hand-Value niedriger ist als die des Spielers
    def dealer_turn(self):
        while self.hand_value(self.Dealer) < 17 and self.hand_value(self.Dealer) < self.hand_value(self.Spieler):
            self.Dealer.append(self.hit())


    # Ende von Blackjack
    def end(self, result):
        print("Deine Hand:", self.Spieler)
        print("Dealers Hand:", self.Dealer)
        print(result)




    # Blackjack Spiel Start erklärt regeln und erstellt dann die Hand von Spieler und Dealer
    # Lässt den Spieler die Wette Platzieren
    # Zug des Spielers
    # Zug des Dealers
    # Hat verschiedene Kriterien an dennen entschieden wird wer gewonnen hat und ermittelt anhand dieser den Gewinner
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
            self.end("Dealer über 21, Du gewinnst")
            self.win_bet()
        elif player_value > 21:
            self.end( " Du bist über 21, Dealer gewinnt, deine Wette geht an die Bank")
        elif player_value < dealer_value:
            self.end("Dealer gewinnt, deine Wette geht an die Bank")
        elif player_value > dealer_value:
            self.end("Du gewinnst")
            self.win_bet()
        else:
           self.end("Unentschieden ") #BANK GEWINNT?
    # Funktion zum setzten der Wette, Eingabe von Namen + Betrag zum finden in der JSON und dann wird der Betrag
    # vom Konto Abgezogen
    def place_bet(self):
        self.bet_name = input("Geben sie Ihren Namen ein:  ")
        self.bet = int(input("Geben sie ein Betrag ein den sie setzten möchten:  "))
        name = self.bet_name
        betrag = self.bet
        # öffnet JSON und vergleicht eingabe Namen mit gespeicherten Namen und zieht dann den Betrag vom Konto ab.
        with open("konten.json", "r+") as datei:
            konten = datei.readlines()
            # Funktionsweise von folgenden Code von ChatGPT und dann angepasst ↓
            for i, konto in enumerate(konten):
                konto = json.loads(konto)
                if konto["name"] == name:
                    konto["balance"] -= betrag
                    konten[i] = json.dumps(konto) + '\n'
                    datei.seek(0)
                    datei.writelines(konten)
                    print("Du hast", self.bet, "$ gesetzt viel Glück!. Aktueller Kontostand: " + str(konto["balance"]))


                    return
            print("Konto nicht gefunden!")
            #-----------------------------------------------#
    # Funktion falls Wette aufgeht, Verdoppelt den Einsatz öffnet die JSON und schreibt dem Spieler das Geld gut.
    def win_bet(self):
        name = self.bet_name
        betrag = self.bet*2

        with open("konten.json", "r+") as datei:
            konten = datei.readlines()

            for i, konto in enumerate(konten):
                konto = json.loads(konto)
                if konto["name"] == name:
                    konto["balance"] += betrag
                    konten[i] = json.dumps(konto) + '\n'
                    datei.seek(0)
                    datei.writelines(konten)
                    print("Du hast", betrag, "$ gewonnen!. Aktueller Kontostand: " + str(konto["balance"]))
                    return

# Roulett Klasse
class Roulette:
    def __init__(self):
        self.green_numbers = [0]
        self.red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        self.black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        self.color = ""
        self.result = None
        self.bet_name = ""
        self.bet = 0
    # Funktion zum drehen des Rads, wählt zufällige Nummer, diese Nummern sind in Farben ein geteielt.
    def spin(self):
        self.result = random.choice(self.red_numbers + self.green_numbers + self.black_numbers)
        if self.result in self.green_numbers:
            self.color = "Grün"
        elif self.result in self.red_numbers:
            self.color = "Rot"
        elif self.result in self.black_numbers:
            self.color = "Schwarz"
        else:
            raise ValueError("Invalid result!")
    # Startet das Spiel und gibt Auswahl über die 2 Modi
    def play_game(self):
        print("Willkommen zu Roulett-Lite")
        print("Welchen Modus möchten sie Spielen:")
        print("(a) Auf eine Farbe wetten")
        print("(b) Auf eine Nummer wetten")
        choice = input()

        if choice == "a":
            print("Auf eine Farbe wetten")
            self.bet_color()
        elif choice == "b":
            print("Auf eine Nummer wetten")
            self.bet_number()
        else:
            print("Error")
    # Modi 1 auf eine Nummer Wetten, wenn geraten Nummer = durch Spin ausgewählte Nummer hat man gewonnen
    def bet_number(self):
        self.place_bet()
        self.spin()
        number_guess = int(input("Auf welcher Nummer wird der Ball landen?"))
        if number_guess == self.result:
            print("Der Ball ist auf ", self.result, self.color, "gelandet du gewinnst!")
            self.win_bet()
        else:
            print("Der ball ist auf", self.result, self.color, "gelandet du verlierst")
    # Modi 2 auf eine Farbe wetten, wenn geratene Farbe = durch Spin ausgewählte Farbe hat man gewonnen
    def bet_color(self):
        self.place_bet()
        self.spin()
        print("Auf welcher Farbe wird der Ball landen?")
        print("Grün")
        print("Rot")
        print("Schwarz")
        color_guess = input().lower()

        if color_guess == self.color.lower():
            print("Der Ball ist auf ", self.result, self.color, "gelandet du gewinnst!")
            self.win_bet()
        else:
            print("Der Ball ist auf ", self.result, self.color, "gelandet du verlierst!")
    # Siehe oben
    def place_bet(self):
        self.bet_name = input("Geben sie Ihren Namen ein:  ")
        self.bet = int(input("Geben sie ein Betrag ein den sie setzten möchten:  "))
        name = self.bet_name
        betrag = self.bet

        with open("konten.json", "r+") as datei:
            konten = datei.readlines()

            for i, konto in enumerate(konten):
                konto = json.loads(konto)
                if konto["name"] == name:
                    konto["balance"] -= betrag
                    konten[i] = json.dumps(konto) + '\n'
                    datei.seek(0)
                    datei.writelines(konten)
                    print("Du hast", self.bet, "$ gesetzt viel Glück!. Aktueller Kontostand: " + str(konto["balance"]))

                    return
    # Siehe oben
    def win_bet(self):
        name = self.bet_name
        betrag = self.bet*2

        with open("konten.json", "r+") as datei:
            konten = datei.readlines()

            for i, konto in enumerate(konten):
                konto = json.loads(konto)
                if konto["name"] == name:
                    konto["balance"] += betrag
                    konten[i] = json.dumps(konto) + '\n'
                    datei.seek(0)
                    datei.writelines(konten)
                    print("Du hast", betrag, "$ gewonnen!. Aktueller Kontostand: " + str(konto["balance"]))
                    return
