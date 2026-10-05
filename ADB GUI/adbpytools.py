import subprocess
import sys

# ADB commands
def InstallAPK(Path):
    try:
        subprocess.run(["adb", "install", Path], check=True)
    except subprocess.CalledProcessError:
        print(f"Error installing APK. See above")

def Logcat():
    try:
        subprocess.run(["adb", "logcat"], check=True)
    except subprocess.CalledProcessError:
        print(f"Error running logcat. See above")

# sys.stdout redirection
class TextRedirector:
    def __init__(self, text_widget):
        self.widget = text_widget
    def write(self, text):
        self.widget.insert("end", text)
        self.widget.see("end")
    def flush(self):
        pass
