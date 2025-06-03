🔐 SecureSysAudit

**SecureSysAudit** is a lightweight Python-based tool designed to perform a basic security audit on Linux systems. It collects system information, inspects user and SSH configurations, and summarizes the results into a Markdown report.

## 📌 Features

- Collects OS and kernel information
- Lists all user accounts
- Identifies users with sudo privileges
- Displays currently logged-in users
- Checks SSH configuration settings
- Shows firewall status (UFW)
- Generates a clear, human-readable audit report

## 🛠️ Usage

1. Clone the repository:

```bash
git clone https://github.com/enormous7/SecureSysAudit.git
cd SecureSysAudit

2. Run the audit script:

Copy
Edit
python3 audit.py

3. View the generated report.md file for the audit results:

cat report.md

🧱 Requirements
No external Python packages required. Script uses built-in modules and standard Linux commands.

📂 Project Structure
bash
Copy
Edit
SecureSysAudit/
├── audit.py            # Main audit script
├── report.md           # Auto-generated audit report
├── README.md           # Project documentation
├── requirements.txt    # Python package list (currently empty)
└── .gitignore          # Ignored files

🎯 Purpose
This project was created as part of a cybersecurity portfolio to demonstrate practical skills in system auditing, scripting, and automation. It is tailored to support applications for roles such as Information System Security Specialist.

👩‍💻 Author
GitHub: enormous7

Project Date: June 2025

