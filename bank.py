import json
import casino
# Bank Klasse
class Bank:
    # Bank Menue mit auswahl über Auszahlen, Einzahlen und Beenden
    def main(self):
        while True:
            print("Willkommen zu Ihrem Konto")
            print("(a) Einzahlen")
            print("(b) Auszahlen")
            print("(c) Zurück")

            auswahl = input("Bitte wählen Sie eine Option: ")

            if auswahl == "a":
                self.einzahlung()
            elif auswahl == "b":
                self.auszahlung()
            elif auswahl == "c":
                print("Zurück zum Casino ")
                casino_instanze = casino.Casino()
                casino_instanze.menue()
            else:
                print("Ungültige Eingabe. Bitte wählen Sie erneut.")
    #Funktion zum einzahlen von Geld auf das Konto, Name wird in der JSON gesucht und bearbeitet
    def einzahlung(self):
        name = input("Geben Sie Ihren Namen ein: ")
        betrag = float(input("Geben Sie den Betrag ein, den sie einzahlen möchten: "))

        with open("konten.json", "r+") as datei:
            konten = datei.readlines()

            for i, konto in enumerate(konten):
                konto = json.loads(konto)
                if konto["name"] == name:
                    konto["balance"] += betrag
                    konten[i] = json.dumps(konto) + '\n'
                    datei.seek(0)
                    datei.writelines(konten)
                    print("Konto erfolgreich aufgeladen.Aktueller Kontostand: " + str(konto["balance"]))
                    return

        print("Konto nicht gefunden.")
    #Funktion zum Auszahlen von Geld, Name als wird in der JSON gesucht und dann bearbeitet
    def auszahlung(self):
        name = input("Geben sie Ihren Namen ein:  ")
        betrag = float(input("Geben Sie den Betrag ein, welche sie Auszahlen möchten:  "))

        with open("konten.json", "r+") as datei:
            konten = datei.readlines()

            for i, konto in enumerate(konten):
                konto = json.loads(konto)
                if konto["name"] == name:
                 if konto["balance"] >= betrag:
                    konto["balance"] -= betrag
                    konten[i] = json.dumps(konto) + '\n'
                    datei.seek(0)
                    datei.writelines(konten)
                    print("Erfolgreich ausgezahlt. Aktueller Kontostand: " + str(konto["balance"]))
                 else:
                    print("Sie haben nicht genügend Geld auf dem Konto")
                    return

        print("Konto nicht gefunden.")


