import subprocess

try: 
    subprocess.run(["adb", "install"], check=True)
except subprocess.CalledProcessError:
    print(f"Error occurred while installing APK. See above")