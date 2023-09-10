# FamilyVisaBot
Get notifications to your Telegram group via the Telegram bot about potential timeslots available in VFS Global Moscow. This bot written in Python language.

To run this bot you require to install Python and Google Chrome Driver

This bot has been tested with the following modules:
* Python 3.10.5
* Google Chrome Driver v.116
* Windows 10
  
**Step 1**: Download and install Python 3.10.5 from [this website](https://www.python.org/downloads/release/python-3105/).

**Step 2**: Download the chromedriver.exe compatible with your Chrome version. Check the executable file [here](https://googlechromelabs.github.io/chrome-for-testing/#stable). Once you download Chrome Driver, please chromedriver.exe in the FamilyVisaBot project folder.

**Step 3**: Install bot dependencies from requirements.txt file by running the command `pip install -r requirements.txt`

**Step 4**: Set up a telegram bot and open file scrapper.py. Replace the value for variables telegram_token and telegram_chatid with bot token and group chat id respectively. Please refer to [Telegram documentation how to create a bot](https://core.telegram.org/bots/features#creating-a-new-bot)

**Final step**: Run the script by executing scrapper.py
