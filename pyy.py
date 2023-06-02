
import math 
import random
import sys 

def Have(Command, Causess, Vara):
    if Command == "Have":
        print(f"You Have Enought {Vara} for {Causes} {Vara}")

def game():
    a = input("N?")
    playtime = 0+1
    Money = 1
    HP = 100 
    Job = ["Not Job"]
    Jobs = 1
    JobsAvailable = ["Waiter","Asistent"]
    playtime = 1
    while True:
        if playtime == 1:
            print("Hello Welcome to the RPG made By Swif use Rob to Rob and make Money or Heal To Heal Work is for work and employmemt is for getting a job type commands to play-,")
            playtime += 1
            continue
        rc = input("Command To Run>")
        if rc == "Rob":
            r = random.randint(25,1001)
            ch = random.randint(1,5)
            if ch == 1:
                Money += r
                print(f"You Stole {r} DD Why did you steal")
                playtime += 1
                continue
            else:
                if ch == 2:
                    chh = random.randint(1,Money)
                    print(f"You Got Caught And Arrested You Loose {chh}")
                    if Money != 0:
                        Money -= chh 
                  
                else:
                    if ch == 3:
                        print("You did not Gain Money")
                    else:
                        if ch == 4:                           
                            print(f"You Lost 20Health")
                            HP -= 10
                        else:
                            if ch == 5:
                                print("Someone Saw You And Wants You to Employ For His Company")
        else:          
            if rc == "Heal":
                if Money >= 10:
                    if HP != 100:
                        HP = 100
                        Money -= 10
                        print("Healed")
                        playtime += 1
                        continue
                    else:
                        print("Full Health Reached")
                        playtime += 1
                        continue
            else:
                if rc == "Money":
                    print(f"{Money} Dollar")
                    playtime += 1 
                    continue
                else:
                    if rc == "Employment":
                        print(JobsAvailable)
                        print("Select")
                        t = input("Select Job>")
                        if t == "Waiter":
                            print("You Have Been Hiered")
                            Job = ["Waiter"]
                        else:
                            if t == "Asistent":
                                print("You Have Been Hiered")
                                Job = ["Asistent"] 

                    else:
                        if rc == "work":
                            if Job == ["Waiter"]:
                                print("You Worked And Gained 250$")
                                Money += 250
                                playtime += 1
                                continue
                            else:
                                if Job == ["Asistent"]:
                                    print("You Worked And Got 250$")
                                    Money += 250
                                    playtime += 1
                                    continue
                                else:
                                    if Job == ["Not Job"]:
                                        print("You Dont Have A Job Use Employment")
                                        continue
                        else:
                            if rc == "exit":
                                sys.exit
                                exit()


game()
