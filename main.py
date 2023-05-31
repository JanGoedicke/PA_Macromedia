import json
import casino


def konto_erstellen():
    name = input("Geben Sie Ihren Namen ein: ")
    passwort = input("Geben Sie Ihr Passwort ein: ")
    balance = 0

    konto = {
        "name": name,
        "passwort": passwort,
        "balance": balance
    }

    with open("konten.json", "a") as datei:
        json.dump(konto, datei)
        datei.write('\n')

    print("Konto erfolgreich erstellt.")


def einloggen():
    name = input("Geben Sie Ihren Namen ein: ")
    passwort = input("Geben Sie Ihr Passwort ein: ")

    with open("konten.json", "r") as datei:
        konten = datei.readlines()

    for konto in konten:
        konto = json.loads(konto)
        if konto["name"] == name and konto["passwort"] == passwort:
            print("Erfolgreich eingeloggt.")
            casino_instanze = casino.Casino()
            casino_instanze.menue()

            return
    print("Falscher Benutzername oder Passwort.")


def startseite():
    while True:
        print("Login Heaven Casino")
        print("(a). Konto erstellen")
        print("(b). Einloggen")
        print("(c). Beenden")

        auswahl = input("Bitte wählen Sie eine Option: ")

        if auswahl == "a":
            konto_erstellen()
        elif auswahl == "b":
            einloggen()
        elif auswahl == "c":
            break
        else:
            print("Ungültige Eingabe. Bitte wählen Sie erneut.")


startseite()
