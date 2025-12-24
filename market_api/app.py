from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/fiyatlar')
def get_prices():
    # Rastgele borsa verileri simüle ediyoruz
    data = {
        "BTC": round(random.uniform(90000, 95000), 2),
        "ETH": round(random.uniform(2500, 3000), 2),
        "SOL": round(random.uniform(100, 150), 2),
        "DOGE": round(random.uniform(0.1, 0.3), 4)
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
