import sqlite3 as sql
from flask import Flask, render_template, Response
import io

app = Flask(__name__)

def get_countries():
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
    return countries

@app.route('/')
def index():
    countries = get_countries()
    return render_template('index.html', countries=countries)

@app.route('/about')
def about_me():
    countries = get_countries()
    return render_template('about.html', countries=countries)

@app.route('/ptfy')
def portfolio():
    countries = get_countries()
    return render_template('portfolio.html', countries=countries)

@app.route('/visited')
def visited():
    countries = get_countries()
    return render_template('visited.html', countries=countries)

@app.route('/country/<int:country_id>')
def country(country_id):
    countries = get_countries()
    country_info = countries[country_id - 1] if 0 < country_id <= len(countries) else None
    if not country_info:
        return "Ülke bulunamadı!"
    return render_template('country.html', country=country_info, country_id=country_id)

@app.route('/image/<int:country_id>')
def image(country_id):
    try:
        db = sql.connect(r"C:/Users/MR. CAPH/PycharmProjects/blogBiranda/blog.db")
        cursor = db.cursor()
        cursor.execute("SELECT fotolar FROM ulkeler WHERE rowid = ?", (country_id,))
        photo_blob = cursor.fetchone()[0]
        if photo_blob:
            return Response(photo_blob, mimetype='image/jpeg')
        return "Fotoğraf bulunamadı!", 404
    except sql.Error as e:
        print(f"Veritabanı hatası: {e}")
        return "Bir hata oluştu!", 500
    finally:
        if db:
            db.close()

if __name__ == '__main__':
    app.run(debug=True)
