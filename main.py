import json
import casino

#Kontoerstellen welches in einer Json als string gespeichert wird
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
        datei.write(json.dumps(konto) + '\n')

    print("Konto erfolgreich erstellt.")

# JSON datei wird nach dem Namen + Passwort überprüft
def einloggen():
    name = input("Geben Sie Ihren Namen ein: ")
    passwort = input("Geben Sie Ihr Passwort ein: ")

    with open("konten.json", "r") as datei:
        konten = datei.readlines()

    for konto_str in konten:
        konto = json.loads(konto_str)
        if konto["name"] == name and konto["passwort"] == passwort:
            print("Erfolgreich eingeloggt.")
            casino_instanze = casino.Casino()
            casino_instanze.menue()
            return

        print("Passwort oder Benutzername falsch. Bitte versuchen Sie es erneut.")


# Startseite wo durch die Eingabe von a,b,c jeweils andere Funktionen des Programm ausgeführt werden
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


if __name__ == '__main__':
    startseite()
