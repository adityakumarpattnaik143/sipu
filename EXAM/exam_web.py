import os
import sys
import subprocess
from flask import Flask, render_template_string, request, jsonify
import markdown
from ansi2html import Ansi2HTMLConverter

app = Flask(__name__)

# Paths
EXAM_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(EXAM_DIR)
EXAM_MD_PATH = os.path.join(EXAM_DIR, 'exam.md')
EXAM_TASKS_PATH = os.path.join(EXAM_DIR, 'exam_tasks.py')

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Zero-Level Exam UI</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; display: flex; height: 100vh; background-color: #f4f4f9; position: relative; }
        .watermark {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            pointer-events: none;
            z-index: 9999;
            overflow: hidden;
            display: flex;
            flex-wrap: wrap;
            align-content: flex-start;
        }
        .watermark span {
            color: rgba(0, 0, 0, 0.05);
            font-size: 3rem;
            padding: 2rem;
            white-space: nowrap;
            transform: rotate(-30deg);
        }
        .panel { flex: 1; padding: 20px; overflow-y: auto; box-sizing: border-box; position: relative; z-index: 1; }
        .left-panel { border-right: 2px solid #ddd; background: #fff; }
        .right-panel { display: flex; flex-direction: column; background: #1e1e1e; color: #d4d4d4; }
        textarea { flex: 1; width: 100%; font-family: monospace; font-size: 14px; background: #2d2d2d; color: #fff; border: 1px solid #444; padding: 10px; resize: none; }
        .controls { padding: 10px 0; display: flex; justify-content: space-between; align-items: center; }
        button { padding: 10px 20px; font-size: 16px; background-color: #007bff; color: white; border: none; cursor: pointer; border-radius: 4px; }
        button:hover { background-color: #0056b3; }
        .output-box { height: 200px; background: #000; color: #ddd; font-family: monospace; padding: 10px; overflow-y: auto; border: 1px solid #444; margin-top: 10px; white-space: pre-wrap;}
        marquee { background-color: #ffeb3b; color: #000; font-weight: bold; padding: 5px; border-bottom: 1px solid #ccc; position: absolute; top: 0; left: 0; width: 100%; z-index: 2; box-sizing: border-box; }
        .panel-container { display: flex; width: 100%; height: calc(100vh - 32px); margin-top: 32px; }
    </style>
</head>
<body>
    <div class="watermark" id="watermark-container"></div>
    <marquee>IMPORTANT NOTICE: This exam is actively monitored. Do not attempt to copy or distribute these materials. Copyright ADITYA KUMAR PATTNAIK.</marquee>
    <div class="panel-container">
        <div class="panel left-panel">
            <h2>Welcome ASHIRBAD PATTNAIK , test by ADITYA</h2>
            {{ exam_html | safe }}
        </div>
    <div class="panel right-panel">
        <h3>exam_tasks.py</h3>
        <textarea id="code-editor">{{ current_code }}</textarea>
        <div class="controls">
            <button onclick="runTests()">Run Tests</button>
            <span id="status"></span>
        </div>
        <div class="output-box" id="test-output">Output will appear here...</div>
        </div>
    </div>

    <script>
        // Generate repeating watermark
        const wmContainer = document.getElementById('watermark-container');
        const wmText = "ADITYA KUMAR PATTNAIK";
        for (let i = 0; i < 100; i++) {
            const span = document.createElement('span');
            span.innerText = wmText;
            wmContainer.appendChild(span);
        }

        // Intercept copy events to inject watermark
        document.addEventListener('copy', function(e) {
            const selection = window.getSelection().toString();
            if (selection) {
                const modifiedText = selection + "\\n\\n---\\nCopied from: " + wmText + "'s Exam Platform";
                e.clipboardData.setData('text/plain', modifiedText);
                e.preventDefault();
            }
        });

        function runTests() {
            const code = document.getElementById('code-editor').value;
            const outputBox = document.getElementById('test-output');
            const statusSpan = document.getElementById('status');

            outputBox.innerText = "Running tests...";
            statusSpan.innerText = "Running...";

            fetch('/run_tests', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ code: code })
            })
            .then(response => response.json())
            .then(data => {
                outputBox.innerHTML = data.output;
                statusSpan.innerText = "Tests Completed.";
            })
            .catch(err => {
                outputBox.innerText = "Error running tests: " + err;
                statusSpan.innerText = "Error!";
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    exam_html = ""
    if os.path.exists(EXAM_MD_PATH):
        with open(EXAM_MD_PATH, 'r', encoding='utf-8') as f:
            exam_html = markdown.markdown(f.read())
    else:
        exam_html = "<p>Could not find exam.md</p>"

    current_code = ""
    if os.path.exists(EXAM_TASKS_PATH):
        with open(EXAM_TASKS_PATH, 'r', encoding='utf-8') as f:
            current_code = f.read()

    return render_template_string(HTML_TEMPLATE, exam_html=exam_html, current_code=current_code)

@app.route('/run_tests', methods=['POST'])
def run_tests():
    data = request.json
    code = data.get('code', '')

    try:
        with open(EXAM_TASKS_PATH, 'w', encoding='utf-8') as f:
            f.write(code)
    except Exception as e:
        return jsonify({"output": f"Failed to save code: {str(e)}"}), 500

    # Run pytest
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'pytest', '--color=yes', EXAM_DIR],
            capture_output=True,
            text=True,
            timeout=10
        )
        output = result.stdout
        if result.stderr:
            output += "\n" + result.stderr

        conv = Ansi2HTMLConverter(inline=True)
        html_output = conv.convert(output, full=False)
        return jsonify({"output": html_output})
    except Exception as e:
        return jsonify({"output": f"Exception while running pytest: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=False, port=5000)
