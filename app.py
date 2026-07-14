from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    receipt = None

    if request.method == "POST":
        item = request.form["item"]
        qty = int(request.form["qty"])
        price = float(request.form["price"])

        total = qty * price

        receipt = {
            "item": item,
            "qty": qty,
            "price": price,
            "total": total,
            "date": datetime.now().strftime("%d-%m-%Y %H:%M")
        }

    return render_template("index.html", receipt=receipt)

if __name__ == "__main__":
    app.run(debug=True)