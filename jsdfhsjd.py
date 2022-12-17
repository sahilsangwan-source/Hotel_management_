print('''                              ||      W E L C O M E    T O  ||
                              ||         NNM CINEMAS        ||''')
      
name=input("enter your name:")     
movies=["inception","Inception","Wolfstreet","wolfstreet","Pushpaa","pushpaa","Bhrahmastra","bhrahmastra","Gravity","gravity","Sitaraman","sitaraman"]
total=0
print("""||||||MOVIES SCREENING THIS WEEK|||||
------------
| Inception  |
------------
| Wolfstreet | 
------------
| Pushpaa    |
------------
| Bhrahmastra|
------------
| Gravity    |
------------
| Sitaraman  |
------------""")
while True:
    towatch=input("Enter the movie you want to watch:")
    if towatch in movies:
        print(""" |    2D    |    
     |    3D    |""")
        while True:
            dimension=input("enter the dimensions you prefer: ")
            if dimension=="3d" or dimension=="3D":
                print(""" 
     |  10:00am  |  11:30am  |
     |  1:30pm   |  3:00pm   |
     |  4:30pm   |  7:00pm   |
     |  9:00pm   |  11:30pm  |""")
                total+=300
            elif dimension=="2d" or dimension=="2D":
                print(""" 
     |  10:00am  |  11:30am  |
     |  1:30pm   |  3:00pm   |
     |  4:30pm   |  7:00pm   |
     |  9:00pm   |  11:30pm  |""")
                total+=0
            while True:
                time=input("select your preferred show timing:")
                t=["10:00am","11:30am","1:30pm","3:00pm","4:30pm","7:00pm","9:00pm","11:30pm"]
                if time in t:
                    while True:
                            seatno=int(input("number of required seats:"))
                            seats=["25A","26A",'27A',"28A","29A","30A","31B","32B","33B","34B"]
                            if seatno<=10:
                                print("""                <<<<   DIAMOND   >>>> Rs.450
                <<<<   GOLDEN   >>>> Rs.280
                <<<<   SILVER   >>>> Rs.180""")
                                while True :
                                    seat=input("choose your seat type:")
                                    seattype=['diamond',"DIAMOND",'golden',"GOLDEN ","silver","SILVER"]
                                    if seat==seattype[0] or seat==seattype[1]:
                                        total+=seatno*450
                                    if seat==seattype[2] or seat==seattype[3]:
                                        total+=seatno*280
                                    if seat==seattype[4] or seat==seattype[5]:
                                        total+=seatno*180
                                    print("to confirm your booking press C:")
                                    confirm=input()
                                    else:
                                        print("please enter valid input!")
                                        continue
                            else:
                                print("sorry! max 10 seats can be booked. try again!")
                                continue
                else:
                    print("invalid time")
                    continue
            else:
                print("invalid dimension! try again")
                continue
    else:
        print("invalid movie name!")
        continue
import datetime
x = datetime.datetime.now()
if confirm=="C" or confirm=="c":
        print("""               NNM CINEMAS          """)
        print(x)
        print(towatch,"show on",x.strftime("%x"),"has been booked for",name)
        print("at:" ,time)
        print(seat)
        for i in range(1,seatno+1):
            seatsno=seats[i]
            sn=print(seatsno,end=",")
        print('(',dimension,')')
        print("Total amount to be paid",total,"(INR)")
else:
    print("data not confirmed! try again")