# Python script to send alert via Telegram bot
# This program monitors system health

import psutil
import requests
import datetime

# Reading confidentials from .env
import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
LOG_FILE = "health.log"

# Setting limit
CPU_THRESHOLD = 20
RAM_THRESHOLD = 20

def send_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": message}, timeout=10)

def log_stats(cpu, ram, disk):
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} | CPU: {cpu}% | RAM: {ram}% | Disk: {disk}%\n")

def check_health():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    log_stats(cpu, ram, disk)

    if cpu > CPU_THRESHOLD:
        send_alert(f"ALERT: High CPU usage detected: {cpu}%")
    if ram > RAM_THRESHOLD:
        send_alert(f"ALERT: High RAM usage detected: {ram}%")

check_health()
