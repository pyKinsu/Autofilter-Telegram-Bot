

### ✅ Final `README.md`

````markdown
# 📁 AutoFilter Telegram Bot

A clean and powerful Telegram AutoFilter Bot that automatically indexes and retrieves files (movies, videos, documents, etc.) from a MongoDB database.

> ✏️ **Note:** I am not the original creator of this codebase. I’ve only edited, cleaned, and published it for public use. The code had no specific author attribution when I received it.

🔗 **GitHub Repo**: [pyKinsu/AutofilterTelegramBot](https://github.com/pyKinsu/AutofilterTelegramBot)

---

## 🚀 Features

- 🔍 Auto-index Telegram files and videos into a database
- ⚡ Smart and fast search system
- 🔐 Admin-only controls & logging support
- 🧩 Easy to deploy and maintain
- 💯 Open-source and fully customizable

---

## 🛠️ Environment Variables

To run the bot, set the following environment variables.  
Use **your own values** – these are just placeholders.

| Variable Name     | Description                                                   |
|------------------|---------------------------------------------------------------|
| `DATABASE_URI`    | MongoDB URI (from MongoDB Atlas or your own server)          |
| `DATABASE_NAME`   | MongoDB database name                                         |
| `COLLECTION_NAME` | MongoDB collection name for storing indexed files            |
| `API_ID`          | Telegram API ID (get from [my.telegram.org](https://my.telegram.org)) |
| `API_HASH`        | Telegram API Hash                                             |
| `BOT_TOKEN`       | Token from [@BotFather](https://t.me/BotFather)              |
| `ADMINS`          | Telegram user IDs of bot admins (comma-separated)            |
| `LOG_CHANNEL`     | Telegram channel ID for logging events/errors                |

---

## 📦 Example `.env` File

```env
DATABASE_URI=your_mongodb_uri_here
DATABASE_NAME=your_database_name
COLLECTION_NAME=your_collection_name
API_ID=your_telegram_api_id
API_HASH=your_telegram_api_hash
BOT_TOKEN=your_bot_token
ADMINS=123456789,987654321
LOG_CHANNEL=-1001234567890
````

> ⚠️ Don’t use example values – fill in your own credentials.

---

## 🚀 How to Deploy

1. **Fork** the repository
   [Click here to fork](https://github.com/pyKinsu/AutofilterTelegramBot/fork)

2. Clone your forked repo:

   ```bash
   git clone https://github.com/your-username/AutofilterTelegramBot.git
   cd AutofilterTelegramBot
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file (or export variables) and run the bot:

   ```bash
   python3 bot.py
   ```

---

## 🧾 License

This project is licensed under the **MIT License**.
See the [LICENSE](./LICENSE) file for details.

---

## 🙏 Credits

* 🛠 Code published and maintained by: [@pykinsu](https://t.me/pykinsu)
* ❌ No original developer attribution — published for free public use

---

## 🤝 Support

For help or questions:
📬 Telegram Contact → [@kissuhelp](https://t.me/kissuhelp)

```

---
