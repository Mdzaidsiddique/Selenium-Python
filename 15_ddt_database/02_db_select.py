
import mysql.connector

try:
    con = mysql.connector.connect(host='localhost',port='3306', user='root', passwd='root', database='mydb')
    cur = con.cursor()
    cur.execute('select * from student')

    # con.commit() #commit is not required here

    for data in cur.fetchall():
        print(data[0])

    con.close()
    print("here is the records..")
except:
    print("something went wrong")