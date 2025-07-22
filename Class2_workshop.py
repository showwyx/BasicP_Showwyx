Distance = int(input("ระยะทาง: "))
result = 0
if Distance >= 500:
    result = 45
    print ("_______________________________________________")
    print (f"ระยะทางคือ {Distance}km ค่าส่งเท่ากับ {result} บาทนะจ้ะ")
    print ("ლ(́◉◞౪◟◉‵ლ)")
elif Distance >= 301:
    result = 35     
    print ("_______________________________________________")
    print (f"ระยะทางคือ {Distance}km ค่าส่งเท่ากับ {result} บาทนะจ้ะ")
    print ("ლ(́◉◞౪◟◉‵ლ)")
elif Distance >= 101:
    result = 25
    print ("_______________________________________________")
    print (f"ระยะทางคือ {Distance}km ค่าส่งเท่ากับ {result} บาทนะจ้ะ")
    print ("ლ(́◉◞౪◟◉‵ლ)")
elif Distance >= 51:
    result = 15
    print ("_______________________________________________")
    print (f"ระยะทางคือ {Distance}km ค่าส่งเท่ากับ {result} บาทนะจ้ะ")
    print ("ლ(́◉◞౪◟◉‵ლ)")
elif Distance >= 5:
    result = 10
    print ("_______________________________________________")
    print (f"ระยะทางคือ {Distance}km ค่าส่งเท่ากับ {result} บาทนะจ้ะ")
    print ("ლ(́◉◞౪◟◉‵ლ)")
else:
    print ("ต่ำกว่า 5km กุไม่ส่ง")

