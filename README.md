# Python Learning Workflow

Welcome to the collaborative Python learning repository!

## Workflow

This repository uses a structured process to ensure that new code is properly reviewed and tested. Here's how it works:

1. **Write Code in a New Branch**:
   - Create a new branch (e.g., `git checkout -b daily-code-updates`).
   - Add your Python code to the repository. For example, create a new script or update existing ones in a directory like `daily_codes/`.
2. **Create a Pull Request**:
   - Commit your code and push the branch to GitHub.
   - Open a Pull Request against the `main` branch.
3. **Review and Approve**:
   - The owner will review the Pull Request and approve the changes.
4. **Merge and Automate Testing**:
   - Once the Pull Request is merged into the `main` branch, GitHub Actions will automatically run.
   - It will check if the Python code successfully executes and passes the tests.
5. **Email Notifications**:
   - An email report containing the test results will be automatically sent to the configured team members upon success or failure.
   - There's also a daily progress report sent every day at 8:00 AM UTC.
