import random
list = ["scicor", "rock", "paper"]
human_c = 0
pc_c= 0

def win():
    print("human won!!!")

def lose():
    print("human lost!!!")

def tie():
    print("nobody won, play again")

def human():
    human = input("Choose between scicors, rock and paper: ")
    return human

def pc_choice():
    pc = random.choice(list)
    return pc
def human_count():
    global human_c
    human_c += 1
def pc_count():
    global pc_c
    pc_c += 1
def decision(h, p):
    if h == "scicor" and p == "scicor":
        print("tie")
    elif h == "scicor" and p == "rock":
        print("pc win´s")
        pc_count()
    elif h == "scicor" and p == "paper":
        print("human wins")
        human_count()
    elif h == "rock" and p == "rock":
        print("tie")
    elif h == "rock" and p == "scicor":
        print("human win´s")
        human_count()
    elif h == "rock" and p == "paper":
        print("pc win´s")
        pc_count()
    elif h == "paper" and p == "scicor":
        print("pc win´s")
        pc_count()
    elif h == "paper" and p == "rock":
        print("human win´s")
        human_count()
    elif h == "paper" and p == "paper":
        print("tie")

    
def play():
   h_dec = human()
   p_dec = pc_choice()
   decision(h_dec, p_dec)
    
        


while True:
    print("Choose, what you wanna do")
    print("1 Play")
    print("2 End Game")
    print("3 Scoreboard")
    i = input()
    if i == "1" :
        play()
    elif i == "2":
        print("Game beenden")
        break
    elif i == "3":
        print(f"Das ist Simon Anzahl:{human_c}")
        print(f"Das ist PC´s Anzahl:{pc_c}")

        