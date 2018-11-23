from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {
 'browser': 'Chrome',
 'browser_version': '70.0',
 'os': 'Windows',
 'os_version': '10',
 'resolution': '1024x768',
 'browserstack.debug': 'true'
}

driver = webdriver.Chrome(desired_capabilities={"proxy": {"proxyType": "MANUAL", "httpProxy": "localhost:8080"}})

#driver = webdriver.Remote(
#    command_executor='http://sergei202:zzHAzhshMjRsEY8ChNHf@hub.browserstack.com:80/wd/hub', desired_capabilities=desired_cap)

driver.get("http://www.ya.ru")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("BrowserStack")
elem.submit()
print(driver.title)
driver.quit()