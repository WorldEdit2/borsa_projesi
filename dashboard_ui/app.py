from flask import Flask, render_template
import requests

app = Flask(__name__)

# Docker ağında diğer servisin adı 'market-service' olacak.
# Localhost yazamayız çünkü her konteynerin kendi localhost'u vardır.
API_URL = "http://market-service:5000/fiyatlar"

@app.route('/')
def index():
    try:
        # Arka planda diğer servise git ve veriyi al
        response = requests.get(API_URL)
        fiyatlar = response.json()
        durum = "Sistem Online"
    except:
        fiyatlar = {}
        durum = "Market Verisine Ulaşılamadı!"

    return render_template('index.html', fiyatlar=fiyatlar, durum=durum)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
