import time
#establishing connectivity
import pymysql
food=pymysql.connect(host='localhost',user='root',password='shailesh@2003',database='hotel')
cursor=food.cursor()
#output for restaurant
def out():
    print('^'*167)
    print('^'*167)
    print()
    print(' '*75,'RESTAURANT LOGIN',' '*75)
    print()
    print('^'*167)
    print('^'*167)
    print('\n'*2)
    print('1)Admin')
    time.sleep(0.5)
    print('\n'*1)
    print('2)User')
    time.sleep(0.5)
    print('\n'*1)
    print('3)Others')
    time.sleep(0.5)
    print('\n'*2)
    print('*'*167)
    print('\n'*2)
out()
#admin details
def admin():
    print('1)Food menu')
    time.sleep(0.5)
    print('\n'*1)
    print('2)Stock')
    time.sleep(0.5)
    print('\n'*1)
    print('3)Branches')
    time.sleep(0.5)
    print('\n'*1)
    print('4)Staff info')
    time.sleep(0.5)
    print('\n'*1)
    print('5)Gross')
    time.sleep(0.5)
    print('\n'*1)
    print('6)Booking')
    time.sleep(0.5)
    print('\n'*1)
    print('7)Feedback')
    time.sleep(0.5)
    print('\n'*1)
    print('8)Exit')
#user details
def user():
    print('1)Food menu')
    time.sleep(0.5)
    print('\n'*1)
    print('2)Branches')
    time.sleep(0.5)
    print('\n'*1)
    print('3)Booking')
    time.sleep(0.5)
    print('\n'*1)
    print('4)Exit')
#other details
def other():
    print('1)Food menu')
    time.sleep(0.5)
    print('\n'*1)
    print('2)Booking')
    time.sleep(0.5)
    print('\n'*1)
    print('3)Feedback')
    time.sleep(0.5)
    print('\n'*1)
    print('4)Exit')

a=int(input('Enter your selection :'))

#outfoodmenu
def showfood():
    cursor.execute('select * from foodmenu')
    data=cursor.fetchall()
    for row in data:
        print(row)
    print('\n'*2)
    print('*'*167)
#addfoodmenu
def addfood():
    code=input('Enter Itemcode:')
    name=input('Enter Itemname:')
    quan=input('Enter Quantity:')
    price=input('Enter Price:')
    typ=input('Enter Type:')
    add="insert into foodmenu values('{}','{}','{}','{}','{}')".format(code,name,quan,price,typ)
    cursor.execute(add)
    food.commit()
    print("Values Insertion Succesful")
    print('\n'*2)
    print('*'*167)
#removefoodmenu
def remfood():
    del1=input('Enter the value of Foodcode:')
    rem="delete from foodmenu where food_code='{}'".format(del1)
    cursor.execute(rem)
    food.commit()
    print("Values Deletion Succesful")
    print('\n'*2)
    print('*'*167)
#showstock    
def showstock():
    cursor.execute('select * from stock')
    data=cursor.fetchall()
    for row in data:
        print(row)
    print('\n'*2)
    print('*'*167)
#addstock
def addstock():
    scode=input('Enter Itemcode:')
    sname=input('Enter Itemname:')
    squan=input('Enter Quantity:')
    sprice=input('Enter Price:')
    styp=input('Enter Type:')
    add="insert into stock values('{}','{}','{}','{}','{}')".format(scode,sname,squan,sprice,styp)
    cursor.execute(add)
    food.commit()
    print("Values Insertion Succesful")
    print('\n'*2)
    print('*'*167)
#remstock
def remstock():
    del1=input('Enter the value of stockcode:')
    rem="delete from stock where stock_code='{}'".format(del1)
    cursor.execute(rem)
    food.commit()
    print("Values Deletion Succesful")
    print('\n'*2)
    print('*'*167)
#showbranch
def showbranch():
    cursor.execute('select * from branches')
    data=cursor.fetchall()
    for row in data:
        print(row)
    print('\n'*2)
    print('*'*167)
#addbranch
def addbranch():
    scode=input('Enter Branchcode:')
    sname=input('Enter Branchname:')
    addr=input('Enter Address:')
    loc=input('Enter Locality:')
    tel=input('Enter Telephone:')
    web=input('Enter Website:')
    add="insert into branches values('{}','{}','{}','{}','{}','{}')".format(scode,sname,addr,loc,tel,web)
    cursor.execute(add)
    food.commit()
    print("Values Insertion Succesful")
    print('\n'*2)
    print('*'*167)
#rembranch
def rembranch():
    del1=input('Enter the value of Branchcode:')
    rem="delete from branches where branch_code='{}'".format(del1)
    cursor.execute(rem)
    food.commit()
    print("Values Deletion Succesful")
    print('\n'*2)
    print('*'*167)
