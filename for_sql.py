import mysql.connector as mysql

db = mysql.connect(
        host = "localhost",
        user = "root",
        passwd = "Arsen121",
        database = "pordz2"
    )
cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS example1(photo1 LONGBLOB, number_all VARCHAR(255), name VARCHAR(255), name1 VARCHAR(255), price VARCHAR(255))")
def upload(data):
        db = mysql.connect(
        host = "localhost",
        user = "root",
        passwd = "Arsen121",
        database = "pordz2"
    )
        cur = db.cursor()
        values = list(data.values())
        cur.execute(f"""
            INSERT INTO example1(photo1, number_all, name, name1, price)
            VALUES ('{data['photo1']}','{data['number_all']}','{data['name']}','{data['name1']}','{values[-1]}')
            """)
        db.commit()
        cur.close()
        db.close()

