import subprocess

def InstallAPK(Path):
    try:
        subprocess.run(["adb", "install", Path], check=True)
    except subprocess.CalledProcessError:
        print(f"Error installing APK. See above")