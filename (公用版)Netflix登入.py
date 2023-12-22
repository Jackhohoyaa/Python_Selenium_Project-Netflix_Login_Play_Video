from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as bs
import requests as rq
import time
options=Options()
options.chrome_executabel_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
driver=webdriver.Chrome(options=Options())
def connect(url):
    driver.get(url)
    driver.minimize_window()
def enter(account_name):
    account=driver.find_element(By.CSS_SELECTOR,"[autocomplete=email]")
    account.send_keys(account_name)
    driver.find_element(By.CSS_SELECTOR,"[type=submit]").click()
    time.sleep(2)
    driver.maximize_window()
def log_in(url,password_name):
    driver.get(url)
    password=driver.find_element(By.CSS_SELECTOR,"[type=password]")
    password.send_keys(password_name)
    driver.find_element(By.CSS_SELECTOR,"[data-uia=login-submit-button]").click()
    time.sleep(2)
def choose_user(url,user,name):
    driver.get(url)
    choose=driver.find_element(By.LINK_TEXT,"%s"%(user)).click()
    time.sleep(2)
def search_video(name):    
    driver.get("https://www.netflix.com/search?q=%s"%(name))
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(2)
def play_video():    
    rawlink=driver.find_elements(By.CSS_SELECTOR,"[role=link]")[0]
    link=rawlink.get_attribute("href")
    time.sleep(1)
    driver.get(link)
    
if __name__ == "__main__":
    enter_url="https://www.netflix.com/tw/"
    log_in_url="https://www.netflix.com/tw/login"
    browser_url="https://www.netflix.com/browse"
    connect(enter_url)
    account=input("請輸入帳號:")
    password=input("請輸入密碼:")
    user=input("請輸入使用者名稱:")
    name=input("請輸入片名:")
    enter(account)
    log_in(log_in_url,password)
    choose_user(browser_url,user,name)
    search_video(name)
    play_video()

