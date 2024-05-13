# modules required
import os
import winsound
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# telegram credentials (please refer to telegram documentation: https://core.telegram.org/bots/features#creating-a-new-bot)
telegram_enabled = True
telegram_token = "0"
telegram_chatid = "0"

# check if telegram credentials are provided
if (telegram_token == "0") or (telegram_chatid == "0"):

    telegram_enabled = False
    print("- Telegram credentials not provided. Messages will only be printed in the prompt.")

else:

    print("Telegram configuration: Success!")

# check if firefox web driver is placed in the project folder
if not os.path.isfile("geckodriver.exe"):

    print("- Firefox web driver not found in project folder.")
    print("Quitting...")
    quit()

else:

    print("Firefox web driver configuration: Success!")

# access website
driver = webdriver.Firefox()
vfs_website = driver.get("https://visa.vfsglobal.com/rus/ru/nld/login")
print("Opening VFS website...")

while True:

    input("Log in manually and click 'Записаться на прием' in the following page.\nThen come back here and type ENTER: ")
    break

sleep(1)
print("Bot has started. See updates below.")

# initial fill of field 'Выберите свой визовый центр'
driver.find_element(By.ID, "mat-select-value-1").click()
sleep(1)
ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
sleep(1)
ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
sleep(1)
ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
sleep(1)
ActionChains(driver).send_keys(Keys.ENTER).perform()
sleep(10)

# initial fill of field 'Выберите категорию записи'
driver.find_element(By.ID, "mat-select-value-5").click()
sleep(1)
ActionChains(driver).send_keys(Keys.ENTER).perform()
sleep(10)

# initial fill of field 'Выберите подкатегорию'
driver.find_element(By.ID, "mat-select-value-3").click()                        
sleep(1)
ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
sleep(1)
ActionChains(driver).send_keys(Keys.ENTER).perform()
sleep(10)

def no_updates_msg():

    if telegram_enabled:
                
        url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
        post_data = {"chat_id": telegram_chatid, "parse_mode": "Markdown", "text": "No available slots. Keep trying."}
        requests.post(url, data=post_data)

def good_news_msg():

    if telegram_enabled:
                
        url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
        post_data = {"chat_id": telegram_chatid, "parse_mode": "Markdown", "text": "There may be slots available. Try to make an appointment now."}
        requests.post(url, data=post_data)

while True:

    # try to spot error message
    try:

        error_msg = driver.find_element(By.XPATH, "/html/body/app-root/div/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[4]/div")

        if "Приносим извинения" in error_msg.text: # means there are no slots available

            print("No available slots. Keep trying.")
            #no_updates_msg()

            # change selection in field 'Выберите свой визовый центр'
            driver.find_element(By.ID, "mat-select-value-1").click()            
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
            
            # change selection in field 'Выберите категорию записи'
            driver.find_element(By.ID, "mat-select-value-5").click()
            sleep(1)
            ActionChains(driver).send_keys(Keys.ENTER).perform()
            sleep(10)

            # change selection in field 'Выберите подкатегорию'
            driver.find_element(By.ID, "mat-select-value-3").click()
            sleep(1)
            ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
            sleep(1)
            ActionChains(driver).send_keys(Keys.ENTER).perform()
            sleep(10)

            continue

        else: # means there may be slots available

            winsound.Beep(440, 1000)
            print("There may be slots available. Try to make an appointment now.")
            good_news_msg()

            break

    except KeyboardInterrupt:

        print("Script interrupted.")

        break

    except: # means there may be slots available
        
        winsound.Beep(440, 1000)
        print("There may be slots available. Try to make an appointment now.")
        good_news_msg()
        
        break