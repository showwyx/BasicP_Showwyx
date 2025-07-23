print ("Oh no Monster is attacked!!!")
print (">>Big cat (100hp)<<")
Pen = 1
Cat = 2
Tax = 3

while True:
    print ("---choose your weapon---")
    print ("1. Pen✎ = 5 dmg")
    print ("2. Cat(ΦωΦ）= 50 dmg")
    print ("3. Tax = 0 dmg (richB)")
    Weapon = input("> ")
    if (Weapon != 1 , 2 , 3):
        print ("---choose your weapon---")
        print ("Pen✎ = 5 dmg")
        print ("Cat(ΦωΦ）= 50 dmg")
        print ("Tax = 0 dmg (richB)")
        Weapon = input("> ")
    else:
        print (f"U put {Weapon}")
        print ("u wanna fight Boss?")
        print ("yes or no")
        break
yes = 0
no = 0
while True:
    answer = str(input("pick your answer: "))
    if answer != yes or answer != no:
        answer = str(input("pick your answer: "))
    else:
        break