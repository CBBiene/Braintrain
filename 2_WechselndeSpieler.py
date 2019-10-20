#Copy Cat

import RPi.GPIO as GPIO
from time import sleep
import random   #Generiert Zufallszahlen

def getPress():
    pressed = False
    while pressed == False:
        for test in range(0,4):
        #Taster gedrückt
            if GPIO.input(buttons[test]) == False:
                GPIO.output(leds[test],1)
                pressed = True
                sleep(0.05) #Entprellen
        #Halten bis Taster losgelassen wird
                while GPIO.input(buttons[test]) == False:
                    sleep(0.05)
                    GPIO.output(leds[test],0)
                return test
         
def saySeq(length):
    for number in range(0,length):
        GPIO.output(leds[sequence[number]],1) #LED an
        sleep(1.2)
        GPIO.output(leds[sequence[number]],0) #LED aus
        sleep(0.5)

def getSeq(length):
    print("Du bist dran")
    for press in range(0,length):
        attempt = getPress()
        if attempt != sequence[press]:
            sleep(0.8)
            return -1
    return 1


#maximale Sequenzlänge/ Farbfolgen
maxLength = 10
sequence = [ random.randint(0,3) for c in range(0,maxLength)]

leds = [16, 12, 20, 21]
buttons = [13, 19, 6, 5]

print("Willkommen beim Spiel Copy-Cat")
#Echte GPIO Nummerierung verwenden
GPIO.setmode(GPIO.BCM)
#Irritierende Warnungen unterdrücken
GPIO.setwarnings(False)
for pin in leds:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, 0) # LEDs abschalten
for pin in buttons:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
maxFails = 3

a = int(input("Bitte gib die Anzahl der Spieler ein: "))
if a == 1:
        name = input("Bitte gib deinen Namen ein: ")
        print("Hallo " + name)
elif a == 2:
        name = input("Bitte gib deinen Namen ein: ")
        name2 = input("Spieler 2, bitte gib deinen Namen ein: ")
        print("Hallo " + name + " und " + name2)
elif a == 3:
        name = input("Bitte gib deinen Namen ein: ")
        name2 = input("Spieler 2, bitte gib deinen Namen ein: ")
        name3 = input("Spieler 3, bitte gib deinen Namen ein: ")
        print("Hallo " + name + " und " + name2 + " und " + name3)
elif a == 4:
        name = input("Bitte gib deinen Namen ein: ")
        name2 = input("Spieler 2, bitte gib deinen Namen ein: ")
        name3 = input("Spieler 3, bitte gib deinen Namen ein: ")
        name4 = input("Spieler 4, bitte gib deinen Namen ein: ")
        print("Hallo " + name + " und " + name2 + " und " + name3 + " und " + name4)
elif a > 4:
        print("Leider sind nur bis zu vier Spieler möglich")
elif ( a < 1 or a > 4):
        input("Bitte gib eine gültige Spieleranzahl ein 1-4:  ")
 
# Endlosschleife
while True:
    #Anzahl der Fehlversuche
        fail = 0 
    #neue Abfolge Erzeugen
        for c in range(0, maxLength):
            sequence[c] = random.randint(0,3) #weil vier farben genutzt werden
        far = 2
    # Anzahl der Fehlversuche vor Reset
        while fail < maxFails:
            print("Tippe die ", far , "Farben nach")
            sleep(500)
            saySeq(far)
            if getSeq(far) != -1:
                far = far + 1
                print("Super! Nun etwas Schwieriger!")
                fail = 0 #Anzahl der Fehlversuche zurücksetzen
            else:
                fail = fail +1
                print("Das War nicht richtig", fail,"Fehlversuche")
                if fail < maxFails:
                    print("Versuche es noch einmal")
            sleep(1.5)
            if far > maxLength:
                print("Superhirn - Gut gemacht!")
                exit() #Beschiss annehmen
        print("Game over - Punkte: ",far-1)
        print("Spieler 2 ist an der Reihe")
        sleep(2.0)
    

