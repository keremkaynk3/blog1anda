import sqlite3 as sql

db = sql.connect(r"C:/Users/MR. CAPH/PycharmProjects/blogBiranda/blog.db")
cursor = db.cursor()


db.commit()
db.close()

print("Data inserted successfully.")

