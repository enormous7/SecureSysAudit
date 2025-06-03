import os
import platform
import subprocess

def get_os_info():
    return platform.platform()

def get_kernel_info():
    return platform.uname()

def get_logged_in_users():
    return subprocess.getoutput("who")

def list_users():
    return subprocess.getoutput("cut -d: -f1 /etc/passwd")

def check_sudo_users():
    return subprocess.getoutput("getent group sudo")

def check_ssh_config():
    path = "/etc/ssh/sshd_config"
    if os.path.exists(path):
        with open(path, "r") as file:
            return file.read()
    return "SSH configuration file not found."

def check_firewall_status():
    return subprocess.getoutput("sudo ufw status")

def generate_report():
    with open("report.md", "w") as report:
        report.write("# Security Audit Report\n\n")
        report.write("## OS Information\n")
        report.write(f"{get_os_info()}\n\n")
        
        report.write("## Kernel Information\n")
        report.write(f"{get_kernel_info()}\n\n")

        report.write("## Logged-in Users\n")
        report.write(f"{get_logged_in_users()}\n\n")

        report.write("## System Users\n")
        report.write(f"{list_users()}\n\n")

        report.write("## Sudo Group Members\n")
        report.write(f"{check_sudo_users()}\n\n")

        report.write("## SSH Configuration\n")
        report.write(f"```\n{check_ssh_config()}\n```\n\n")

        report.write("## Firewall Status\n")
        report.write(f"```\n{check_firewall_status()}\n```\n\n")

if __name__ == "__main__":
    generate_report()
    print("Security audit completed. See 'report.md' for results.")
