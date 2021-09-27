from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r'C:\Users\glzha\Desktop\Git\小脚本\chromedriver.exe')

driver.get('http://timeterminal/')

name = driver.find_element_by_id("Ident1")
name.send_keys('Zhang')

sleep(2)

password = driver.find_element_by_id("Ident2")
password.send_keys('7500478')

sleep(2)

coming = driver.find_element_by_id('C1')
coming.click()
print('已打卡登录')

sleep(2)

going = driver.find_element_by_id('C2')
going.click()
print('已打卡下班')

# sleep(1)
# info = driver.find_element_by_id('C5')
# info.click()