#showstaff
def showstaff():
    cursor.execute('select * from staff_info')
    data=cursor.fetchall()
    for row in data:
        print(row)
    print('\n'*2)
    print('*'*167)
#addstaff
def addstaff():
    scode=input('Enter Staffid:')
    sname=input('Enter Staff Designation:')
    sal=input('Enter Salary:')
    exp=input('Enter Experience(in years):')
    qual=input('Enter Qualification:')
    add="insert into staff_info values('{}','{}','{}','{}','{}')".format(scode,sname,sal,exp,qual)
    cursor.execute(add)
    food.commit()
    print("Values Insertion Succesful")
    print('\n'*2)
    print('*'*167)
#remstaff
def remstaff():
    del1=input('Enter the value of Staffcode:')
    rem="delete from staff_info where info_id='{}'".format(del1)
    cursor.execute(rem)
    food.commit()
    print("Values Deletion Succesful")
    print('\n'*2)
    print('*'*167)
#showgross
def showgross():
    cursor.execute('select * from gross')
    data=cursor.fetchall()
    for row in data:
        print(row)
    print('\n'*2)
    print('*'*167)
#addgross
def addgross():
    scode=input('Enter Grosscode:')
    sname=input('Enter Gross Name:')
    income=input('Enter Income:')
    prof=input('Enter Profit(in %):')
    gtype=input('Enter Gross Type:')
    add="insert into gross values('{}','{}','{}','{}','{}')".format(scode,sname,income,prof,gtype)
    cursor.execute(add)
    food.commit()
    print("Values Insertion Succesful")
    print('\n'*2)
    print('*'*167)
#remgross
def remgross():
    del1=input('Enter the value of Grosscode:')
    rem="delete from gross where gross_code='{}'".format(del1)
    cursor.execute(rem)
    food.commit()
    print("Values Deletion Succesful")
    print('\n'*2)
    print('*'*167)
#showbooking
def showbooking():
    cursor.execute('select * from booking')
    data=cursor.fetchall()
    count=cursor.rowcount
    print('Total number of bookings:',count)
    for row in data:
        print(row)
    print('\n'*2)
    print('*'*167)
#addbooking
def addbooking():
    bid=input('Enter Booking Id:')
    bplace=input('Enter Preferred place:')
    bname=input('Enter Customer Name:')
    bdate=input('Enter Booking Date:')
    bpay=input('Enter Total Pay:')
    add="insert into booking values('{}','{}','{}','{}','{}')".format(bid,bplace,bname,bdate,bpay)
    cursor.execute(add)
    food.commit()
    print("Values Insertion Succesful")
    print('\n'*2)
    print('*'*167)
#rembooking
def rembooking():
    del1=input('Enter the value of Booking Id:')
    rem="delete from booking where Order_id='{}'".format(del1)
    cursor.execute(rem)
    food.commit()
    print("Values Deletion Succesful")
    print('\n'*2)
    print('*'*167)

#showfeed
def showfeed():
    cursor.execute('select * from feedback')
    data=cursor.fetchall()
    count=cursor.rowcount
    print('Total number of feedbacks:',count)
    for row in data:
        print(row)
    print('\n'*2)
    print('*'*167)
#addfeed
def addfeed():
    bid=input('Enter Feedback Id:')
    bplace=input('Enter your Name:')
    bname=input('Enter your Location:')
    bdate=input('Enter Date of visit:')
    bpay=input('Enter Dine in/ Take Out:')
    baa=input('Enter Food quality:')
    bab=input('Enter Overall Rating:')
    add="insert into feedback values('{}','{}','{}','{}','{}','{}','{}')".format(bid,bplace,bname,bdate,bpay,baa,bab)
    cursor.execute(add)
    food.commit()
    print("Values Insertion Succesful")
    print('\n'*2)
    print('*'*167)
    print("Feedback Insertion Succesful")
    print('\n'*2)
    print('*'*167)
#remfeed
def remfeed():
    del1=input('Enter the value of Name:')
    rem="delete from feedback where Name='{}'".format(del1)
    cursor.execute(rem)
    food.commit()
    print("Feedback Deletion Succesful")
    print('\n'*2)
    print('*'*167)    
def adminout1():
    print('*'*167)
    print(' '*75,'Food Menu',' '*75)
    print('\n'*2)
    print('1)Show Food Menu')
    time.sleep(0.5)
    print('\n'*1)
    print('2)Add an Item')
    time.sleep(0.5)
    print('\n'*1)
    print('3)Remove an Item')
    time.sleep(0.5)
    print('\n'*1)
    print('4)Exit')
    print('\n'*2)
    for i in range(0,100):
        food=int(input('Enter your Choice for foodmenu:'))
        if food==1:
            showfood()
        elif food==2:
            addfood()
        elif food==3:
            remfood()
        elif food==4:
            print('Thank you')
            print('\n'*2)
            print('*'*167)
            break
            
