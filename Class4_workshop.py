def main():
    movie_list = [
        {'movie_name':'JaonaiVSAomsin' , 'price':990 , 'age':18},
        {'movie_name':'JaosuaJudpakjai' , 'price':20 , 'age':3},
        {'movie_name':'JaokhunRobloxDance' , 'price':10 ,'age':3},
        {'movie_name':'NiceTryDiddy' , 'price':200 , 'age':10},
        {'movie_name':'PluemAndEuro' , 'price':10 , 'age':18}
    ]

def showmovie(movie_list):
    print ("_____________________")
    i = 0
    for movie in range (movie_list):
        i += 1
        print (i,".",movie["movie_name"],"ราคา",movie["price"],"baht","แนะนำ",movie["age"],"ปี")

def buymovie(movie_list):
    print ("_____________________")
    showmovie(movie_list)

    while True:
        print("1.แสดงรายชื่อหนัง\n2.ซื้อตั๋วจ่ะ")
        menu = int(input("ต้องการเลือกmenuใด(1/2): "))
        if menu == 1:
            showmovie(movie_list)
        elif menu == 2:
            buymovie(movie_list)
            break
        else:
            print("i na hee")
            

main()