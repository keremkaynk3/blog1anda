import sqlite3 as sql

db = sql.connect(r"C:/Users/MR. CAPH/PycharmProjects/blogBiranda/blog.db")
cursor = db.cursor()

def add_Country(self):
    print("Eklemek istediğiniz ülkenin verilerini doğru ve eksiksiz tuşlayınız:")
    a = input("Ülke ismi:")
    b = input("Youtube Linki:")
    c = input("Başkenti:")
    d = input("Ülke Kodu")
    e = input("Ülke Nüfusu")
    f = input("Para Birimi:")
    g = input("Şehir Bilgisi:")
    h = 0
    sorgu = "INSERT INTO ulkeler(ulke_adi, linkler, baskent, kodu, nufus, para_birimi, yerler, fotolar) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(sorgu, (a, b, c, d, e, f, g, h))
    db.commit()
    print("Ülke bilgisi veritabanına eklendi...")
