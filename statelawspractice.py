from calendar import IllegalMonthError
from multiprocessing.sharedctypes import Value
from optparse import Values
from re import M

from traitlets import Int
import copy



def make_hash(o):
    if isinstance(o, (set, tuple, list)):
        return tuple([make_hash(e) for e in o])
    elif not isinstance(o, dict):
        return hash(o)

    new_o = copy.deepcopy(o)
    for k, v in new_o.items():
        new_o[k] = make_hash(v)

        return hash(tuple(frozenset(sorted(new_o.items()))))

USAstates = ["Alabama", "Alaska", "Florida"]
USAlaws = ["abortion", "cannabis"]
abortionLaw = {
    0 : "banned",
    1 : "restricted",
    2 : "legal until viability",
    3 : "legal in all stages of pregnancy"
}

cannabisLaw = {
    0 : "illegal",
    1 : "legal for medical use",
    2 : "legal for medical and recreation use",
}

states = {tuple(
{
    "State Name": "Alabama",
    "Abortion Law": "restricted",
    "Cannabis Law": "legal for medical use",
    "Voter Leaning": "red",
}),
tuple(
{
    "State Name": "Alaska",
    "Abortion Law": "legal in all states of pregnancy",
    "Cannabis Law": "legal for medical use",
    "Voter Leaning": "red",
}),
tuple(

{
    "State Name": "Florida",
    "Abortion Law": "restricted",
    "Cannabis Law": "legal for medical use",
    "Voter Leaning": "red"
}),
}



#def whichState(text):
#    if len(text) == ""
#input("State? ")


#x = "Alabama"
#y = "Alaska"
#sharedLaws = {k: x[k] for k in x if k in y and x[k] == y[k]}
#print("There are " + str(len(sharedLaws)) + " similarities between " + str(x.keys()) + " and " + str(y.keys()))

def stateLaws(topic, results):
    rightsScore = 0
    for a, b in USAstates.items():
        rightsScore = rightsScore + b.get(results, 0)
    return rightsScore

#abortionStatus =
#cannabisStatus = states[3:4]
#stateStatus = 
user_state = input("State: ")
user_law = input("Law: ")
stateLaw1 = [states, 0, 1]

user_question = "In " + user_state + ", " + user_law + " is " + str(abortionLaw[1]) + "."
#stateStatus = states[0:49].values()
#if user_input == USAstates:
print(user_question)

#if user_law in USAlaws and user_state in USAstates:
#    print("In " + user_state + ", " + user_law + " is " + str(stateLaw1[1:1]) + ".")

if user_law == "abortion" and user_state == "Alabama":
    print("In " + user_state + ", " + user_law + " is " + str(dict(abortionLaw).get(1)) + ".") 
    exit()
elif user_law == "cannabis" or "marijuana" or "weed" and user_state == "Alabama":
    print("In " + user_state + ", " + user_law + " is " + str(dict(cannabisLaw).get(1)) + "." )
    exit()


if user_law == "abortion" and user_state == "Alaska":
    print("In " + user_state + ", " + user_law + " is " + str(dict(abortionLaw).get(3)) + ".") 
    exit()
if user_law == "cannabis" or "marijuana" or "weed" and user_state == "Alaska":
    print("In " + user_state + ", " + user_law + " is " + str(dict(cannabisLaw).get(2)) + "." )
    exit()



#print("Abortion Law")
#print("In Alabama, abortion is " + str(states["Alabama"]["Abortion Law"]) + ".")
#print("Rights Score is: " + str(sum("Alabama".values())))


