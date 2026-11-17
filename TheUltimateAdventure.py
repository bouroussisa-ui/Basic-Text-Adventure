import time
import random

items = []

print("Welcome to the Survival Adventure")

riddles = ("What has keys but no locks?", "What has a heart that doesn't beat?", "What has a head and a tail but no body?", "What has a neck but no head?", "What has a face and two hands but no arms or legs?", "What has a tongue but cannot talk?", "What has a bed but never sleeps?", "What has a ring but no finger?", "What has a thumb and four fingers but is not alive?", "What has a spine but no bones?")


def findcoin():
    if "coin" in items:
       lolcoin = input("You entered the tunnel. You can go deeper into the tunnel or go back. (Deeper/Back):") 
       while lolcoin.lower() != "deeper" and lolcoin.lower() != "back":
              lolcoin = input("You entered the tunnel. You can go deeper into the tunnel or go back. (Deeper/Back):")
       if lolcoin.lower() == "deeper":
           riddle = random.choice(riddles)
           riddlewizard = input(f"You went deeper into the tunnel and found a wizard. The wizard gives you a riddle. If you answer correctly, he will let you live. If you answer incorrectly, he will kill you. The riddle is '{riddle}' You have 10 seconds to answer. What is your answer?")
           start = time.time()
           while riddlewizard.lower() not in ["piano", "artichoke", "coin", "bottle", "clock", "shoe", "river", "telephone", "glove", "book"]:
                riddlewizard = input(f"You went deeper into the tunnel and found a wizard. The wizard gives you a riddle. If you answer correctly, he will let you live. If you answer incorrectly, he will kill you. The riddle is '{riddle}' You have 10 seconds to answer. What is your answer?")
           if riddlewizard.lower() == "piano" and riddle == "What has keys but no locks?":
                print("You answered correctly. The wizard let you live. You can now go back to the tunnel.")
                darktunnel()
           if riddlewizard.lower() == "artichoke" and riddle == "What has a heart that doesn't beat?":
                print("You answered correctly. The wizard let you live. You can now go back to the tunnel.")
                darktunnel()
           if riddlewizard.lower() == "coin" and riddle == "What has a head and a tail but no body?":
                print("You answered correctly. The wizard let you live. You can now go back to the tunnel.")
                darktunnel()
           if riddlewizard.lower() == "bottle" and riddle == "What has a neck but no head?":
                print("You answered correctly. The wizard let you live. You can now go back to the tunnel.")
                darktunnel()
           if riddlewizard.lower() == "clock" and riddle == "What has a face and two hands but no arms or legs?":
                print("You answered correctly. The wizard let you live. You can now go back to the tunnel.")
                darktunnel()
           if riddlewizard.lower() == "shoe" and riddle == "What has a tongue but cannot talk?":
                print("You answered correctly. The wizard let you live. You can now go back to the tunnel.")
                darktunnel()
           if riddlewizard.lower() == "river" and riddle == "What has a bed but never sleeps?":
                print("You answered correctly. The wizard let you live. You can now go back to the tunnel.")
                darktunnel()
           if riddlewizard.lower() == "telephone" and riddle == "What has a ring but no finger?":
                print("You answered correctly. The wizard let you live. You can now go back to the tunnel.")
                darktunnel()
           if riddlewizard.lower() == "glove" and riddle == "What has a thumb and four fingers but is not alive?":
                print("You answered correctly. The wizard let you live. You can now go back to the tunnel.")
                darktunnel()
           if riddlewizard.lower() == "book" and riddle == "What has a spine but no bones?":
                print("You answered correctly. The wizard let you live. You can now go back to the tunnel.")
                darktunnel()
           else:
               print("You answered incorrectly. The wizard killed you. Game over.")
           end = time.time()
           if end - start > 10:
                print("You took too long to answer and the wizard killed you. Game Over.")
                return
           return
       if lolcoin.lower() == "back":
           darktunnel()
           return
       findcoin()
       return
    findcoin = input("You entered the tunnel and found a coin. You can take the coin, go deeper into the tunnel or go back. (Take/Deeper/Back):")
    while findcoin.lower() != "take" and findcoin.lower() != "deeper" and findcoin.lower() != "back":
        findcoin = input("You entered the tunnel and found a coin. You can take the coin, go deeper into the tunnel or go back. (Take/Deeper/Back):")
    if findcoin.lower() == "take":
        items.append("coin")
        print("You took the coin !")
        darktunnel()
        return
    if findcoin.lower() == "deeper":
        print("You need to take the coin before going deeper.")
        findcoin()
        return
    if findcoin.lower() == "back":
        darktunnel()
        return
    findcoin()
                

def answerfindkey():
    if "key" in items:
        print("You already have the key. You can go back.")
        answerbridge()
    else:
        answerfindkey = input("You went down the well and found a key. You can either take the key or go back. (Take/Back):")
        while answerfindkey.lower() != "take" and answerfindkey.lower() != "back":
            answerfindkey = input("You went down the well and found a key. You can either take the key or go back. (Take/Back):")
        if answerfindkey.lower() == "take":
            items.append("key")
            print("You took the key !")
            answerbridge()
        if answerfindkey.lower() == "back":
            items.append("no_goblin")
            answerwell()


