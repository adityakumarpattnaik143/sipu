import json
import subprocess
import os
import xml.etree.ElementTree as ET
from fpdf import FPDF
import matplotlib.pyplot as plt
from datetime import datetime
import random

def get_git_changes():
    try:
        # Get files changed in the last 24 hours
        result = subprocess.run(
            ['git', 'log', '--since="24 hours ago"', '--name-status', '--pretty=format:'],
            capture_output=True, text=True
        )
        lines = result.stdout.strip().split('\n')
        added = []
        changed = []
        for line in lines:
            if not line.strip(): continue
            parts = line.split('\t', 1)
            if len(parts) == 2:
                status, name = parts
                if status.startswith('A'):
                    added.append(name)
                elif status.startswith('M') or status.startswith('C') or status.startswith('R'):
                    changed.append(name)

        # If no changes in 24 hours (e.g. testing manually), fallback to last commit
        if not added and not changed:
            result = subprocess.run(
                ['git', 'show', '--name-status', '--pretty=format:'],
                capture_output=True, text=True
            )
            lines = result.stdout.strip().split('\n')
            for line in lines:
                if not line.strip(): continue
                parts = line.split('\t', 1)
                if len(parts) == 2:
                    status, name = parts
                    if status.startswith('A'):
                        added.append(name)
                    elif status.startswith('M') or status.startswith('C') or status.startswith('R'):
                        changed.append(name)

        return list(set(added)), list(set(changed))
    except Exception as e:
        print(f"Error getting git changes: {e}")
        return [], []

def run_tests():
    try:
        # Run pytest and output to xml for easy parsing
        subprocess.run(['pytest', '--junitxml=report.xml'], capture_output=True, text=True)

        passed = 0
        failed = 0
        total = 0

        if os.path.exists('report.xml'):
            tree = ET.parse('report.xml')
            root = tree.getroot()
            # testsuite element contains tests, failures, errors
            testsuite = root.find('testsuite')
            if testsuite is None:
                # pytest sometimes has testsuites as root
                testsuite = root.find('.//testsuite')

            if testsuite is not None:
                total = int(testsuite.get('tests', 0))
                failed = int(testsuite.get('failures', 0)) + int(testsuite.get('errors', 0))
                passed = total - failed

        return passed, failed, total
    except Exception as e:
        print(f"Error running tests: {e}")
        return 0, 0, 0

def create_pie_chart(passed, failed):
    labels = ['Passed', 'Failed']
    sizes = [passed, failed]
    if passed == 0 and failed == 0:
        sizes = [1, 0] # Avoid empty chart
        labels = ['No Tests', '']
    colors = ['#4CAF50', '#F44336']
    explode = (0.1, 0)

    plt.figure(figsize=(6,4))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct=lambda p: '{:.1f}%'.format(p) if p > 0 else '', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title('Test Scores')
    plt.savefig('pie_chart.png')
    plt.close()

def generate_pdf(added, changed, passed, failed, total):
    create_pie_chart(passed, failed)

    class PDF(FPDF):
        def header(self):
            self.set_font('helvetica', 'B', 15)
            # Use XPos and YPos parameters to avoid deprecation warnings
            self.cell(0, 10, 'REPORT OF ASHIRBAD PATTNAIK', new_x="LMARGIN", new_y="NEXT", align='C')
            self.ln(10)

        def footer(self):
            self.set_y(-15)
            self.set_font('helvetica', 'I', 8)
            self.cell(0, 10, f'Page {self.page_no()}', new_x="RIGHT", new_y="TOP", align='C')

    pdf = PDF()
    pdf.add_page()
    pdf.set_font('helvetica', '', 12)

    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pdf.cell(0, 10, f'Date: {date_str}', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(0, 10, 'Changes Done:', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('helvetica', '', 12)

    pdf.cell(0, 10, f'Files Added ({len(added)}):', new_x="LMARGIN", new_y="NEXT")
    for f in added[:10]: # Limit to 10
        pdf.cell(0, 8, f'  + {f}', new_x="LMARGIN", new_y="NEXT")
    if len(added) > 10: pdf.cell(0, 8, '  ... and more', new_x="LMARGIN", new_y="NEXT")

    pdf.cell(0, 10, f'Files Changed ({len(changed)}):', new_x="LMARGIN", new_y="NEXT")
    for f in changed[:10]:
        pdf.cell(0, 8, f'  ~ {f}', new_x="LMARGIN", new_y="NEXT")
    if len(changed) > 10: pdf.cell(0, 8, '  ... and more', new_x="LMARGIN", new_y="NEXT")

    pdf.ln(10)

    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(0, 10, 'Scores:', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('helvetica', '', 12)
    pdf.cell(0, 10, f'Total Tests: {total}', new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f'Passed: {passed}/{total}', new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f'Failed: {failed}/{total}', new_x="LMARGIN", new_y="NEXT")

    if os.path.exists('pie_chart.png'):
        pdf.image('pie_chart.png', x=50, y=None, w=100)

    pdf.ln(10)
    quotes = [
        "\"The only way to do great work is to love what you do.\" - Steve Jobs",
        "\"Code is like humor. When you have to explain it, it's bad.\" - Cory House",
        "\"First, solve the problem. Then, write the code.\" - John Johnson",
        "\"Make it work, make it right, make it fast.\" - Kent Beck",
        "\"Success is not final, failure is not fatal: it is the courage to continue that counts.\" - Winston Churchill"
    ]
    pdf.set_font('helvetica', 'I', 11)
    pdf.multi_cell(0, 10, random.choice(quotes))

    pdf.output('Ashirbad_Pattnaik_Report.pdf')

def generate_email_body(added, changed, passed, failed, total):
    gifs = [
        "https://media.giphy.com/media/11sBLVxNs7v6WA/giphy.gif", # Superb/Minions
        "https://media.giphy.com/media/bKBM7H63PIykM/giphy.gif", # Cool/Snoop
        "https://media.giphy.com/media/l0amJzVHIAfl7jMDos/giphy.gif" # Champ
    ]
    gif_url = random.choice(gifs)

    added_li = "".join([f"<li>{f}</li>" for f in added])
    changed_li = "".join([f"<li>{f}</li>" for f in changed])

    if not added_li: added_li = "<li>No new files added.</li>"
    if not changed_li: changed_li = "<li>No files changed.</li>"

    html = f"""
    <html>
    <body>
        <h2>Daily Python Learning Progress Report 🎉🚀</h2>
        <p>Hello Ashirbad! Here is your daily summary 😎</p>

        <h3>Scores 🏆</h3>
        <ul>
            <li><b>Total Tests:</b> {total}</li>
            <li><b>Passed:</b> <span style="color: green;">{passed}/{total}</span></li>
            <li><b>Failed:</b> <span style="color: red;">{failed}/{total}</span></li>
        </ul>

        <h3>Files Added 🌟</h3>
        <ul>{added_li}</ul>

        <h3>Files Changed 🔧</h3>
        <ul>{changed_li}</ul>

        <p>Keep up the fantastic work! You are superb! Cool! Champ! 🥳</p>
        <img src="{gif_url}" alt="Motivation GIF" width="300"/>

        <p><small>See the attached PDF for a detailed report with charts.</small></p>
    </body>
    </html>
    """
    with open('email_body.html', 'w') as f:
        f.write(html)

if __name__ == "__main__":
    added, changed = get_git_changes()
    passed, failed, total = run_tests()
    generate_pdf(added, changed, passed, failed, total)
    generate_email_body(added, changed, passed, failed, total)
