# Telegram Bot Starter (Polling, no web server)

This is a minimal Telegram bot that uses *polling* (no webhooks, no Flask).

## Files
- `main.py` — the bot code
- `requirements.txt` — dependencies
- `.replit` — lets the Run button call `python main.py` (Replit may still require using the Shell)

## Quick start on Replit (GitHub import flow)
1) Create a new GitHub repo and upload these three files, or use Replit's "Import from GitHub" with this ZIP.
2) In Replit, open **Secrets** and add:
   - Key: `TELEGRAM_BOT_TOKEN` — Value: your BotFather token
3) Open the **Shell** tab and run:
   ```
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   python main.py
   ```
   (If `python` fails, use `python3` instead.)

4) In Telegram, open your bot and send `/start`.
