import json
import casino

class Bank:
    def main(self):
        while True:
            print("Willkommen zu Ihrem Konto")
            print("(a) Einzahlen")
            print("(b) Auszahlen")
            print("(c) Beenden")

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
                    print("Konto erfolgreich aufgeladen.")
                    return

        print("Konto nicht gefunden.")

    def auszahlung(self):
        name = input("Geben sie Ihren Namen ein:  ")
        betrag = float(input("Geben Sie den Betrag ein, welche sie Auszahlen möchten:  "))

        with open("konten.json", "r+") as datei:
            konten = datei.readlines()

            for i, konto in enumerate(konten):
                konto = json.loads(konto)
                if konto["name"] == name:
                    konto["balance"] -= betrag
                    konten[i] = json.dumps(konto) + '\n'
                    datei.seek(0)
                    datei.writelines(konten)
                    print("Erfolgreich ausgezahlt. Aktueller Kontostand: " + str(konto["balance"]))

                    return

        print("Konto nicht gefunden.")
# Auszahlung

