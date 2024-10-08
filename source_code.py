import re
import random
#CREATING DATABASE
import mysql.connector

def del_book(mycursor, mydb):
    bookid1=input("ENTER BOOKID OF THE BOOK TO DELETED : ")
    str1 = "DELETE FROM book WHERE bookid = %s"
    bi=(bookid1,)
    mycursor.execute(str1, bi)
    mydb.commit()
    str0="SELECT * FROM BOOK"
    mycursor.execute(str0)
    d=mycursor.fetchall()
    for k in d:
        print(k)

def add_book(mycursor, mydb):
    print("ALL INFORMATION IS MANDATORY TO FILL")
    #CREATING A BOOKID
    bi1=random.choice('0123456789')
    bi2=random.choice('0123456789')
    bi3=random.choice('0123456789')
    bi4=random.choice('0123456789')
    bookid="B"+str(bi1)+str(bi2)+str(bi3)+str(bi4)
    bookname=input("ENTER BOOK NAME : ")
    author=input("ENTER AUTHOR NAME : ")
    publisher=input("ENTER PUBLISHER NAME : ")
    catagory=input("ENTER CATAGORY : ")
    tc=input("TOTAL NUMBER OF COPIES : ")
    ic=0
    sql = "INSERT INTO BOOK(BOOKID, BOOKNAME , BOOKAUTHOR , PUBLISHER , CATAGORY , TOTAL_COPIES ,COPIES_OF_ISSUE ) VALUES (%s,%s,%s,%s,%s,%s,%s)"

    mycursor.execute(sql, [bookid,bookname,author,publisher,catagory,tc,ic])
    str0="SELECT * FROM BOOK"
    mycursor.execute(str0)
    d=mycursor.fetchall()
    for k in d:
        print(k)

def add_user(mycursor, mydb):
    print("ALL INFORMATION IS MANDATORY TO FILL")
    #CREATING A USERID
    ui1=random.choice('0123456789')
    ui2=random.choice('0123456789')
    ui3=random.choice('0123456789')
    ui4=random.choice('0123456789')
    userid="U"+str(ui1)+str(ui2)+str(ui3)+str(ui4)
    userpass=input("ENTER PASSWORD: ")
    username=input("ENTER USER NAME: ")
    address=input("ENTER ENTER USER ADDRESS : ")
    phno=input("ENTER CONTACT NUMBER : ")
    print("YOUR USERID IS:", userid)
    sql = "INSERT INTO USERS(USERID, PASSWORD , NAME , ADDRESS , CONTACT_NUMBER  ) VALUES (%s,%s,%s,%s,%s)"
    mycursor.execute(sql, [userid,userpass,username,address,phno])
##    str0="SELECT * FROM USERS"
##    mycursor.execute(str0)
##    d=mycursor.fetchall()
##    for k in d:
##        print(k)

def del_user(mycursor, mydb):
    userid1=input("ENTER USERID OF THE USER TO DELETED : ")
    str1 = "DELETE FROM USERS WHERE USERID = %s"
    ui=(userid1,)
    mycursor.execute(str1, ui)
    mydb.commit()
##    str0="SELECT * FROM USERS"
##    mycursor.execute(str0)
##    d=mycursor.fetchall()
##    for k in d:
##        print(k)

    
def issue_book(mycursor, mydb):
    print("ALL INFORMATION IS MANDATORY TO FILL")
    #CREATING TRANSACTION ID
    ti1=random.choice('0123456789')
    ti2=random.choice('0123456789')
    ti3=random.choice('0123456789')
    ti4=random.choice('0123456789')
    tranid="T"+str(ti1)+str(ti2)+str(ti3)+str(ti4)
    print("TRANSACTION ID:",tranid)
    userid=input("ENTER USERID: ")
    bookid=input("ENTER BOOKID: ")
    #DATE OF ISSUE AND RETURN
    from datetime import date, timedelta
    current_date = date.today()
    days_after = (date.today()+timedelta(days=14))
    dateof_issue=current_date
    dateof_return=days_after
    print("DATE OF ISSUE(YYYY-MM-DD):",date.today())
    print("DATE OF RETURN(YYYY-MM-DD):",(date.today()+timedelta(days=14)))
    print ("YOU CAN ISSUE A BOOK FOR ONLY 14 DAYS IF YOU KEEP IT MORE THAN THAT YOU WILL BE FINED")
    sql = "INSERT INTO TRANSACTIONS(TRANSACTIONID , USERID , BOOKID , DATE_OF_ISSUE , DATE_OF_RETURN) VALUES (%s,%s,%s,%s,%s)"
    mycursor.execute(sql, [tranid,userid,bookid,dateof_issue,dateof_return])
