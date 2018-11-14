import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost:8080/litecart/en/")
    driver.find_element_by_xpath("//a[contains(text(),'New customers click here')]").click()
    driver.find_element_by_xpath("//input[@name='firstname']").send_keys('Ivan')
    driver.find_element_by_xpath("//input[@name='lastname']").send_keys('Ivanov')
    driver.find_element_by_xpath("//input[@name='address1']").send_keys('st. Shkolnaya 13')
    driver.find_element_by_xpath("//input[@name='postcode']").send_keys('12345')
    driver.find_element_by_xpath("//input[@name='city']").send_keys('Moscow')

    country = Select(driver.find_element_by_xpath("//select[@name='country_code']"))
    country.select_by_visible_text('United States')

    zone = driver.find_element_by_xpath("//select[@name='zone_code']")
    driver.execute_script("arguments[0].style.opacity = 1", zone)
    #driver.implicitly_wait(10)
    wait = WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located((By.XPATH,"//option[contains(text(),'Alabama')]")))

    zone_select = Select(zone)
    zone_select.select_by_visible_text('Idaho')

    email = 'test'+str(random.randint(1,100))+'@test.com'

    driver.find_element_by_xpath("//input[@name='email']").send_keys(email)
    driver.find_element_by_xpath("//input[@placeholder='+1']").send_keys('5458412')

    driver.find_element_by_xpath("//input[@name='password']").send_keys('1')
    driver.find_element_by_xpath("//input[@name='confirmed_password']").send_keys('1')

    driver.find_element_by_xpath("//button[@value='Create Account']").click()

    driver.find_element_by_xpath("//div[@id='box-account'] //a[contains(text(),'Logout')]").click()

    driver.find_element_by_xpath("//input[@name='email']").send_keys(email)
    driver.find_element_by_xpath("//input[@name='password']").send_keys('1')
    driver.find_element_by_xpath("//button[@value='Login']").click()

    driver.find_element_by_xpath("//div[@id='box-account'] //a[contains(text(),'Logout')]").click()



    pass




