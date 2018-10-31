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

def is_element_present(driver, *args):
  try:
    driver.find_element(*args)
    return True
  except NoSuchElementException:
    return False



def test_example(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is("My Store"))
    #elements = driver.find_elements_by_id('app-')
    #print(elements)

    elements = driver.find_elements(By.CSS_SELECTOR,'li')
    # app- > a > span.name

    # doc-logotype > a > span
    # app- > a > span.name

    #'app-.name:contains("Catalog")'

    for element in elements:
        element.click()
        #driver.find_element_by_id('doc-logotype').click()
    pass
