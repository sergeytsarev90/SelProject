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
    elements = driver.find_elements_by_id('app-')

    count1 = elements.__len__()

    i=0
    while i<count1:

        elements = driver.find_elements_by_id('app-')
        elements[i].click()

        if is_element_present(driver,By.CSS_SELECTOR,'h1'):
            print('Заголовок существует')

        i += 1
        elements_into = driver.find_elements_by_css_selector(".docs>li")
        count2 = elements_into.__len__()

        j = 0
        while j< count2:
            elements_into = driver.find_elements_by_css_selector(".docs>li")
            elements_into[j].click()
            j+=1
            if is_element_present(driver, By.CSS_SELECTOR, 'h1'):
                print('Заголовок существует')
