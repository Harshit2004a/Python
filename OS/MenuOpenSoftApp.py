# Menu Driven Python program for opening the required software Application
import os
import platform
import subprocess

def open_application(choice):
    system = platform.system()

    if system == "Windows":
        apps = {
            1: "notepad",
            2: "calc",
            3: "mspaint",
            4: "explorer",
            5: "chrome",
        }
    elif system == "Darwin":
        apps = {
            1: "open -a TextEdit",
            2: "open -a Calculator",
            3: "open -a Preview",
            4: "open .",
            5: "open -a Google\\ Chrome",
        }
    elif system == "Linux":
        apps = {
            1: "gedit",
            2: "gnome-calculator",
            3: "eog",
            4: "xdg-open .",
            5: "google-chrome",
        }
    else:
        print("Unsupported OS")
        return

    command = apps.get(choice)
    if command:
        try:
            subprocess.Popen(command if isinstance(command, list) else command.split())
        except FileNotFoundError:
            print("Application not found. Make sure it's installed.")
    else:
        print("Invalid choice.")

def main():
    while True:
        print("\n--- Software Launcher Menu ---")
        print("1. Text Editor")
        print("2. Calculator")
        print("3. Image Viewer or Paint")
        print("4. File Explorer")
        print("5. Web Browser (Chrome)")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 6:
                print("Exiting...")
                break
            open_application(choice)
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()

# Code by Harshit