def answerkey():
    answerkey = input("You entered the house and found a locked door. You need a key to open the door. (Use Key/Back):")
    while answerkey.lower() != "use key" and answerkey.lower() != "back":
        answerkey = input("You entered the house and found a locked door. You need a key to open the door. (Use Key/Back):")
    if answerkey.lower() == "use key" and "key" in items:
        print("You used the key and opened the door. You found a treasure. You won the game!")
    if answerkey.lower() == "use key" and "key" not in items:
        answerno_key = input("You don't have a key. Do you want to go back and find the key? (Back):")
        if answerno_key.lower() == "back":
            answerhouse()


def answerhouse():
    answerhouse = input("You entered the village but the village is abandoned. You found a house. Do you want to enter the house or go back? (Enter/Back):")
    while answerhouse.lower() != "enter" and answerhouse.lower() != "back":
        answerhouse = input("You entered the village but the village is abandoned. You found a house. Do you want to enter the house or go back? (Enter/Back):")
    if answerhouse.lower() == "enter":
        answerkey()
    if answerhouse.lower() == "back":
        answervillage()


def answerwell():
    answerwell = input("You crossed the bridge and found a well. Do you want to enter the well or go back? (Enter/Back):")
    while answerwell.lower() != "enter" and answerwell.lower() != "back":
        answerwell = input("You crossed the bridge and found a well. Do you want to enter the well or go back? (Enter/Back):")
    if answerwell.lower() == "enter":
        answerfindkey()
    if answerwell.lower() == "back" and "key" in items:
        answerbridge()
    if answerwell.lower() == "back" and "no_goblin" in items:
        answerbridge()
    if answerwell.lower() == "back" and "coin" in items:
        print("You gave the coin to the goblin and he let you go. You can now go back to the bridge.")
        items.remove("coin")
        time.sleep(1)
        answerbridge()
    if answerwell.lower() == "back" and "key" not in items and "coin" not in items:
        print("You turned back and found a goblin. The goblin killed you. Game Over.")


def darktunnel():
    darktunnel = input("You went past the goblin and found a dark tunnel. Do you want to enter the tunnel or go back? (Enter/Back):")
    while darktunnel.lower() != "enter" and darktunnel.lower() != "back":
        darktunnel = input("You went past the goblin and found a dark tunnel. Do you want to enter the tunnel or go back? (Enter/Back):")
    if darktunnel.lower() == "enter":
        findcoin()

    if darktunnel.lower() == "back":
        answergoblin()


def answergoblin():
    start = time.time()
    answergoblin = input("You entered the cave and found a goblin. The goblin is ready to attack you. Fortunately, you have 10 seconds to run away. You can either run go past him of run away. (Past/Away):")
    while answergoblin.lower() != "past" and answergoblin.lower() != "away":
        answergoblin = input("You entered the cave and found a goblin. The goblin is ready to attack you. Fortunately, you have 10 seconds to run away. You can either run away or go past him. (Past/Away):")
    end = time.time()
    if end - start > 10:
        print("You took too long to answer and the goblin killed you. Game Over.")
        return
    if answergoblin.lower() == "past":
        darktunnel()
    if answergoblin.lower() == "away":
        answercave()


def answervillage():
    answervillage = input("You followed the river and found a village. Do you want to enter the village or go back? (Enter/Back):")
    while answervillage.lower() != "enter" and answervillage.lower() != "back":
        answervillage = input("You followed the river and found a village. Do you want to enter the village or go back? (Enter/Back):")
    if answervillage.lower() == "enter":
        answerhouse()
    if answervillage.lower() == "back":
        answerriver()


def answerbridge():
    answerbridge = input("You crossed the river and found a bridge. Do you want to cross the bridge or go back? (Cross/Back):")
    while answerbridge.lower() != "cross" and answerbridge.lower() != "back":
        answerbridge = input("You crossed the river and found a bridge. Do you want to cross the bridge or go back? (Cross/Back):")
    if answerbridge.lower() == "cross":
        answerwell()
    if answerbridge.lower() == "back":
        answerriver()


def answercave():
    answercave = input("You went right and found a cave. Do you want to enter the cave or go back? (Enter/Back):")
    while answercave.lower() != "enter" and answercave.lower() != "back":
        answercave = input("You went right and found a cave. Do you want to enter the cave or go back? (Enter/Back):")
    if answercave.lower() == "enter":
        answergoblin()
    if answercave.lower() == "back":
        question1()
        

def answerriver():
    answerriver = input("You went left and found a river. You can either cross the river or follow it. (Cross/Follow):")
    while answerriver.lower() != "cross" and answerriver.lower() != "follow":
        answerriver = input("You went left and found a river. You can either cross the river or follow it. (Cross/Follow):")
    if answerriver.lower() == "cross":
        answerbridge()
    if answerriver.lower() == "follow":
        answervillage()


def question1():
    question1 = input("You are in a forest and you see a path. Do you want to go left or right? (Left/Right):")
    while question1.lower() != "left" and question1.lower() != "right":
        question1 = input("You are in a forest and you see a path. Do you want to go left or right? (Left/Right):")
    if question1.lower() == "left":
        answerriver()
    if question1.lower() == "right":
        answercave()


def start_adventure():
        start = input("Do you want to get in the adventure? (Yes/No):")
        while start.lower() != "yes" and start.lower() != "no":
            start = input("Do you want to get in the adventure? (Yes/No):")
        if start.lower() == "no":
            print("Ok see you next time !")
            return
        if start.lower() == "yes":
            print("Ok lets go !")
            print("Loading...")
            time.sleep(2)
            question1()



#Let's start the adventure
start_adventure()
