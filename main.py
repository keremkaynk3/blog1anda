import sqlite3 as sql
from flask import Flask, render_template, request
import addCountry
import uPdates

app = Flask(__name__)

# SQLite veritabanı bağlantısı
try:
    db = sql.connect(r"C:/Users/MR. CAPH/PycharmProjects/blogBiranda/blog.db")
    cursor = db.cursor()

    # Ana ekranda görünecek olan ülkeleri veritabanından çekiyorum.
    cursor.execute("SELECT ulke_adi, linkler, baskent, kodu, nufus, para_birimi, yerler, fotolar FROM ulkeler")
    countries = cursor.fetchall()
except sql.Error as e:
    print(f"Veritabanı hatası: {e}")
    countries = []

finally:
    if db:
        db.close()

# index.html ve country.html dosyalarımı main dosyamda çağırıyorum.
@app.route('/')
def index():
    return render_template('index.html', countries=countries)


@app.route('/visited')
def visited():
    try:
        db = sql.connect(r"C:/Users/MR. CAPH/PycharmProjects/blogBiranda/blog.db")
        cursor = db.cursor()
        cursor.execute("SELECT ulke_adi, linkler, baskent, kodu, nufus, para_birimi, yerler, fotolar FROM ulkeler")
        countries = cursor.fetchall()
    except sql.Error as e:
        print(f"Veritabanı hatası: {e}")
        countries = []
    finally:
        if db:
            db.close()

    return render_template('visited.html', countries=countries)


@app.route('/country/<int:country_id>')
def country(country_id):
    # Seçilen ülkenin bilgilerini alıyorum.
    country_info = countries[country_id - 1] if 0 < country_id <= len(countries) else None

    # Eğer ülke bulunamazsa veya veri yoksa, hata mesajı gösteriyorum.
    if not country_info:
        return "Ülke bulunamadı!"

    return render_template('country.html', country=country_info)


@app.route('/add_data', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        try:
            a = uPdates.uPdates()
            a.add_Country()
            a.add_Country()
            return "Yeni veriler başarıyla eklendi!"
        except Exception as e:
            return f"Veri ekleme sırasında hata oluştu: {e}"
    return render_template('add_data.html')


if __name__ == '__main__':
    app.run(debug=True)
