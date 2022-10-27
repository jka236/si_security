from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def sqlinjection(host):
    timeToSleep=1
    #create a new Firefox session
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    #driver.implicitly_wait(30)
    driver.maximize_window()
    print("Success")
    
sqlinjection("http://google.com")
