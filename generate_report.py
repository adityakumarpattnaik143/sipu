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
            # Background color for header
            self.set_fill_color(33, 150, 243) # Blue
            self.set_text_color(255, 255, 255) # White
            self.set_font('helvetica', 'B', 18)
            self.cell(0, 15, 'REPORT OF ASHIRBAD PATTNAIK', border=0, new_x="LMARGIN", new_y="NEXT", align='C', fill=True)
            self.ln(10)

        def footer(self):
            self.set_y(-25)
            # Signature
            self.set_text_color(100, 100, 100)
            self.set_font('helvetica', 'I', 10)
            self.cell(0, 10, 'Curated by: ADITYA KUMAR PATTNAIK', align='C', new_x="LMARGIN", new_y="NEXT")

            # Page number
            self.set_text_color(128, 128, 128)
            self.set_font('helvetica', 'I', 8)
            self.cell(0, 10, f'Page {self.page_no()}', align='C')

    pdf = PDF()
    pdf.add_page()

    # File Changes Section
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('helvetica', 'B', 14)
    pdf.cell(0, 10, 'Changes Done:', new_x="LMARGIN", new_y="NEXT")

    pdf.set_font('helvetica', '', 11)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 10, f'Files Added ({len(added_files)}):', new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(76, 175, 80) # Green for added
    for f in added_files:
        pdf.cell(0, 8, f'  + {f}', new_x="LMARGIN", new_y="NEXT")

    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 10, f'Files Changed ({len(changed_files)}):', new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(255, 152, 0) # Orange for changed
    for f in changed_files:
        pdf.cell(0, 8, f'  ~ {f}', new_x="LMARGIN", new_y="NEXT")

    pdf.ln(10)

    # Scores Section
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('helvetica', 'B', 14)
    pdf.cell(0, 10, 'Test Scores:', new_x="LMARGIN", new_y="NEXT")

    pdf.set_font('helvetica', 'B', 12)
    pdf.set_text_color(76, 175, 80) # Green
    pdf.cell(0, 8, f'Passed: {passed} / {total}', new_x="LMARGIN", new_y="NEXT")

    pdf.set_text_color(244, 67, 54) # Red
    pdf.cell(0, 8, f'Failed: {failed} / {total}', new_x="LMARGIN", new_y="NEXT")

    pdf.ln(5)
    # Add Pie Chart
    if os.path.exists('pie_chart.png'):
        pdf.image('pie_chart.png', x=50, w=100)

    pdf.ln(10)

    # Motivation Section
    pdf.set_text_color(33, 150, 243) # Blue
    pdf.set_font('helvetica', 'I', 12)
    pdf.multi_cell(0, 10, f'Motivational Quote:\n"{quote}"', new_x="LMARGIN", new_y="NEXT")

    pdf.output('report.pdf')

def generate_email_html(added_files, changed_files, passed, failed, total):
    quotes = [
        "Believe you can and you're halfway there.",
        "The only way to do great work is to love what you do.",
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "Don't watch the clock; do what it does. Keep going.",
        "The secret of getting ahead is getting started.",
        "Push yourself, because no one else is going to do it for you.",
        "Great things never come from comfort zones."
    ]
    gifs = [
        "https://media.giphy.com/media/11sBLVxNs7v6WA/giphy.gif",
        "https://media.giphy.com/media/fsQbx1hX7hPBBpIM5b/giphy.gif",
        "https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif",
        "https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif",
        "https://media.giphy.com/media/xT0xezQGU5xCDJuCPe/giphy.gif"
    ]
    emojis = ["💪", "😎", "🚀", "🔥", "🌟", "🎉", "🏆", "🧠"]

    quote = random.choice(quotes)
    selected_gifs = random.sample(gifs, 2)
    selected_emojis = "".join(random.sample(emojis, 3))

    pass_color = "#4CAF50" if passed > 0 else "#757575"
    fail_color = "#F44336" if failed > 0 else "#757575"

    html_content = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f4f7f6;
                color: #333;
                padding: 20px;
                line-height: 1.6;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                background: #fff;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            }}
            .header {{
                background: linear-gradient(135deg, #2196F3, #1976D2);
                color: white;
                text-align: center;
                padding: 20px;
                border-radius: 8px;
                margin-bottom: 20px;
            }}
            .header h2 {{ margin: 0; font-size: 24px; }}
            .section {{
                margin-bottom: 25px;
            }}
            .section h3 {{
                color: #2c3e50;
                border-bottom: 2px solid #eee;
                padding-bottom: 8px;
                margin-bottom: 15px;
            }}
            ul {{ list-style-type: none; padding-left: 0; }}
            ul li {{
                background: #f8f9fa;
                margin-bottom: 8px;
                padding: 10px;
                border-left: 4px solid #007bff;
                border-radius: 4px;
            }}
            .scores ul li:first-child {{ border-left-color: {pass_color}; }}
            .scores ul li:last-child {{ border-left-color: {fail_color}; }}
            .motivation {{
                text-align: center;
                background: #e9ecef;
                padding: 20px;
                border-radius: 8px;
                font-style: italic;
                margin-top: 30px;
            }}
            .gifs {{
                text-align: center;
                margin-top: 20px;
            }}
            .gifs img {{
                border-radius: 8px;
                margin: 0 10px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }}
            .footer {{
                text-align: center;
                margin-top: 40px;
                font-size: 14px;
                color: #6c757d;
                border-top: 1px solid #ddd;
                padding-top: 20px;
            }}
            .signature {{
                font-weight: bold;
                color: #2196F3;
                font-size: 16px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h2>Daily Python Learning Progress</h2>
                <p style="margin-top: 10px; font-size: 14px;">Summary of automated checks</p>
            </div>

            <div class="section">
                <h3>Files Added ({len(added_files)})</h3>
                <ul>
                    {''.join([f"<li>➕ {f}</li>" for f in added_files]) if added_files else "<li>No files added.</li>"}
                </ul>
            </div>

            <div class="section">
                <h3>Files Changed ({len(changed_files)})</h3>
                <ul>
                    {''.join([f"<li>🔄 {f}</li>" for f in changed_files]) if changed_files else "<li>No files changed.</li>"}
                </ul>
            </div>

            <div class="section scores">
                <h3>Test Scores 🎯</h3>
                <ul>
                    <li>Passed: {passed} / {total} ✅</li>
                    <li>Failed: {failed} / {total} ❌</li>
                </ul>
            </div>

            <div class="motivation">
                <p>"{quote}"</p>
                <p>Keep up the great work! {selected_emojis}</p>
            </div>

            <div class="gifs">
                <img src="{selected_gifs[0]}" alt="Motivation GIF" width="150" />
                <img src="{selected_gifs[1]}" alt="Motivation GIF" width="150" />
            </div>

            <div class="footer">
                <p>Generated automatically via GitHub Actions.</p>
                <p>Curated by: <span class="signature">ADITYA KUMAR PATTNAIK</span></p>
            </div>
        </div>
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
