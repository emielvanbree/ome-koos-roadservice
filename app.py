
from flask import Flask, request, render_template, jsonify, send_from_directory
import os, json
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/rentals", methods=["POST"])
def rentals():
    data = request.json
    with open("data/rentals.json", "a") as f:
        f.write(json.dumps(data) + "\n")
    return jsonify({"status": "success", "message": "Aanvraag ontvangen!"})

@app.route("/api/crew", methods=["POST"])
def crew():
    data = request.json
    with open("data/crew.json", "a") as f:
        f.write(json.dumps(data) + "\n")
    return jsonify({"status": "success", "message": "Beschikbaarheid geregistreerd."})

@app.route("/api/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return jsonify({"status": "success", "message": "Upload gelukt!"})
    return jsonify({"status": "error", "message": "Geen bestand ontvangen."})

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
