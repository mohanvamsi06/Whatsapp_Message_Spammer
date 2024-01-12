#spams msgs using whatsapp web from microsoft edge
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import time
from tqdm import tqdm

username = 'Vamsi'
message = 'hlo'
x = 20

browser = webdriver.Edge()
print("Browser tab opened")

try:
    browser.get('https://web.whatsapp.com/')
    print("Waiting for Login")

    text_area = WebDriverWait(browser, 60).until(
			expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[4]/div/div[1]/div/div[2]/div[2]/div/div[1]'))
    )
    print("Login Successfull")
    text_area.click()
    text_area.send_keys(username)
    text_area.send_keys(Keys.ENTER)
    print("Sending messages")

    i = 0

    for i in tqdm(range(0, x), unit='iteration'):
        actions = ActionChains(browser)
        actions.send_keys(message)
        actions.perform()
        actions.send_keys(Keys.ENTER)
        actions.perform()
        if (i == x-1):
            print("Messages Sent Successfully")
            
    time.sleep(2)
    print("Loging Out")
    browser.find_element("xpath",'/html/body/div[1]/div/div/div[4]/header/div[2]/div/span/div[5]/div').click()
    time.sleep(1)
    c=0
    while(c<6):
        actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()
        time.sleep(0.2)
        c += 1
        if (c==6):
            actions.send_keys(Keys.ENTER)
            actions.perform()
            print("Trying to Logout")
            browser.find_element("xpath",'/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div[3]/div/button[2]').click()
            print("Logout Successfull")
            break
                        
        time.sleep(10)
        print("Closing Browser")
        browser.quit()

except Exception as err:
    print(err)
    browser.quit()
