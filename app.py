from flask import Flask, render_template, jsonify
from excel_sensor_reader import get_next_vitals
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/vitals")
def api_vitals():
    data = get_next_vitals()
    return jsonify(data)

# ---------- REQUIRED FOR CLOUD ----------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

