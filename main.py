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
def gewonnen():
    global r
    print("Gewonnen! Het woord was:", woord)
    r = False

woorden = d.get_ranked()

random.shuffle(woorden)
woord = random.choice(woorden)
grwoord = str("-"*len(woord))
grlijst = []
vletters = " "
for x in range(len(woord)):
    grlijst.append("-")
while r:
    if vletters == " ":
        while True:
            letter = input(f"Je hebt al geraden: {grwoord}\nKies een letter of kies ? om het geheime woord te raden: ").lower()
            if letter.isdigit():
                print("Dat is geen letter!")
            else:
                break
            sleep(1)
    else:
        while True:
            letter = input(f"Je hebt al geraden: {grwoord}\nVerkeerde letters zijn: {vletters}\nKies een letter of kies ? om het geheime woord te raden: ")
            if letter.isdigit():
                print("Dat is geen letter!")
            else:
                break
            sleep(1)
    if letter == "?":
        print("Je wilt een poging doen?")
        sleep(1)
        rwoord = input("Raad het geheime woord: ").lower()
        if rwoord != woord:
            hlevel += 1
            fout()
        else:
            gewonnen()
    elif letter in woord:
        for x in range(len(woord)):
            if woord[x] == letter:
                pos = x
                grlijst[x] = woord[x]
        grwoord = ""
        for x in range(len(woord)):
            grwoord += f"{grlijst[x]}"
        print(f"Je hebt geraden: {grwoord}")
        if grwoord == woord:
            gewonnen()
    else:
        hlevel += 1
        fout()
        vletters += letter

    sleep(1)