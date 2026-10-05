import subprocess
import tkinter as tk
from tkinter import ttk
import adbpytools
from tkinter import messagebox

# Main Window
def ErrorCheck(ErrorMessage):
    adbpytools.InstallAPK(PathInput.get())
    if subprocess.CalledProcessError:
        messagebox.showerror("ADB Command Failed", ErrorMessage)

root = tk.Tk()
root.title("ADB GUI")
root.geometry("400x500")

InstallFrame = ttk.Frame(root, padding=10)
InstallFrame.pack(fill=tk.BOTH, expand=True)

PathInput = ttk.Entry(InstallFrame, width=50)
PathInput.pack(pady=10)
InstallButton = ttk.Button(InstallFrame, text="Install APK", command=lambda: ErrorCheck("Failed to install APK."))
InstallButton.pack(pady=10)

LogcatFrame = ttk.Frame(root, padding=10)
LogcatFrame.pack(fill=tk.BOTH, expand=True)

LogcatButton = ttk.Button(LogcatFrame, text="Run Logcat", command=adbpytools.Logcat)
LogcatButton.pack(pady=10)

root.mainloop()