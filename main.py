import os
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from db import commands
from config.settings import driver
import fille_get
import file_data


fille_get.try_api()
file_data.add_data()

base_dir = os.path.dirname(os.path.realpath(__file__))

time.sleep(20)
"""
/html/body/div[4]/div[3]/div/div/div/div[6]/div/div/div/div[2]/div/table/tbody/tr[3]/td[2]/a
//*[@id="customer-phone"]/td[2]/a
"""

def whatsapp_render(contact, data):
    try:

        driver.get(contact)
        time.sleep(20)
        message_content = "Здорова! \n"+str(data[1])

        inp_xpath = '//div[@contenteditable="true"][@data-tab="10"]'
        input_box = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, inp_xpath)))
        input_box.send_keys(message_content + Keys.ENTER)

        attachment_box = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                # (By.XPATH, '//div[@title = "Attach"]'))
                (By.XPATH, '//div[@title = "Прикрепить"]'))
        )
        attachment_box.click()
        time.sleep(1)
        image_box = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        # image_box = WebDriverWait(driver, 5).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH,
        #          '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'))
        # )
        file_path1 = os.path.join(base_dir, 'ironman.jpg')
        # file_path2 = os.path.join(base_dir, 'spiderman.jpg')
        # file_path3 = os.path.join(base_dir, 'joker.jpg')
        # for i in file_list:
        #     image_box.send_keys(i)

        image_box.send_keys(file_path1)
        time.sleep(3)

        # send_button = WebDriverWait(driver, 5).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, '//span[@data-icon="send"]')))

        send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
        # send_button = WebDriverWait(driver, 5).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, '//span[@data-icon="send"]')))
        send_button.click()
        time.sleep(2)
    except IndexError as e:
        driver.quit()
        print(e)


def messenger(url, data):
    try:
        contacts = ["706946757"]
        for n in data:
            for i in contacts:
                contact = url+i
                whatsapp_render(contact, n)
    except Exception as e:
        print(e)
        os._exit(0)


messenger("https://web.whatsapp.com/send?phone=", commands.get_data_whatsapp())
driver.quit()