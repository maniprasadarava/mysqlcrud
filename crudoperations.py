import mysql.connector  

def create_table():
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="Schooldb")
    mycursor=mysqldb.cursor()
    try:
        mycursor.execute("create table student(roll INT,name VARCHAR(255), marks INT)")
    except:
        print("table already Exit")  
    mysqldb.close()

def insert_record():
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="Schooldb")  
    mycursor=mysqldb.cursor()#cursor() method create a cursor object    
    try:    
        mycursor.execute("insert into student values(1,'Pawan',80),(2,'Kalyan',89),(3,'mani',90)")  
        mysqldb.commit() # Commit is used for your changes in the database  
        print('Record inserted successfully...')   
    except:     
        mysqldb.rollback()  
    mysqldb.close()

def read_record():
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="Schooldb")  
    mycursor=mysqldb.cursor() 
    try:  
        mycursor.execute("select * from student")  
        result=mycursor.fetchall()   
        for i in result:    
            roll=i[0]  
            name=i[1]  
            marks=i[2]  
            print(roll,name,marks)  
    except:   
        print('Error:Unable to fetch data.')  
    mysqldb.close()

def update_record():  
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="Schooldb") 
    mycursor=mysqldb.cursor()
    try:  
        mycursor.execute("UPDATE student SET name='Ramu', marks=100 WHERE roll=1")
        mysqldb.commit()   
        print('Record updated successfully...')   
    except:     
        mysqldb.rollback()  
    mysqldb.close()
def delete_record():
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="Schooldb") 
    mycursor=mysqldb.cursor()   
    try:   
        mycursor.execute("DELETE FROM student WHERE roll=2")   
        mysqldb.commit()  
        print('Record deteted successfully...')  
    except:    
        mysqldb.rollback()  
    mysqldb.close() 
