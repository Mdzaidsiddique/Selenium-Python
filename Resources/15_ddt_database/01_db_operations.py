# mySQL database connector
# selenium is ment for automating web not ment for database testing, thease are data driven testing not database testig
# we can perform crud operation using selenium python

# install mySQL connector for python # mysql-connector-python # select, insert, update, delete

# insert, update, delete : these command will not return anything

import mysql.connector

insert_query = "INSERT INTO student (sid, sname) VALUES (5, 'zaid'),(6, 'alif');"
update_query = "UPDATE student SET sname = 'zaid alif' WHERE sid = 6"
delete_query = "DELETE FROM student WHERE sid = 6"

# stablised a connection to database

try:
    con = mysql.connector.connect(host='localhost',port='3306', user='root', passwd='root', database='mydb')

    curs = con.cursor()  # create cursor
    # curs.execute(insert_query) #execure queary through cursor
    # curs.execute(update_query)
    curs.execute(delete_query)
    con.commit()  # commit transection
    con.close()  # close connection
    print("done")
except:
    print("connection unsuccessful")



