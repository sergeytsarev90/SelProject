import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities.CHROME
caps['loggingPrefs'] = {'performance': 'ALL'}

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(desired_capabilities=caps)
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    elements = driver.find_elements_by_xpath("//tr/td[3]/a[contains(text(), 'Duck')]")
    i=0
    while i<elements.__len__():
        driver.find_element_by_xpath("//tr[" + str(5+i) + "]/td[3]/a[contains(text(), 'Duck')]").click()
        for l in driver.get_log("performance"):
            print(l)
        driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
        i+=1


