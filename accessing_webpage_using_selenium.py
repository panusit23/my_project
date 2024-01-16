#Accessing_MDR_Info

from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.edge.service import Service
#from selenium.webdriver.ie.service import Service
from selenium.webdriver.common.by import By
import time
import pprint

#driver_path = r'C:\Users\201014501\Desktop\Official 818\4_818_analyze\Webdriver\chromedriver-win64\chromedriver-win64\chromedriver.exe'
driver_path = r'C:\Users\201014501\Desktop\Official 818\4_818_analyze\Webdriver\geckodriver-v0.33.0-win64\geckodriver.exe'
#driver_path = r'C:\Users\201014501\Desktop\Official 818\4_818_analyze\Webdriver\edgedriver_win64\msedgedriver.exe'
#driver_path = r'\Users\201014501\Desktop\Official 818\4_818_analyze\Webdriver\IEDriverServer_x64_4.11.0\IEDriverServer.exe'
service = Service(executable_path=driver_path)

#driver = webdriver.Chrome(service=service)
driver = webdriver.Firefox(service=service)
#driver = webdriver.Edge(service=service)
#driver = webdriver.Ie(service=service)


url_path = r"https://x.x.x.x"
driver.get(url_path)

username_field = driver.find_element(by=By.ID, value="Username")
password_field = driver.find_element(by=By.ID, value="Password")
login_field = driver.find_element(by=By.NAME, value="Submit")

username_field.send_keys("admin")
time.sleep(1)
password_field.send_keys("xxxxxxxx")
time.sleep(1)
login_field.click()
time.sleep(1)


'''
web_element = driver.find_element(by=By.ID, value="")
find_tag_p = web_element.find_elements(by=By.TAG_NAME, value="p")
print(type(find_tag_p))


did_not_content_advance_button = driver.find_element(by=By.ID, value="advanceButton")
did_not_content_advance_button.click()


'''

print("-"*20)
print('!!!!!Done!!!!!')

#time.sleep(15)
#driver.quit()