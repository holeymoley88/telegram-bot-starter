# Telegram Bot (Webhook-ready)

This bot can run in two modes:
- **Polling** (local dev)
- **Webhook** (production / Railway / etc.)

## Environment Variables
- `TELEGRAM_BOT_TOKEN` - your BotFather token
- `BASE_URL` - your public URL (omit for polling mode)

## Run locally (polling)
```
pip install -r requirements.txt
python main.py
```

## Deploy to Railway (webhook)
- Add `TELEGRAM_BOT_TOKEN` and `BASE_URL` in Railway Variables
- Start command: `python main.py`
