from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')

sleep(3)

username = driver.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
username.send_keys("""Enter Email address""")

password = driver.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
password.send_keys("""Enter password""")

signin = driver.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
signin.click()
sleep(3)
notnow = driver.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/div/div/div/button')
notnow.click()
sleep(3)
againNotNow = driver.find_element_by_xpath(
    '/html/body/div[4]/div/div/div/div[3]/button[2]')
againNotNow.click()
sleep(3)
message = driver.find_element_by_xpath(
    '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')
message.click()
sleep(5)

direct = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button')
direct.click()
sleep(3)
search_user = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input')
search_user.send_keys('tannyable_')
sleep(5)


el=driver.find_elements_by_xpath("/html/body/div[4]/div/div/div[2]/div[2]/div[1]")[0]
el.click()

#user = driver.find_elements_by_class_name('-qQT3')
#user[0].click()
#action = webdriver.common.action_chains.ActionChains(driver)
#action.move_to_element_with_offset(el, 225, 179)
#action.click()

sleep(2)
selectUser = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]')
selectUser.click()
sleep(5)
textbox = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
for i in range(1000):
    textbox.send_keys('Kya chal la !!!!!')
    textbox.send_keys(Keys.ENTER)
