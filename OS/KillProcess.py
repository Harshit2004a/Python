# Kill a Process by name using Python

import psutil

def kill_process_by_name(name):
    killed = False
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] and name.lower() in proc.info['name'].lower():
            try:
                proc.kill()
                print(f"Killed process: {proc.info['name']} (PID: {proc.info['pid']})")
                killed = True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                print(f"Could not kill: {proc.info['name']} (PID: {proc.info['pid']})")
    if not killed:
        print(f"No process with name containing '{name}' was found.")

kill_process_by_name("notepad")

# Code by Harshit