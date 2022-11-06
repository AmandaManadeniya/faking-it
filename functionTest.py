import numpy as np 
import random

#only supports one faker
def assignRole(playerNames):
    liar = []
    truthers = []
    random.shuffle(playerNames)
    liar.append(playerNames[0])
    liarName = liar[0]

    for player in playerNames:
        if player == liarName: 
            continue 
        else:
            truthers.append(player)
    print("The faker is: ", str(liar[0]),"- the truthers are: ", truthers)   
    return liarName


def assignQ(liarName, players): 
    questionBank = [] 
    q1 = "Who's most likely to run someone over?"
    q2 = "Who's most likely to get cancelled?"
    q3 = "Who's got the most money?"
    q4 = "Who's the smartest?"
    q5 = "Who's the worst texter?"
    questionBank.extend([q1,q2,q3,q4,q5])

    random_question = random.choice(questionBank)

    fakerQ = "FAKER! player along"

    for player in players: 
        if player == liarName: 
            print(fakerQ)
        else: 
            print(random_question)

def guessFaker(): 
    playerGuess = input("Guess the faker!") 

    if playerGuess == liarName: 
        print("Correct")
    else: 
        print("Wrong!")

players = ["Mandy", "Muskan", "Abby", "Angie", "Becky", "Simone", "Ashley"] 
liarName = assignRole(players)
assignQ(liarName, players)
guessFaker() 


