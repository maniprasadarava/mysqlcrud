# import mysql.connector 

# mysqldb=mysql.connector.connect(host="localhost",user="root",password="")    
# mycursor=mysqldb.cursor()  
# mycursor.execute("create database student")   
# mysqldb.close()


import mysql.connector as connector
from crudoperations import create_table, insert_record,read_record,update_record,delete_record
while(1):
    print("-------------------MENU-----------------------")
    print("  1) create Table")
    print("  2) Insert Record")
    print("  3) Read Record")
    print("  4) Update Record")
    print("  5) Delete Record")
    print("  6) Exit")

    choice= int(input("Enter Your Choice: "))

    if choice==1:
        create_table()
    elif choice==2:
        insert_record()
    elif choice==3:
        read_record()
    elif choice==4:
        update_record()
    elif choice==5:
        delete_record()
    else:
        break