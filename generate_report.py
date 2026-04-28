import os
import subprocess
import json
import random
from fpdf import FPDF
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(e.stderr)
        return ""

def get_git_changes():
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    # Get files added
    added_files_output = run_command(f'git log --since="{yesterday}" --name-status --pretty=format: | grep "^A" | cut -f2')
    added_files = [f for f in added_files_output.split("\n") if f] if added_files_output else []

    # Get files modified
    changed_files_output = run_command(f'git log --since="{yesterday}" --name-status --pretty=format: | grep "^M" | cut -f2')
    changed_files = [f for f in changed_files_output.split("\n") if f] if changed_files_output else []

    # Deduplicate
    added_files = list(set(added_files))
    changed_files = list(set(changed_files))

    return added_files, changed_files

def get_test_scores():
    # Run pytest and generate json report
    run_command("pytest --json-report --json-report-file=report.json")
    try:
        with open("report.json", "r") as f:
            report = json.load(f)
            summary = report.get("summary", {})
            passed = summary.get("passed", 0)
            failed = summary.get("failed", 0)
            total = summary.get("total", 0)
            return passed, failed, total
    except Exception as e:
        print(f"Error reading test report: {e}")
        return 0, 0, 0

def create_pie_chart(passed, failed, total):
    labels = ['Passed', 'Failed']
    sizes = [passed, failed]
    colors = ['#4CAF50', '#F44336'] # Green for pass, Red for fail
    explode = (0.1, 0)  # explode 1st slice

    plt.figure(figsize=(6,6))
    if total == 0:
        plt.pie([1], labels=['No Tests'], colors=['gray'])
    else:
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Test Results')
    plt.savefig('pie_chart.png')
    plt.close()

def generate_pdf(added_files, changed_files, passed, failed, total):
    quotes = [
        "Believe you can and you're halfway there.",
        "The only way to do great work is to love what you do.",
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "Don't watch the clock; do what it does. Keep going.",
        "The secret of getting ahead is getting started."
    ]
    quote = random.choice(quotes)

    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 15)
            self.cell(0, 10, 'REPORT OF ASHIRBAD PATTNAIK', 0, 1, 'C')
            self.ln(10)

        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    pdf = PDF()
    pdf.add_page()

    # File Changes Section
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Changes Done:', 0, 1)

    pdf.set_font('Arial', '', 11)
    pdf.cell(0, 10, f'Files Added ({len(added_files)}):', 0, 1)
    for f in added_files:
        pdf.cell(0, 8, f'  - {f}', 0, 1)

    pdf.cell(0, 10, f'Files Changed ({len(changed_files)}):', 0, 1)
    for f in changed_files:
        pdf.cell(0, 8, f'  - {f}', 0, 1)

    pdf.ln(10)

    # Scores Section
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Test Scores:', 0, 1)
    pdf.set_font('Arial', '', 11)
    pdf.cell(0, 8, f'Passed: {passed} / {total}', 0, 1)
    pdf.cell(0, 8, f'Failed: {failed} / {total}', 0, 1)

    pdf.ln(5)
    # Add Pie Chart
    if os.path.exists('pie_chart.png'):
        pdf.image('pie_chart.png', x=50, w=100)

    pdf.ln(10)

    # Motivation Section
    pdf.set_font('Arial', 'I', 12)
    pdf.multi_cell(0, 10, f'Motivational Quote:\n"{quote}"')

    pdf.output('report.pdf')

def generate_email_html(added_files, changed_files, passed, failed, total):
    html_content = f"""
    <html>
    <body>
        <h2>Daily Python Learning Progress Report</h2>
        <p>Hello team! Here is the summary of the daily automated checks.</p>

        <h3>Files Added ({len(added_files)})</h3>
        <ul>
            {''.join([f"<li>{f}</li>" for f in added_files])}
        </ul>

        <h3>Files Changed ({len(changed_files)})</h3>
        <ul>
            {''.join([f"<li>{f}</li>" for f in changed_files])}
        </ul>

        <h3>Test Scores 🎯</h3>
        <ul>
            <li>Passed: {passed} / {total} ✅</li>
            <li>Failed: {failed} / {total} ❌</li>
        </ul>

        <h3>Great job! You are doing awesome!</h3>
        <p>
            <img src="https://media.giphy.com/media/11sBLVxNs7v6WA/giphy.gif" alt="Superb" width="150" />
            <img src="https://media.giphy.com/media/fsQbx1hX7hPBBpIM5b/giphy.gif" alt="Cool" width="150" />
            <img src="https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif" alt="Champ" width="150" />
        </p>
        <p>Keep up the good work! 💪😎🚀</p>
    </body>
    </html>
    """
    with open('email_body.html', 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    added, changed = get_git_changes()
    passed, failed, total = get_test_scores()

    create_pie_chart(passed, failed, total)
    generate_pdf(added, changed, passed, failed, total)
    generate_email_html(added, changed, passed, failed, total)

    print("Report generated successfully.")
