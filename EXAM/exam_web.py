import os
import sys
import subprocess
import re
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
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; display: flex; height: 100vh; background-color: #f4f4f9; position: relative; user-select: none; -webkit-user-select: none; }
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
        textarea { flex: 1; width: 100%; font-family: monospace; font-size: 14px; background: #2d2d2d; color: #fff; border: 1px solid #444; padding: 10px; resize: vertical; min-height: 100px; margin-bottom: 5px; }
        .controls { padding: 5px 0 15px 0; display: flex; justify-content: space-between; align-items: center; }
        button { padding: 5px 15px; font-size: 14px; background-color: #007bff; color: white; border: none; cursor: pointer; border-radius: 4px; }
        button:hover { background-color: #0056b3; }
        .output-box { height: 150px; background: #000; color: #ddd; font-family: monospace; padding: 10px; overflow-y: auto; border: 1px solid #444; margin-top: 10px; white-space: pre-wrap; display: none; }
        .output-box.active { display: block; }
        .task-container { display: flex; flex-direction: column; flex: 1; min-height: 200px; margin-bottom: 20px; border-bottom: 1px solid #444; padding-bottom: 15px; }
        .task-container h4 { margin: 5px 0; }
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
        <h3>Interactive Exam Workspace</h3>

        {% for task in tasks %}
        <div class="task-container">
            <h4>{{ task.title }}</h4>
            <textarea id="code-task{{ loop.index }}">{{ task.code }}</textarea>
            <div class="controls">
                <button onclick="runTests({{ loop.index }}, '{{ task.func_name }}')">Run {{ task.title }} Tests</button>
                <span id="status-{{ loop.index }}" style="font-weight: bold; margin-left: 10px;"></span>
            </div>
            <div class="output-box" id="test-output-{{ loop.index }}"></div>
        </div>
        {% endhof %}

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

        // Intercept and prevent copy/paste/cut/contextmenu
        document.addEventListener('copy', function(e) {
            e.preventDefault();
            alert('Copying is disabled on this platform.');
        });
        document.addEventListener('cut', function(e) {
            e.preventDefault();
            alert('Cutting is disabled on this platform.');
        });
        document.addEventListener('paste', function(e) {
            e.preventDefault();
            alert('Pasting is disabled on this platform.');
        });
        document.addEventListener('contextmenu', function(e) {
            e.preventDefault();
        });

        function runTests(taskNum, keyword) {
            // Collect all task codes
            const totalTasks = {{ tasks|length }};
            const allCode = [];
            for (let i = 1; i <= totalTasks; i++) {
                const el = document.getElementById('code-task' + i);
                if (el) {
                    allCode.push(el.value);
                }
            }

            const outputBox = document.getElementById('test-output-' + taskNum);
            const statusSpan = document.getElementById('status-' + taskNum);

            outputBox.classList.add('active');
            outputBox.innerText = "Running tests for Task " + taskNum + "...";
            statusSpan.innerText = "Running...";
            statusSpan.style.color = "yellow";

            fetch('/run_tests', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    codes: allCode,
                    keyword: keyword
                })
            })
            .then(response => response.json())
            .then(data => {
                outputBox.innerHTML = data.output;
                statusSpan.innerText = "Tests Completed.";
                statusSpan.style.color = "lightgreen";
            })
            .catch(err => {
                outputBox.innerText = "Error running tests: " + err;
                statusSpan.innerText = "Error!";
                statusSpan.style.color = "red";
            });
        }
    </script>
</body>
</html>
"""

def parse_exam_tasks():
    tasks = []
    if not os.path.exists(EXAM_TASKS_PATH):
        return tasks

    with open(EXAM_TASKS_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split("def ")
    task_idx = 1
    for part in parts[1:]:
        lines = part.splitlines()
        if not lines: continue

        first_line = lines[0]
        func_name_match = re.match(r'^([a-zA-Z0-9_]+)\s*\(', first_line)
        if func_name_match:
            func_name = func_name_match.group(1)
            code_block = "def " + part.rstrip()

            tasks.append({
                "title": f"Task {task_idx}: {func_name}",
                "func_name": func_name,
                "code": code_block
            })
            task_idx += 1

    return tasks


@app.route('/')
def index():
    exam_html = ""
    if os.path.exists(EXAM_MD_PATH):
        with open(EXAM_MD_PATH, 'r', encoding='utf-8') as f:
            exam_html = markdown.markdown(f.read())
    else:
        exam_html = "<p>Could not find exam.md</p>"

    tasks = parse_exam_tasks()
    template = HTML_TEMPLATE.replace('{% endhof %}', '{% endfor %}')

    return render_template_string(template,
        exam_html=exam_html,
        tasks=tasks
    )

@app.route('/run_tests', methods=['POST'])
def run_tests():
    data = request.json
    codes = data.get('codes', [])
    keyword = data.get('keyword', '')

    combined_code = "\n\n".join(codes) + "\n"

    try:
        with open(EXAM_TASKS_PATH, 'w', encoding='utf-8') as f:
            f.write(combined_code)
    except Exception as e:
        return jsonify({"output": f"Failed to save code: {str(e)}"}), 500

    try:
        cmd = [sys.executable, '-m', 'pytest', '--color=yes', EXAM_DIR]
        if keyword:
            cmd.extend(['-k', keyword])

        result = subprocess.run(
            cmd,
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
