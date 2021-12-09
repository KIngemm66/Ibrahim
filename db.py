import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'danburan',
    user = 'root',
    password = ''
)

mycursor = mydb.cursor(dictionary=True)



mycursor.execute(
    """CREATE TABLE IF NOT EXISTS Plants(
        ID INT NOT NULL AUTO_INCREMENT,
        plantname VARCHAR(255),
        species VARCHAR(255),
        manufacturer VARCHAR(255),
        manufacturerlocation VARCHAR(255),
        price VARCHAR(255),
        amountremaining VARCHAR(255),
        PRIMARY KEY(ID)
    )
    """
)
