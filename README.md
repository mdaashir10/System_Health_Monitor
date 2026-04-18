# System Health Monitor

A Python + Bash tool that monitors CPU, RAM, and disk usage every 5 minutes and sends Telegram alerts when thresholds are exceeded.

## Features
- Logs system stats to health.log
- Sends Telegram alerts if CPU or RAM exceeds 80%
- Runs automatically via cron every 5 minutes

## Setup
### First create your personal BOT
1. Go to Telegram and search for BotFather
2. Start your bot with -> /start, then give a name
3. Then you will receive your API (or bot token)
4. Search on browser -> https://api.telegram.org/bot{BOT_TOKEN}/getUpdates
5. Here you will find your chat ID
6. Go ahead with option 1 or 2

### Option 1 - Run directly
1. Clone the repo
2. Create a virtual environment: python -m venv venv
3. Install dependencies: pip install -r requirements.txt
4. Copy dot_env_example to .env and fill in your values
5. Make alert script executable: chmod +x alert
6. Add cron job: crontab -e
   */5 * * * * /full/path/to/system-health-monitor/alert

### Option 2 — Run with Docker
1. Clone the repo
2. Copy dot_env_example to .env and fill in your values
3. docker build -t system-health-monitor .
4. docker run --env-file .env system-health-monitor

## Environment Variables
Create a .env file with:
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id
