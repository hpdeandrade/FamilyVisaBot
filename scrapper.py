# import libraries
import os
import winsound
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# telegram credentials (replace 0 by your token & chatid)
telegram_enabled = True
telegram_token = 0
telegram_chatid = 0

print("Bot started...")

# check if telegram credentials are provided
if not (telegram_token or telegram_chatid):
    telegram_enabled = False
    print("- Alert! No Telegram credentials were provided. Messages will only be printed in the prompt.")

# check if chromedriver.exe is placed in the project folder
if not os.path.isfile("chromedriver.exe"): 
    print("- Error! chromedriver.exe not found in project folder.")
    print("Quitting...")
    quit()

# access website
driver = webdriver.Chrome()
vfs_website = driver.get("https://visa.vfsglobal.com/rus/ru/nld/login")

print("Website successfully opened!")

# sleep for 2 minutes so the user can fill in credentials manually and proceed to the next page
sleep(120)

# first round of inputs
driver.find_element(By.ID, "mat-select-value-1").click()                        # fill in field #1 (Выберите свой визовый центр)
sleep(1)
ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
sleep(1)
ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
sleep(1)
ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
sleep(1)
ActionChains(driver).send_keys(Keys.ENTER).perform()
sleep(10)

driver.find_element(By.ID, "mat-select-value-3").click()                        # fill in field #2 (Выберите категорию записи)
sleep(1)
ActionChains(driver).send_keys(Keys.ENTER).perform()
sleep(10)

while True:

    # spot error message
    try:
        error_msg = driver.find_element(By.XPATH, "/html/body/app-root/div/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[4]/div")

        if "Приносим извинения" in error_msg.text:                              # ---> this scenario means the error message box remains there unchanged
            print("No good news yet...")
            driver.find_element(By.ID, "mat-select-value-1").click()            # change selection in field #1 (Выберите свой визовый центр)
            sleep(1)
            ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
            sleep(1)
            ActionChains(driver).send_keys(Keys.ENTER).perform()
            sleep(10)
            driver.find_element(By.ID, "mat-select-value-1").click()
            sleep(1)
            ActionChains(driver).send_keys(Keys.ARROW_UP).perform()
            sleep(1)
            ActionChains(driver).send_keys(Keys.ENTER).perform()
            sleep(10)

            driver.find_element(By.ID, "mat-select-value-3").click()            # change selection in field #2 (Выберите категорию записи)
            sleep(1)
            ActionChains(driver).send_keys(Keys.ENTER).perform()
            sleep(10)

            continue

        else:                                                                   # ---> this scenario means the text in the error message box has changed (no longer contains the words "Приносим извинения" in the beginning)
            print("There may be some good news...")
            winsound.Beep(440, 1000)

            # send telegram message
            if telegram_enabled:
                url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
                post_data = {"chat_id": telegram_chatid, "parse_mode": "Markdown", "text": "There may be some good news about the visa )"}
                requests.post(url, data=post_data)

            break

    except:                                                                     # ---> this scenario means the error message box is no longer there
        print("There may be some good news...")                                 
        winsound.Beep(440, 1000)

        # send telegram message
        if telegram_enabled:
            url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
            post_data = {"chat_id": telegram_chatid, "parse_mode": "Markdown", "text": "There may be some good news about the visa :)"}
            requests.post(url, data=post_data)

        break
