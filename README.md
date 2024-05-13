# familyvisabot
![familyvisabot]("https://github.com/hpdeandrade/familyvisabot/icon.png")

Get notifications to your Telegram group via the Telegram bot about potential timeslots available in VFS Global Moscow. For other locations, the code must be adjusted. This bot written in Python language.

To run this bot you require to install Python and Firefox web driver.

This bot has been tested with the following modules:

* Python 3.12.3 (download [here](https://www.python.org/downloads/release/python-3123/))
* Firefox web driver v0.34.0 (download [here](https://github.com/mozilla/geckodriver/releases))
* Windows 10/11
  
**Step 1**: Download and install Python.

**Step 2**: Download Firefox web driver (geckodriver). Once downloaded, move the executable file to the familyvisabot project folder.

**Step 3**: Install bot dependencies from `requirements.txt` file by running the command `pip install -r requirements.txt`.

**Step 4**: Set up a telegram bot and open file `script.py`. Replace the value for variables telegram_token and telegram_chatid with bot token and group chat id respectively. Please refer to [Telegram documentation on how to create a bot](https://core.telegram.org/bots/features#creating-a-new-bot).

**Final step**: Run the script by executing `script.py` and follow the instructions displayed in the command prompt.