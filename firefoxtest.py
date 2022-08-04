
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

#service  = Service("C:\Users\AbdullahHaybeDAAT\AppData\Local\Programs\Python\geckodriver.exe")
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(service = Service(executable_path=GeckoDriverManager().install()),options=options)
username = "208"
password = "IVSKUZ2vXr"
url = "https://vangils.my3cx.nl/#/login"
newurl = "https://vangils.my3cx.nl/api/CallLog?dateRangeType=LastNinetyDays&numberOfRows=500"
driver.get(url)
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id=\"content\"]/login-component/div/div/form/div/div[1]/input").send_keys(username)
driver.find_element(By.XPATH,"//*[@id=\"content\"]/login-component/div/div/form/div/div[2]/input").send_keys(password)
driver.find_element(By.XPATH,"//*[@id=\"content\"]/login-component/div/div/form/button").click()

time.sleep(1)
data = driver.get_cookies()
pd = pd.DataFrame(data)
print(pd)
