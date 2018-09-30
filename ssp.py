#D� man k�r det h�r programmet kommer man att f� spela det klassiska spelet "Sten, Sax, P�se!" mot datorn.
#Spelaren f�r sj�lv v�lja hur m�nga po�ng som kr�vs f�r att vinna.
#Spelet h�ller p� tills antingen spelaren eller datorn har f�tt den m�ngd po�ng som kr�vs f�r att vinna.

#Det kommer att beh�vas random som m�ste importeras. Det kommer att kr�vas att resultaten sparas mellan rundorna.


#-- coding: utf-8 --
import random


print "*******************"
print "ROCK PAPER SCISSORS"
print "*******************"
print
print "Regler:"
print "V�lj f�rst hur m�nga po�ng som kr�vs f�r att vinna."
print "V�lj sedan 1 f�r sten, 2 f�r sax eller 3 f�r p�se."
print "Kom ih�g, sten vinnar sax, sax vinner p�se och p�se vinner sten."
print 
total_score = input("Hur m�nga po�ng kr�vs f�r att vinna? ")

user_score = 0
computer_score = 0

def checkResults(user,computer):
    #Spelaren vinner:
    if user == 0 and computer == 1:
        user_score += 1
        print "Du vann rundan!"
    elif user == 1 and computer == 2:
        user_score += 1
        print "Du vann rundan!"
    elif user == 2 and computer == 0:
        user_score += 1
        print "Du vann rundan!"
    #Datorn vinner:
    else:
        print "Du f�rlorade rundan."
        computer_score +=1

def round():
    user_choice = input("V�lj 1:Sten, 2:Sax, 3:P�se  ")
    #Kolla om spelarens input �r mellan 1-3 (0=sten, 1=sax, 2= p�se)
    computer_choice = random.randint(0,2)
    checkResults(user_choice,computer_choice)
    if user_score == total_score:
        print "Du vann spelet!"
    elif computer_score == total_score:
        print "Du f�rlorade spelet."
    else:
        round()
round()
