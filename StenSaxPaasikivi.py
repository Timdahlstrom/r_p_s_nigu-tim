# -- coding: utf-8 --
import random

def startPrint():
    print "*****************"
    print "Sten Sax Påse"
    print "*****************"
    print
    print "Regler:"
    print "Välj först hur många poäng som krävs för att vinna"
    print "Välj sedan din spelhand"
    print "Sten vinner sax, paper vinner sten och sax vinner påse"
    print


def checkResults(user, computer):
        if user_score == total_score:
            print "\nDu vann Sten Sax Påse!"
            print "Dina poäng är följande: ", user_score
            print "Datorns poäng är följande: ", computer_score
            print

        elif computer_score == total_score:
            print "\nDu förlorade Sten Sax Påse!"
            print "Dina poäng är fljande: ", user_score
            print "Datorns poäng är följande: ", computer_score
            print

        else:
            if user == computer:
                print "Oavgjort"
            elif user == "Sten":
                if computer == "Påse":
                    print "Du förlorade"
                    return computer_score + 1
                else:
                    print "Du vann!"
                    return user_score + 1
            elif user == "Sax":
                if computer == "Sten":
                    print "Du förlorade"
                    return computer_score + 1
                else:
                    print "Du vann!"
                    return user_score + 1
            elif user == "Påse":
                if computer == "Sax":
                    print "Du förlorade"
                    return computer_score + 1
                else:
                    print "Du vann!"
                    return user_score + 1
            else:
                print "Ett fel uppstod, kolla stavningen."



def main():
    user_score = 0
    computer_score = 0
    startPrint()
    total_score = input("hur många poäng krävs för att vinna?: ")
    while user_score < total_score and computer_score < total_score:
        user_choice = raw_input("Välj Sten, Sax eller Påse: ")
        t = ["Sten", "Sax", "Påse"]
        computer_choice = t[random.randint(0, 2)]
        checkResults(user_choice, computer_choice)


main()