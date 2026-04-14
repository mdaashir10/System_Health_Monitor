# Python script to send alert via Telegram bot
# This program monitors system health

import psutil
import requests
import datetime

BOT_TOKEN = "8766959012:AAFJFkf_IaR4vejnliM2UnNvMg726jG3Th0"
CHAT_ID = "6958926293"
LOG_FILE = "health.log"

# Setting limit
CPU_THRESHOLD = 80
RAM_THRESHOLD = 80

def send_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": message})

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

if __name__ == '__main__':
    check_health()
