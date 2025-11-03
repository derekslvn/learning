import tkinter as tk
import keyboard
import threading
import time
import sys

running = False
suspended = False

def release_all():
    """Release all keys that may have been pressed earlier."""
    for key in ["up", "w", "left", "right", "q", "d"]:
        keyboard.release(key)

def start_macro():
    global running
    if not running:
        running = True
        release_all()  # make sure nothing is stuck
        status_label.config(text="Running UP + W loop...")
        threading.Thread(target=macro_loop, daemon=True).start()

def macro_loop():
    global running, suspended
    while running:
        if suspended:
            time.sleep(0.1)
            continue

        if keyboard.is_pressed("up"):
            keyboard.press("up")
            keyboard.press("w")
            time.sleep(0.015)  # Adjust speed if needed
            keyboard.release("up")
            keyboard.release("w")
        else:
            keyboard.release("up")
            keyboard.release("w")
            time.sleep(0.02)

        time.sleep(0.001)

def stop_macro():
    global running
    running = False
    release_all()
    status_label.config(text="Stopped.")
    root.after(300, sys.exit)

def suspend_macro():
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

# ================= GUI =================
root = tk.Tk()
root.title("Python Macro GUI")
root.geometry("340x220")
root.resizable(False, False)

tk.Label(root, text="Script Controls:", font=("Segoe UI", 10, "bold")).pack(pady=5)
tk.Button(root, text="Start Macro", width=20, command=start_macro).pack(pady=3)
tk.Button(root, text="Suspend / Resume", width=20, command=suspend_macro).pack(pady=3)
tk.Button(root, text="Stop Script", width=20, command=stop_macro).pack(pady=3)

tk.Label(root, text="Commands:", font=("Segoe UI", 10, "bold")).pack(pady=5)
tk.Button(root, text="F1 (/f)", width=20, command=do_f1).pack(pady=3)
tk.Button(root, text="F2 (/mort)", width=20, command=do_f2).pack(pady=3)

status_label = tk.Label(root, text="Idle", fg="blue")
status_label.pack(pady=10)

root.mainloop()
