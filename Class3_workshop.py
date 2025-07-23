print ("Oh no Monster is attacked!!!")
print (">>Big Fox (100hp)<<")
print ("---choose your weapon---")
print ("1.Pen✎ = 5 dmg")
print ("2.Cat(ΦωΦ）= 50 dmg")
print ("3.Tax = 1 dmg (but rich)")

while True:
    weapon = input("choose your weapon (1,2,3)>>>: ")

    if weapon == "1":
        print ("U choose Pen✎(5dmg)")
        break
    elif weapon == "2":
        print ("U choose Cat(ΦωΦ)(50dmg)")
        
    elif weapon == "3":
        print ("U choose Tax(1dmg)")
        break
    else:
        print ("bro just choose 1,2,3")

while True:
    fight = input("U wanna fight with boss?(1,2): ")
    if fight == "1":