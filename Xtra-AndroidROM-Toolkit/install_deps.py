import os
import sys
import platform
import subprocess

def is_termux():
    return "com.termux" in os.environ.get("PREFIX", "")

def run_command(command, shell=False):
    try:
        subprocess.run(command, shell=shell, check=True)
    except subprocess.CalledProcessError:
        print(f"❌ Failed to execute: {command}")

def main():
    print("🧠 Detection Operating System...")

    system = platform.system()
    if is_termux():
        print("📱 Termux Android Detected")
        script = "install_deps_termux.sh"
        if os.path.exists(script):
            run_command(["bash", script])
        else:
            print(f"❌ Script {script} Not Found.")
    elif system == "Linux":
        print("🐧 Linux Detected")
        script = "install_deps_linux.sh"
        if os.path.exists(script):
            run_command(["bash", script])
        else:
            print(f"❌ Script {script} Not Found.")
    elif system == "Windows":
        print("🪟 Windows Detected")
        script = "install_deps_windows.bat"
        if os.path.exists(script):
            run_command([script], shell=True)
        else:
            print(f"❌ Script {script} Not Found.")
    else:
        print(f"🤷 Unrecognized System: {system}")

if __name__ == "__main__":
    main()