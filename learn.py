import tkinter as tk
import keyboard
import threading
import time
import sys

running = False
suspended = False

# ================ ACTION FUNCTIONS =================
def start_up_loop():
    global running
    if not running:
        running = True
        status_label.config(text="Running UP loop...")
        threading.Thread(target=up_loop, daemon=True).start()

def up_loop():
    global running, suspended
    while running:
        if suspended:
            time.sleep(0.1)
            continue
        if keyboard.is_pressed("up"):
            keyboard.press("up")
            keyboard.press("w")
            time.sleep(0.01)
        else:
            time.sleep(0.1)

def stop_script():
    global running
    running = False
    status_label.config(text="Stopped.")
    root.after(500, sys.exit)

def suspend_script():
    global suspended
    suspended = not suspended
    status_label.config(text="Suspended" if suspended else "Running...")

def do_f1():
    keyboard.write("/f")
    keyboard.press_and_release("enter")
    status_label.config(text="Sent /f")

def do_f2():
    keyboard.write("/mort")
    keyboard.press_and_release("enter")
    status_label.config(text="Sent /mort")

# ================ GUI =================
root = tk.Tk()
root.title("Python Macro GUI")
root.geometry("340x220")
root.resizable(False, False)

tk.Label(root, text="Script Controls:", font=("Segoe UI", 10, "bold")).pack(pady=5)

tk.Button(root, text="Start UP Loop", width=20, command=start_up_loop).pack(pady=3)
tk.Button(root, text="Suspend / Resume", width=20, command=suspend_script).pack(pady=3)
tk.Button(root, text="Stop Script", width=20, command=stop_script).pack(pady=3)

tk.Label(root, text="Commands:", font=("Segoe UI", 10, "bold")).pack(pady=5)
tk.Button(root, text="F1 (/f)", width=20, command=do_f1).pack(pady=3)
tk.Button(root, text="F2 (/mort)", width=20, command=do_f2).pack(pady=3)

status_label = tk.Label(root, text="Idle", fg="blue")
status_label.pack(pady=10)

root.mainloop()