##    str0="SELECT * FROM TRANSACTIONS"
##    mycursor.execute(str0)
##    d=mycursor.fetchall()
##    
##    for k in d:
##        print(k)
        
    # query to update the copies_of_issue
    query_to_update_copies_of_issue = "UPDATE BOOK SET COPIES_OF_ISSUE = COPIES_OF_ISSUE + 1 WHERE BOOKID=%s"
    mycursor.execute(query_to_update_copies_of_issue, [bookid])

def return_book(mycursor, mydb):
    print("ALL INFORMATION IS MANDATORY TO FILL")
    userid=input("ENTER USERID: ")
    bookid=input("ENTER BOOKID: ")
    tranid=input("ENTER TRANSACTION ID:")
    str4 = "SELECT DATE_OF_RETURN FROM TRANSACTIONS WHERE TRANSACTIONID = %s"
    ti=(tranid,)
    mycursor.execute(str4, ti)
    d=mycursor.fetchall()
    for k in d:
        date_entry=k
        h=str(date_entry)
        print(k)
    from datetime import date, timedelta
    import datetime
    current_date = date.today()
    try:
        year, month, day = h.split(",")[0][-4:], h.split(",")[1][-1], h.split(",")[2][-2]
        str1 = "DELETE FROM TRANSACTIONS WHERE TRANSACTIONID = %s"
        ti=(tranid,)
        mycursor.execute(str1, ti)
        print("THANKS FOR ISSUEING BOOK DO COME AGAIN")
        mydb.commit()
##        str0="SELECT * FROM USERS"
##        mycursor.execute(str0)
##        l=mycursor.fetchall()
##        for po in l:
##            print(po)
        query_to_update_copies_of_issue = "UPDATE BOOK SET COPIES_OF_ISSUE = COPIES_OF_ISSUE - 1 WHERE BOOKID=%s"
        mycursor.execute(query_to_update_copies_of_issue, [bookid])
    except:
        print("inside the except block")
    
    
def find_by_name(mycursor, mydb):
    bookn=input("ENTER NAME OF THE BOOK : ")
    str1 = "SELECT * FROM BOOK WHERE BOOKNAME = %s"
    bi=(bookn,)
    mycursor.execute(str1, bi)
    d=mycursor.fetchall()
    for k in d:
        print(k)

def find_by_author(mycursor, mydb):
    booka=input("ENTER AUTHOR OF THE BOOK : ")
    str1 = "SELECT * FROM BOOK WHERE BOOKAUTHOR = %s"
    bi=(booka,)
    mycursor.execute(str1, bi)
    d=mycursor.fetchall()
    for k in d:
        print(k)

def find_by_publisher(mycursor, mydb):
    bookp=input("ENTER PUBLISHER OF THE BOOK : ")
    str1 = "SELECT * FROM BOOK WHERE PUBLISHER = %s"
    bi=(bookp,)
    mycursor.execute(str1, bi)
    d=mycursor.fetchall()
    for k in d:
        print(k)
    

