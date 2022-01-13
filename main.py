import random
from time import sleep
import dutch_words as d

# Je moet in command prompt of de ene mac terminal "pip install dutch_words" typen en dan enter
# Alleen dan werkt het

hlevel = 0

r = True

hl1 = ("\n"
      "\n"
      "\n"
      "\n"
      "\n"
      "_______________")
hl2 = ("|\n"
      "|\n"
      "|\n"
      "|\n"
      "|\n"
      "|_____")
hl3 = ("____________\n"
      "|/\n"
      "|\n"
      "|\n"
      "|\n"
      "|_____")
hl4 = ("____________\n"
      "|/         |\n"
      "|\n"
      "|\n"
      "|\n"
      "|_____")
hl5 = ("____________\n"
      "|/         |\n"
      "|         ( )\n"
      "|\n"
      "|\n"
      "|_____")
hl6 = ("____________\n"
      "|/         |\n"
      "|         ( )\n"
      "|         /|\\ \n"
      "|\n"
      "|_____")
hl7 = ("____________\n"
      "|/         |\n"
      "|         ( )\n"
      "|         /|\\ \n"
      "|         / \\ \n"
      "|_____")

def fout():
    global r
    if hlevel == 1:
        print(hl1)
    elif hlevel == 2:
        print(hl2)
    elif hlevel == 3:
        print(hl3)
    elif hlevel == 4:
        print(hl4)
    elif hlevel == 5:
        print(hl5)
    elif hlevel == 6:
        print(hl6)
    elif hlevel == 7:
        print(hl7)
        print("Game Over... :(\nHet juiste woord was:", woord)
        r = False

woorden = []
woord = ""
grwoord = ""
grlijst = []
vletters = " "
glijst = []
def setvar(): # Reset de variablen
    global woorden, woord, grwoord, grlijst, vletters, glijst
    woorden = d.get_ranked() # 10000+ Nederlandse Woorden
    random.shuffle(woorden) # Shuffle de woorden
    woord = random.choice(woorden).lower() # Kies een random nederlands woord
    grwoord = str("-"*len(woord)) # Maak het woord alleen dan met streepjes
    grlijst = [] # Een lijst, heel belangrijk
    vletters = " " # Letters die fout zijn
    glijst = []
    for x in range(len(woord)):
        grlijst.append("-") # Maak het woord alleen dan met streepjes in een lijst

def gewonnen(): # Gewonnen!
    global r
    print("Gewonnen! Het woord was:", woord)
    sleep(1)
    nogeenkeer = input("Wil je nog een keer?(j/n)\n")
    print("Oke!")
    if nogeenkeer == "j": # Wilt de speler nog een keer?
        sleep(1)
        setvar() # Reset de variablen
    else:
        r = False

setvar()
while r: # Galgje loop
    if vletters == " ":
        while True: # Letter invoer loop, voor niet geldige input
            letter = input(f"Je hebt al geraden: {grwoord}\nKies een letter of kies ? om het geheime woord te raden: ").lower()
            if letter.isdigit(): # Is het een cijfer?
                print("Dat is geen letter!")
            elif len(letter) > 1 and letter != "qq": # Is de "letter" langer dan 1?
                print("Je kan maar 1 letter invoeren!")
            
            else: # Zoniet, dan doe dit
                if letter in glijst: # Is de letter al geraden?
                    print(f"Je hebt {letter} al geraden!")
                else:
                    break
            sleep(1)
    else: # Hetzelfde alleen als ^ dan is de vletters variable niet leeg
        while True:
            letter = input(f"Je hebt al geraden: {grwoord}\nVerkeerde letters zijn: {vletters}\nKies een letter of kies ? om het geheime woord te raden: ")
            if letter.isdigit():
                print("Dat is geen letter!")
            elif len(letter) > 1 and letter != "qq":
                print("Je kan maar 1 letter invoeren!")
            else:  # Zoniet, dan doe dit
                if letter in glijst:
                    print(f"Je hebt {letter} al geraden!")
                else:
                    break
            sleep(1)
    if letter == "?": # Wilt de speler het woord raden
        print("Je wilt een poging doen?")
        sleep(1)
        rwoord = input("Raad het geheime woord: ").lower()
        if rwoord != woord: # Is het woord fout?
            hlevel += 1
            fout()
        else: # Is het woord goed?
            gewonnen()
    elif letter in woord: # Is de letter in het woord? (Beste stukje code in dit programma)
        glijst.append(letter)
        for x in range(len(woord)):
            if woord[x] == letter: # Moelijk uit te leggen wat dit allemaal doet, dus ik leg ff niet uit
                pos = x
                grlijst[x] = woord[x]
        grwoord = ""
        for x in range(len(woord)):
            grwoord += f"{grlijst[x]}"
        print(f"Je hebt geraden: {grwoord}")
        if grwoord == woord:
            gewonnen()
    elif letter == "qq": # Wilt de speler dat het programma stopt?
        r = False
    else:
        hlevel += 1
        fout()
        vletters += letter
        glijst.append(letter)

    sleep(1) # Wacht