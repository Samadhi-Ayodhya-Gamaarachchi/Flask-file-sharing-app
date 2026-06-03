from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    files = os.listdir(app.config["UPLOAD_FOLDER"])
    return render_template("index.html", files=files)

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return redirect(url_for("home"))
    file = request.files["file"]
    if file.filename == "":
        return redirect(url_for("home"))
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    return redirect(url_for("home"))

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename, as_attachment=True)

@app.route("/delete/<filename>", methods=["POST"])
def delete_file(filename):
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(filename))
    if os.path.exists(filepath):
        os.remove(filepath)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)