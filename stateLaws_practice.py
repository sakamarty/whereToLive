#Abortion laws: 0-bans all abortions,1-restricts abortions,2-proctects the right to abortion until viability,3-protects the right to abortionthough all stages of pregnancy
#Cannabis: 0-illegal,1-medical legal,2-recreational legal
#Voters: 0-red,1-neutral,2-blue

stateData = {"Alabama" : {"Abortion Law" : 1,"Cannabis Law" : 1, "Voter Leaning" : 0},
    "Alaska" : {"Abortion Law" : 3,"Cannabis Law" : 2, "Voter Leaning" : 0}}

def stateLaws(topic, result):
    rightsScore = 0
    for k, v in topic.items():
        rightsScore= rightsScore + v.get(result, 0)
    return rightsScore

print("Rights Score")
print(str(stateLaws(stateData,"Abortion Law")))



Alabama = {"Abortion Law": 1, "Cannabis Law": 1, "Voter Leaning":0,}
Alaska = {"Abortion Law": 3, "Cannabis Law": 2, "Voter Leaning": 0,}

def stateLaws(topic,result):
    rightsScore = 0
    for k, v in topic.items():
        rightsScore= rightsScore + v.get(result, 0)
    return rightsScore

print("Rights Score")
print((stateLaws(Alabama, "Abortion Law")))



def abortionLaw(value, laws): 
    restriction = 0
    for k, v in abortionLaws.items():
        restriction = restriction + v.get(value, 0)
    return restriction




USAstates = {
    "Alabama": {"Abortion Law": 1, "Cannabis Law": 1, "Voter Leaning":0},
    "Alaska": {"Abortion Law": 3, "Cannabis Law": 2, "Voter Leaning":0},
}



abortionLaws = {
    0 : "banned",
    1 : "restricted",
    2 : "allowed until viability",
    3 : "allowed in all stages of pregnancy",
}

cannabisLaws = {
    0: "illegal",
    1: "legal when medical",
    2: "legal for recreational and medical purposes"
}

str(states["Alabama" and "Alaska" and "Florida"]["Abortion Law" and "Cannabis Law" or "Voter Leaning"])


key = list(states.keys())

alabamaValues = {}

for s in states:
    if s["Abortion Law"] > 2:
        alabamaValues[s["Abortion Law"]] = s["Cannabis Law"]
        print("Alabama " + s["Abortion Law"] + " END.")
    
print(alabamaValues)


key = frozenset(states.items())
value = list(states.values())
key = key[0]
value = value[0]
states[key] = True

alabamaValues = {}

for s in states:
    if s["Cannabis Law"] > 2:
        alabamaValues[s["Abortion Law"]] = s["Cannabis Law"]
        print("Alabama " + s["Abortion Law"] + " END.")
    
print(alabamaValues)


def infoRequest():
    if user_state in USAstates and user_law in USAlaws:
        if dict(states).values(states) == str(user_state) and dict(states).keys() == True:
            print(user_question)

infoRequest()