print ("Oh no Monster is attacked!!!")
print (">>Big Fox (100hp)<<")

while True:
    print ("------------------------")
    print ("1.Pen✎ = 5 dmg")
    print ("2.Cat(ΦωΦ）= 50 dmg")
    print ("3.Tax = 1 dmg (but rich)")
    weapon = input("choose your weapon (1,2,3)>>>: ")

    if weapon == "1":
        print ("U choose Pen✎(5dmg)")
        break
    elif weapon == "2":
        print ("U choose Cat(ΦωΦ)(50dmg)")
        break
    elif weapon == "3":
        print ("U choose Tax(1dmg)")
        break
    else:
        print ("bro just choose 1,2,3")

while True:
    fight = input("U wanna fight with boss?(choose 1,2): ")
    if fight == "1":
        nextfight = input("How many rounds?: ")
        print ("Let's start!")
        break
    elif fight == "2":
        print ("Exist.")
        break
    else:
        print ("bro just choose 1,2")