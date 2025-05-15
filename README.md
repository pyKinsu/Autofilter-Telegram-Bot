# 📁 AutoFilter Telegram Bot

A clean and powerful Telegram AutoFilter Bot for (movies, videos, documents, etc.) 

> ✏️ **Note:** I am not the original creator of this codebase. I’ve only edited, cleaned, and published it for public use. The code had no specific author.

<a href="https://github.com/pyKinsu/AutofilterTelegramBot" target="_blank">
  <img src="https://img.shields.io/badge/View%20on-GitHub-blue?style=plastic&logo=github" width="200" height="38.5" alt="View on GitHub" />
</a>

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

| Variable          |  Values                                                  |
|-------------------|---------------------------------------------------------------|
| `DATABASE_URI`    | MongoDB URI (from MongoDB Atlas or your own server)          |
| `DATABASE_NAME`   | MongoDB database name                                         |
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
<a href="https://github.com/pyKinsu/AutofilterTelegramBot/fork" target="_blank">
  <img src="https://img.shields.io/badge/Fork%20this-Repository-success?logo=github&style=for-the-badge" width="200" height="38.5" alt="Fork this Repository" />
</a>



---

## 🧾 License

<a href="./LICENSE" target="_blank">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge&logo=opensourceinitiative" width="200" height="38.5" alt="License: MIT" />
</a>
---

## 🙏 Credits

* 🛠 Code published and maintained by: [@pykinsu](https://github.com/pykinsu)
* ❌ No original developer attribution — published for free public use

---

<h2>🌟 Support <img src="https://media.giphy.com/media/LnQjpWaON8nhr21vNW/giphy.gif" width="32"/></h2> <p align="center"> <a href="https://telegram.me/kissuhelp"><img src="https://img.shields.io/badge/-Contact%20Me-black.svg?style=for-the-badge&logo=Telegram" width="200" height="38.5"/></a> </p> <p align="center"> <a href="https://telegram.me/kissubots"><img src="https://img.shields.io/badge/-Support%20Channel-black.svg?style=for-the-badge&logo=Telegram" width="200" height="38.5"/></a> </p>
