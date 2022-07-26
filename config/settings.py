import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# options = webdriver.ChromeOptions()
options.headless = False
# options.add_argument("--window-size=1920,1200")

#Local\Google\Chrome\User Data
options.add_argument("user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
# options.add_argument("user-data-dir=~/Library/Application Support/Google/Chrome/Default")
dir_path = os.path.dirname(os.path.realpath(__file__))
DRIVER_PATH = os.path.join(dir_path, 'chromedriver')
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.minimize_window()
