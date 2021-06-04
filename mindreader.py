import sys
import time
import random


def hello():
    print("Howdy! \nI'm a mind-reader bot. \nThink of a number from 1 to 10.")


def choice():
    print("When you have decided your number, type ''GO'' and click the 'enter' key.")

    while True:
        answer = input(">")

        if "GO" in answer.upper():
            print("Good! Let's go!")
            break

        else:
            print("What was that? Just type ''GO'' when you are ready! :)")
            continue


def mindreading():
    num = random.randint(0,10)
    print("Now, let me think...")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("I think I got it.")
    time.sleep(1)
    print("Aha! Your number is ", num, ", right?   (Type 'YES' or 'NO')")

def solution():
    while True:
        answer = input (">")

        if "YES" in answer.upper():
            print("I am now inside your brain! >:)")
            time.sleep(3)
            quit()

        elif "NO" in answer.upper():
            print("Wh- what? D:")
            time.sleep(2)
            print("You are a liar! D:<")
            
            ####ADD STH ANGERED
            
            print("Ok. I calmed down. Sorry about that. :( For now, have a good day.")
            time.sleep(3)
            quit()
        else:
            print("Just say 'YES' or 'NO'. Was that your number?")
            continue

        
            

hello()
choice()
mindreading()
solution()