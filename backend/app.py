# backend/app.py

from flask import Flask, request, jsonify, send_from_directory
from parser_utils import calculate_match_score
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

app = Flask(__name__, static_folder=BASE_DIR, template_folder=BASE_DIR)

@app.route("/")
def index():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/api/match", methods=["POST"])
def analyze():
    resume_text = request.form.get("resume", "")
    job_description = request.form.get("job_description", "")

    if not resume_text or not job_description:
        return jsonify({"error": "Please provide both resume and job description."}), 400

    score, missing = calculate_match_score(resume_text, job_description)
    return jsonify({"match_percentage": score, "missing_keywords": missing})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

