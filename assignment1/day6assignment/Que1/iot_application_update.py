import mysql.connector as myc
from datetime import datetime
connection= myc.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_application",
    use_pure=True
)

id=int(input("Enter id whose temperature to be updated :"))
temperture=int(input("Enter new Temperature: "))

query=f"UPDATE iot_application  SET temperature={temperture} WHERE id={id};"

cursor = connection.cursor()


cursor.execute(query)

connection.commit()

cursor.close()

connection.close()