# copyright 2023 © Xron Trix | https://github.com/Xrontrix10

import logging, json
import asyncio # <-- 1. Import asyncio
from uvloop import install
from pyrogram.client import Client

# Read the dictionary from the txt file
with open("/content/Telegram-Leecher/credentials.json", "r") as file:
    credentials = json.loads(file.read())

API_ID = credentials["API_ID"]
API_HASH = credentials["API_HASH"]
BOT_TOKEN = credentials["BOT_TOKEN"]
OWNER = credentials["USER_ID"]
DUMP_ID = credentials["DUMP_ID"]


logging.basicConfig(level=logging.INFO)

install()

# 2. Define an async function to hold the bot logic
async def main():
    # 3. Client initialization MUST be inside the async function
    colab_bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
    
    print("Starting Bot....")
    
    # 4. Use async with to manage the connection
    async with colab_bot:
        print("Bot is running. Press Ctrl+C to stop.")
        # This keeps the bot active and listening for updates
        await colab_bot.idle() 
        

# 5. Use the standard asynchronous entry point
if __name__ == "__main__":
    try:
        # This creates the event loop and runs the main() coroutine
        asyncio.run(main()) 
    except KeyboardInterrupt:
        print("\nBot stopped by user.")
