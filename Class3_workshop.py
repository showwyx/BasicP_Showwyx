print ("-----------------------------------------")
print ("Oh No Monster is attacked!!!")
print (">>>>Big Fox (100hp)<<<<")
print ("-----------------------------------------")
print ("Legendary Weapon Has Spawn")
print ("Pen✎")
print ("Cat(ΦωΦ)")
print ("Tax")
print ("-----------------------------------------")
while True:
    fight = input("U wanna fight boss? (yep select 1/no select 2): ")
    if fight == "1":
        fight = True
        nextfight = int(input("How many rounds?: "))
        if nextfight == 0:
            print ("bro r u kidding me?")
        else:
            print ("-----------------------------------------")
            print ("Let's start!")
            break
    elif fight == "2":
        fight = False
        print ("Exist.")
        break
    else:
        print ("bro just choose 1,2")

if fight == True:
    health = 100
    for i in range (nextfight):
        if health == 0:
            print("-----------------------------------------")
            print ("!!!Big Fox is died!!!")
            print ("💋💋You defeated Big Fox💋💋")
            print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
            break
        elif health < 0:
            print ("Oh No Boss Is Awake")
            health += 20
        print("-----------------------------------------")
        print(f"Round {i + 1}")
        print(f"Big Fox ({health}) hp")
        print("-----------------------------------------")
        print("1. Pen✎ = 5 dmg")
        print("2. Cat(ΦωΦ）= 50 dmg")
        print("3. Tax = 1 dmg (but rich)")

        while True:
            weapon = input("choose your weapon (1,2,3)>>>: ")
            if weapon == "1":
                print("U choose Pen✎ (5 dmg)")
                health -= 5
                break
            elif weapon == "2":
                print("U choose Cat(ΦωΦ) (50 dmg)")
                health -= 50
                break
            elif weapon == "3":
                print("U choose Tax (1 dmg)")
                health -= 1
                break
            else:
                print("bro just choose 1,2,3")
    else:
        print("-----------------------------------------")
        print ("your round is end.")
        print (f"Big Fox = ({health}) hp")
        print ("GAME OVER TT")