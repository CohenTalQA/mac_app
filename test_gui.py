import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import subprocess
import json
from pathlib import Path
import threading
import time
import requests
import sys


if getattr(sys, 'frozen', False):
    BASE_PATH = Path(sys._MEIPASS)
else:
    BASE_PATH = Path(__file__).parent

CONFIG_PATH = BASE_PATH / "config"

current_process = None
appium_process = None


# ---------------- APPium ---------------- #

def wait_for_appium():
    for _ in range(15):
        try:
            r = requests.get("http://127.0.0.1:4723/status")
            if r.status_code == 200:
                return True
        except:
            pass
        time.sleep(1)
    return False


def start_appium():
    global appium_process

    if appium_process and appium_process.poll() is None:
        status_label.config(text="Appium already running", fg="orange")
        return

    try:
        appium_process = subprocess.Popen(["appium.cmd"])
        status_label.config(text="Starting Appium...", fg="blue")

        if wait_for_appium():
            status_label.config(text="Appium Ready 🚀", fg="green")
        else:
            status_label.config(text="Appium failed to start", fg="red")

    except FileNotFoundError:
        status_label.config(text="Appium not installed", fg="red")


def stop_appium():
    global appium_process

    if appium_process and appium_process.poll() is None:
        appium_process.terminate()
        appium_process.wait()
        status_label.config(text="Appium stopped", fg="red")
    else:
        status_label.config(text="Appium not running", fg="orange")


# ---------------- ADB ---------------- #

def check_adb():
    try:
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True)

        lines = result.stdout.strip().split("\n")

        if len(lines) > 1 and "device" in lines[1]:
            adb_label.config(text="🟢 Device Connected", fg="green")
        else:
            adb_label.config(text="🔴 No Device", fg="red")

    except:
        adb_label.config(text="ADB not found", fg="red")


# ---------------- TEST RUNNER ---------------- #

def run_tests(env):
    global current_process

    status_label.config(text="Running tests...", fg="blue")
    progress.start()

    config_file = CONFIG_PATH / f"config_{env}.json"

    with open(config_file, "r", encoding="utf-8") as f:
        config_data = json.load(f)

    config_data["flows"]["login"] = login_var.get()
    config_data["flows"]["create_appointment"] = create_var.get()
    config_data["flows"]["edit_appointment"] = edit_var.get()
    config_data["flows"]["cancel_appointment"] = cancel_var.get()

    with open(config_file, "w", encoding="utf-8") as f:
        json.dump(config_data, f, indent=4, ensure_ascii=False)

    current_process = subprocess.Popen(
        ["python", "-m", "pytest", f"--env={env}", "--tb=short"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    stop_button.config(state="normal")
    text_area.delete("1.0", tk.END)

    for line in current_process.stdout:
        text_area.insert(tk.END, line)
        text_area.see(tk.END)

    current_process.wait()

    progress.stop()
    stop_button.config(state="disabled")

    if current_process.returncode == 0:
        status_label.config(text="Tests Passed ✅", fg="green")
    else:
        status_label.config(text="Tests Failed ❌", fg="red")


def start_run(env):
    threading.Thread(target=run_tests, args=(env,), daemon=True).start()


def stop_tests():
    global current_process

    if current_process and current_process.poll() is None:
        current_process.terminate()
        status_label.config(text="Tests stopped", fg="orange")
        progress.stop()


# ---------------- UI ---------------- #

root = tk.Tk()
root.title("Automation Test Dashboard")
root.geometry("750x550")

title = tk.Label(root, text="Automation Test Dashboard", font=("Arial", 16, "bold"))
title.pack(pady=10)


# ----- ADB -----

adb_label = tk.Label(root, text="ADB Status: Unknown", font=("Arial", 11))
adb_label.pack(pady=5)

tk.Button(root, text="Check ADB", command=check_adb).pack(pady=5)


# ----- Appium -----

tk.Button(root, text="Start Appium", width=20, command=start_appium).pack(pady=5)

tk.Button(root, text="Stop Appium", width=20, bg="orange", command=stop_appium).pack(pady=5)


# ----- Flows -----

flows_frame = tk.LabelFrame(root, text="Select Flows")
flows_frame.pack(pady=10)

login_var = tk.BooleanVar(value=True)
create_var = tk.BooleanVar(value=True)
edit_var = tk.BooleanVar(value=True)
cancel_var = tk.BooleanVar(value=False)

tk.Checkbutton(flows_frame, text="Login", variable=login_var).pack(anchor="w")
tk.Checkbutton(flows_frame, text="Create Appointment", variable=create_var).pack(anchor="w")
tk.Checkbutton(flows_frame, text="Edit Appointment", variable=edit_var).pack(anchor="w")
tk.Checkbutton(flows_frame, text="Cancel Appointment", variable=cancel_var).pack(anchor="w")


# ----- Environment -----

env_frame = tk.LabelFrame(root, text="Environment")
env_frame.pack(pady=10)

tk.Button(env_frame, text="Run TEST", width=15, command=lambda: start_run("test")).pack(side="left", padx=10)
tk.Button(env_frame, text="Run PROD", width=15, command=lambda: start_run("prod")).pack(side="left", padx=10)


stop_button = tk.Button(root, text="STOP", width=20, bg="red", fg="white", command=stop_tests, state="disabled")
stop_button.pack(pady=5)


# ----- Status -----

status_label = tk.Label(root, text="Idle", font=("Arial", 12))
status_label.pack(pady=5)

progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="indeterminate")
progress.pack(pady=5)


# ----- Output -----

text_area = ScrolledText(root, height=20, width=90)
text_area.pack(pady=10)


root.mainloop()