# operation method perfrom the db operations
def operations(ch1, mycursor, mydb):
    #PROCEDURE FOR MANAGEING BOOK DETAILS
    if ch1==1:
        print(" PLEASE READ CAREFULLY SINCE THE CHOICES ARE CHANGED!!!")
        print("1-ADD A BOOK")
        print("2-DELETE A BOOK")
        ch2=int(input("ENTER YOUR CHOICE :"))
    
        #PROCEDURE ADDING BOOK DETAILS
        if ch2==1:
            add_book(mycursor, mydb)
                
        #PROCEDURE DELETING BOOK DETAILS
        if ch2==2:
            del_book(mycursor, mydb)


    #PROCEDURE FOR MANAGEING USER DETAILS
    elif ch1==2:
        print(" PLEASE READ CAREFULLY SINCE THE CHOICES ARE CHANGED!!!")
        print("1-ADD A USER")
        print("2-DELETE A USER")
        ch3=int(input("ENTER YOUR CHOICE :"))

        #PROCEDURE ADDING USER DETAILS
        if ch3==1:
            add_user(mycursor, mydb)
        #PROCEDURE DELETING USER DETAILS
        if ch3==2:
            del_user(mycursor, mydb)
            

    #PROCEDURE FOR MANAGEING BOOK TRANSACTIONS
    elif ch1==3:
        print(" PLEASE READ CAREFULLY SINCE THE CHOICES ARE CHANGED!!!")
        print("1-ISSUE A BOOK")
        print("2-RETURNING A BOOK")
        ch4=int(input("ENTER YOUR CHOICE :"))
        #PROCEDURE FOR ISSUING A BOOK
        if ch4==1:
            issue_book(mycursor, mydb)
            
        #PROCEDURE FOR RETURNING A BOOK
        if ch4==2:
            return_book(mycursor, mydb)
                    
    #PROCEDURE FOR SEARCHING BOOK 
    elif ch1==4:
        print(" PLEASE READ CAREFULLY SINCE THE CHOICES ARE CHANGED!!!")
        print("1-SEARCH BOOK BY NAME")
        print("2-SEARCH BOOK BY AUTHOR")
        print("3-SEARCH BOOK BY PUBLISHER")
        ch5=int(input("ENTER YOUR CHOICE :"))
        
        if ch5==1:
            find_by_name(mycursor, mydb)
        if ch5==2:
            find_by_author(mycursor, mydb)     
        if ch5==3:
           find_by_publisher(mycursor, mydb)
        else:
            print("wrong input")
       
    elif ch1==5:
        mydb.commit()
        import sys
        sys.exit()
        
        


# main method -> you need not to call main method interpreter will call it by itself 
if __name__ == "__main__":
    
    #SOURCE CODE FOR LIBRARY MANAGEMENT:
    print("WELCOME TO LIBRARY")
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234')
    if mydb.is_connected:
        print('SUCCESFULLY CONNECTED TO DATABASE')
    else:
        print('ERROR IN CONNECTING TO DATABASE')

    #CREATE CURSOR OBJECT USING CONNECTION OBJECT
    mycursor=mydb.cursor()
    mycursor.execute("create database if not exists LIBRARY_DATABASE")
    mycursor.execute("use LIBRARY_DATABASE")
    mycursor.execute("create table if not exists BOOK(BOOKID char(5) primary key, BOOKNAME varchar(40), BOOKAUTHOR varchar(30), PUBLISHER varchar(50), CATAGORY varchar(20), TOTAL_COPIES int(3),COPIES_OF_ISSUE int(3))")
    mycursor.execute("create table if not exists USERS(USERID char(5) primary key,PASSWORD varchar(123),NAME varchar(30),ADDRESS varchar(200),CONTACT_NUMBER numeric(10))")
    mycursor.execute("create table if not exists TRANSACTIONS(TRANSACTIONID  char(5) primary key,USERID char(5), BOOKID char(5), DATE_OF_ISSUE  date, DATE_OF_RETURN date, foreign key(BOOKID) references BOOK(BOOKID),foreign key(USERID) references USERS(USERID))")
    mydb.commit()


##    mycursor.execute("desc BOOK")
##    for i in mycursor:
##        print(i)
##    mycursor.execute("desc USERS")
##    for i in mycursor:
##        print(i)
##    mycursor.execute("desc TRANSACTIONS")
##    for i in mycursor:
##        print(i)

    while(True):
        print("1-MANAGE BOOKS")
        print("2-MANAGE USERS")
        print("3-BOOK TRANSACTION")
        print("4-SEARCH A BOOK")
        print("5-EXIT")
        ch1=int(input("ENTER YOUR CHOICE :"))
        operations(ch1, mycursor, mydb)
