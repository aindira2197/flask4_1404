from flask import Flask, render_template

app = Flask(__name__)

payments = [
    {"client": "Akbar Toshmatov",  "amount": 500000,  "paid": True,  "method": "Karta"},
    {"client": "Barno Yusupova",   "amount": 1200000, "paid": False, "method": "Naqd"},
    {"client": "Jasur Qodirov",    "amount": 750000,  "paid": True,  "method": "Karta"},
    {"client": "Dilnoza Xasanova", "amount": 300000,  "paid": False, "method": "Karta"},
    {"client": "Eldor Mirzayev",   "amount": 950000,  "paid": True,  "method": "Naqd"},
]

@app.route('/payments')
def payments_page():
    jami_tolangan = sum(p["amount"] for p in payments if p["paid"])
    jami_qarz = sum(p["amount"] for p in payments if not p["paid"])

    return render_template(
        'payments.html',
        payments=payments,
        jami_tolangan=jami_tolangan,
        jami_qarz=jami_qarz
    )

if __name__ == "__main__":
    app.run(debug=True)