def adminout2():
    print('*'*167)
    print(' '*75,'Stock Details',' '*75)
    print('\n'*2)
    print('1)Show Stock Details')
    time.sleep(0.5)
    print('\n'*1)
    print('2)Add a Stock')
    time.sleep(0.5)
    print('\n'*1)
    print('3)Remove a Stock')
    time.sleep(0.5)
    print('\n'*1)
    print('4)Exit')
    print('\n'*2)
    for i in range(0,100):
        stock=int(input('Enter your Choice for stock:'))
        if stock==1:
            showstock()
        elif stock==2:
            addstock()
        elif stock==3:
            remstock()
        elif stock==4:
            print('Thank you')
            print('\n'*2)
            print('*'*167)
            break

def adminout3():
    print('*'*167)
    print(' '*75,'Branch Details',' '*75)
    print('\n'*2)
    print('1)Show Branch Details')
    time.sleep(0.5)
    print('\n'*1)
    print('2)Add a Branch')
    time.sleep(0.5)
    print('\n'*1)
    print('3)Remove a Branch')
    time.sleep(0.5)
    print('\n'*1)
    print('4)Exit')
    print('\n'*2)
    for i in range(0,100):
        branch=int(input('Enter your Choice for branch:'))
        if branch==1:
            showbranch()
        elif branch==2:
            addbranch()
        elif branch==3:
            rembranch()
        elif branch==4:
            print('Thank you')
            print('\n'*2)
            print('*'*167)
            break

def adminout4():
    print('*'*167)
    print(' '*75,'Staff Details',' '*75)
    print('\n'*2)
    print('1)Show Staff Details')
    time.sleep(0.5)
    print('\n'*1)
    print('2)Add an info')
    time.sleep(0.5)
    print('\n'*1)
    print('3)Remove an info')
    time.sleep(0.5)
    print('\n'*1)
    print('4)Exit')
    print('\n'*2)
    for i in range(0,100):
        staff=int(input('Enter your Choice for staff:'))
        if staff==1:
            showstaff()
        elif staff==2:
            addstaff()
        elif staff==3:
            remstaff()
        elif staff==4:
            print('Thank you')
            print('\n'*2)
            print('*'*167)
            break

def adminout5():
    print('*'*167)
    print(' '*75,'Gross Details',' '*75)
    print('\n'*2)
    print('1)Show Gross Details')
    time.sleep(0.5)
    print('\n'*1)
    print('2)Add an info')
    time.sleep(0.5)
    print('\n'*1)
    print('3)Remove an info')
    time.sleep(0.5)
    print('\n'*1)
    print('4)Exit')
    print('\n'*2)
    for i in range(0,100):
        gross=int(input('Enter your Choice for gross:'))
        if gross==1:
            showgross()
        elif gross==2:
            addgross()
        elif gross==3:
            remgross()
        elif gross==4:
            print('Thank you')
            print('\n'*2)
            print('*'*167)
            break
        
def adminout6():
    print('*'*167)
    print(' '*75,'Booking Details',' '*75)
    print('\n'*2)
    print('1)Show Booking Details')
    time.sleep(0.5)
    print('\n'*1)
    print('2)Add a Booking')
    time.sleep(0.5)
    print('\n'*1)
    print('3)Remove a Booking')
    time.sleep(0.5)
    print('\n'*1)
    print('4)Exit')
    print('\n'*2)
    for i in range(0,100):
        booking=int(input('Enter your Choice for booking:'))
        if booking==1:
            showbooking()
        elif booking==2:
            addbooking()
        elif booking==3:
            rembooking()
        elif booking==4:
            print('Thank you')
            print('\n'*2)
            print('*'*167)
            break

def adminout7():
    print('*'*167)
    print(' '*75,'Feedback Details',' '*75)
    print('\n'*2)
    print('1)Show Feedback Details')
    time.sleep(0.5)
    print('\n'*1)
    print('2)Exit')
    print('\n'*2)
    for i in range(0,100):
        feed=int(input('Enter your Choice for feedback:'))
        if feed==1:
            showfeed()
        elif feed==2:
            print('Thank you')
            print('\n'*2)
            print('*'*167)
            break

def userout1():
    print('*'*167)
    print(' '*75,'Food Menu',' '*75)
    print('\n'*2)
    print('1)Show Food Menu')
    time.sleep(0.5)
    print('\n'*1)
    print('2)Add an Item')
    time.sleep(0.5)
    print('\n'*1)
    print('3)Exit')
    print('\n'*2)
    for i in range(0,100):
        food=int(input('Enter your Choice for foodmenu:'))
        if food==1:
            showfood()
        elif food==2:
            addfood()
        elif food==3:
            print('Thank you')
            print('\n'*2)
            print('*'*167)
            break

