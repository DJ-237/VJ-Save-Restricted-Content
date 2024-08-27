import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23875576"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e2cd4340c9ebb2477c7e948a4045dd49")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://glalgupta205:2et2DcUmVjoNJnl2@cluster0.mybbc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
