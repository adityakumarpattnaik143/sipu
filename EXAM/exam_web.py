import os
import sys
import subprocess
import re
from flask import Flask, render_template, request, jsonify
import markdown
from ansi2html import Ansi2HTMLConverter

app = Flask(__name__)

# Paths
EXAM_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(EXAM_DIR)
EXAM_MD_PATH = os.path.join(EXAM_DIR, 'exam.md')
EXAM_TASKS_PATH = os.path.join(EXAM_DIR, 'exam_tasks.py')


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
    return render_template('exam_web.html',
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
            output = "".join([output, "\n", result.stderr])

        conv = Ansi2HTMLConverter(inline=True)
        html_output = conv.convert(output, full=False)
        return jsonify({"output": html_output})
    except Exception as e:
        return jsonify({"output": f"Exception while running pytest: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=False, port=5000)
