import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def is_element_present(element, args):
  try:
    element.find_element_by_css_selector(args)
    return True
  except NoSuchElementException:
    return False


def test_example(driver):
    driver.get("http://localhost:8080/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    #WebDriverWait(driver, 10).until(EC.title_is("My Store"))

    elements = driver.find_elements_by_xpath('//*[contains(@class,''row'')]')
    for element in elements:
        temp = element.find_element_by_css_selector('[href]').text
        print(temp)




    pass

