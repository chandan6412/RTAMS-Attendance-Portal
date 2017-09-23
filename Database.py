import sqlite3


def create_user_table():
    connection = sqlite3.connect("signIn.db")
    #connection.execute("CREATE TABLE USER(USERNAME TEXT NOT NULL,EMAIL_ID TEXT,PASSWORD TEXT NOT NULL)")
    #connection.execute("INSERT INTO USER VALUES(?,?,?)",('chandan','chandan6412@gmail.com','chan'))
    #connection.commit()

    fetch = connection.execute("SELECT * FROM USER")

    for data in fetch:
        print("Username",data[0])
        print("EmailId",data[1])
        print("Password",data[2])

    connection.close()
create_user_table()