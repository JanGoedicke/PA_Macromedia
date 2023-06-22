#PA_Macromedia#

Overview:

 This is a small and simple Casino game where you can play 2 different games and can manage your Account.

 You will start in a Menue where you can:
 -Create an Account
 -Login to an Account(If you have created one)
 -End the Programm
 The Accounts will be saved in a JSON Document called Konto.json.

if you login successfully you will be brought into the casino menu where you can:
-Manage your Account Ballance
-Show the possible Games
-End the menu

There Are 2 Possible Games, Black Jack, and Roulette you can play.
You will have to place a bit every time you wanna play.
If you win you get double the amount back.

You can charge or discharge your account in the Ballance Menue 

The in Programm Menue is on german langauge 

Installation:

DowlLoad:
bank.py, casino.py, main.py, and konten.json.
Make sure they are in the same folder.

Usage:

-Create an Account in the first menu
-Login to that Account 
-Charge your Ballance in the Ballance Menue
-Chose a game you wanna play and place your bet

License:
-MIT

Errors:
-Sometimes there is an issue with the JSON Data, make sure the first line isn't empty after you already created  an Account 
-If you type no Int Vallues in the bet function you will have to start from the beginning 
- Sometimes after a Win or loss in a game it will kick you back to the Login screen