def userout2():
    print('*'*167)
    print(' '*75,'Branch Details',' '*75)
    print('\n'*2)
    print('1)Show Branch Details')
    time.sleep(0.5)
    print('\n'*1)
    print('2)Add a Branch')
    time.sleep(0.5)
    print('\n'*1)
    print('3)Exit')
    print('\n'*2)
    for i in range(0,100):
        branch=int(input('Enter your Choice for branch:'))
        if branch==1:
            showbranch()
        elif branch==2:
            addbranch()
        elif branch==3:
            print('Thank you')
            print('\n'*2)
            print('*'*167)
            break

def userout3():
    print('*'*167)
    print(' '*75,'Booking Details',' '*75)
    print('\n'*2)
    print('1)Show Booking Details')
    time.sleep(0.5)
    print('\n'*1)
    print('2)Exit')
    print('\n'*2)
    for i in range(0,100):
        booking=int(input('Enter your Choice for booking:'))
        if booking==1:
            showbooking()
        elif booking==2:
            print('Thank you')
            print('\n'*2)
            print('*'*167)
            break

def otherout1():
    print('*'*167)
    print(' '*75,'Food Menu',' '*75)
    print('\n'*2)
    print('1)Show Food Menu')
    time.sleep(0.5)
    print('\n'*1)
    print('2)Exit')
    print('\n'*2)
    for i in range(0,100):
        food=int(input('Enter your Choice for foodmenu:'))
        if food==1:
            showfood()
        elif food==2:
            print('Thank you')
            print('\n'*2)
            print('*'*167)
            break

def otherout2():
    print('*'*167)
    print(' '*75,'Booking Details',' '*75)
    print('\n'*2)
    print('1)Show Booking Details')
    time.sleep(0.5)
    print('\n'*1)
    print('2)Add a Booking')
    time.sleep(0.5)
    print('\n'*1)
    print('3)Exit')
    print('\n'*2)
    for i in range(0,100):
        booking=int(input('Enter your Choice for booking:'))
        if booking==1:
            showbooking()
        elif booking==2:
            addbooking()
            print("Booking Confirmed")
        elif booking==3:
            print('Thank you')
            print('\n'*2)
            print('*'*167)
            break

def otherout3():
    print('*'*167)
    print(' '*75,'Feedback Details',' '*75)
    print('\n'*2)
    print('1)Show Feedback Details')
    time.sleep(0.5)
    print('\n'*1)
    print('2)Add a Feedback')
    time.sleep(0.5)
    print('\n'*1)
    print('3)Remove a Feedback')
    time.sleep(0.5)
    print('\n'*1)
    print('4)Exit')
    print('\n'*2)
    for i in range(0,100):
        feed=int(input('Enter your Choice for feedback:'))
        if feed==1:
            showfeed()
        elif feed==2:
            addfeed()
        elif feed==3:
            remfeed()
        elif feed==4:
            print('Thank you')
            print('\n'*2)
            print('*'*167)
            break
        
def out1():
    if a==1:
        b=(input('Enter the password:'))
        print('\n'*2)
        print('*'*167)
        if b=='passwd':
            for i in (0,100):
                print(' '*75,'Welcome Admin',' '*75)
                print()
                admin()
                print('\n'*2)
                c=int(input('Enter Your Choice for admin:'))
                if c==1:
                    adminout1()
                elif c==2:
                    adminout2()
                elif c==3:
                    adminout3()
                elif c==4:
                    adminout4()
                elif c==5:
                    adminout5()
                elif c==6:
                    adminout6()
                elif c==7:
                    adminout7()
                elif c==8:
                    print('Thank you')
                    print('\n'*2)
                    print('*'*167)
                    exit()

        else:
            print('Incorrect Password')
            print('Admin Rights Blocked')

def out2():
    if a==2:
        b=(input('Enter your user id:'))
        print('\n'*2)
        print('*'*167)
        print(' '*75,'Welcome User',' '*75)
        print()
        user()
        print('\n'*2)
        for i in (0,100):
            c=int(input('Enter Your Choice for user:'))
            if c==1:
                userout1()
            elif c==2:
                userout2()
            elif c==3:
                userout3()
            elif c==4:
                print('Thank you')
                print('\n'*2)
                print('*'*167)
                exit()

def out3():
    if a==3:
        b=(input('Enter your name:'))
        print('\n'*2)
        print('*'*167)
        print(' '*75,'Welcome',b,' '*75)
        print()
        other()
        print('\n'*2)
        for i in (0,100):
            c=int(input('Enter Your Choice for other user:'))
            if c==1:
                otherout1()
            elif c==2:
                otherout2()
            elif c==3:
                otherout3()
            elif c==4:
                print('Thank you')
                print('\n'*2)
                print('*'*167)
                exit()
                

for i in range(0,10):
    out1()
    out2()
    out3()
