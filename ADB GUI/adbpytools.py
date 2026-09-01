import subprocess

def InstallAPK(Path):
    try:
        subprocess.run(["adb", "install", Path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error installing APK: {e}")