import bot
import os
from dotenv import load_dotenv
import bot
import logger
def main():

    load_dotenv(dotenv_path="config")

    bot.bot_instance.run(os.getenv("TOKEN"))

if __name__ == "__main__":
    main()



