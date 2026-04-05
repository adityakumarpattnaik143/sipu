from flask import Flask, render_template, request, jsonify
import markdown
import subprocess
import os

app = Flask(__name__)

EXAM_DIR = "EXAM"
EXAM_MD_PATH = os.path.join(EXAM_DIR, "exam.md")
EXAM_TASKS_PATH = os.path.join(EXAM_DIR, "exam_tasks.py")

@app.route("/")
def index():
    # Read and render exam questions
    try:
        with open(EXAM_MD_PATH, "r") as f:
            md_content = f.read()
        html_questions = markdown.markdown(md_content)
    except FileNotFoundError:
        html_questions = "<p>Error: exam.md not found.</p>"

    # Read current exam tasks code
    try:
        with open(EXAM_TASKS_PATH, "r") as f:
            code_content = f.read()
    except FileNotFoundError:
        code_content = "# Error: exam_tasks.py not found."

    return render_template("index.html", questions=html_questions, code=code_content)

@app.route("/run_tests", methods=["POST"])
def run_tests():
    data = request.get_json()
    if not data or "code" not in data:
        return jsonify({"error": "No code provided"}), 400

    code = data["code"]

    # Save code to exam_tasks.py
    try:
        with open(EXAM_TASKS_PATH, "w") as f:
            f.write(code)
    except Exception as e:
        return jsonify({"error": f"Failed to save code: {str(e)}"}), 500

    # Run pytest
    try:
        result = subprocess.run(
            ["python3", "-m", "pytest", "EXAM/test_exam_tasks.py", "-v"],
            capture_output=True,
            text=True
        )
        return jsonify({
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        })
    except Exception as e:
        return jsonify({"error": f"Failed to run tests: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
