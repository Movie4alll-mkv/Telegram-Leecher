# copyright 2023 © Xron Trix | https://github.com/Xrontrix10

import logging, json
import asyncio # <--- ADD THIS
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

# =========================================================
# START OF FIX: Define an async function for bot operations
# =========================================================

# The Client initialization and usage must be inside an async function
async def main():
    # Initialize the client inside the async function
    colab_bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
    
    # Optional: Attach handlers here if they are defined elsewhere
    # e.g., colab_bot.add_handler(...) 
    
    # Start the bot
    print("Starting Bot....")
    async with colab_bot:
        print("Bot is running. Press Ctrl+C to stop.")
        # This keeps the bot active and listening for updates
        await colab_bot.idle() 
        

# =========================================================
# END OF FIX: Run the async function only when the script is executed
# =========================================================

# This block ensures the asyncio loop is correctly started
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot stopped by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
