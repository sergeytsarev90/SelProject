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
    driver.get("http://localhost/litecart/en/")

    elements = driver.find_elements_by_css_selector('li.product.column.shadow.hover-light')

    for element in elements:
        if is_element_present(element,'div.image-wrapper'):
            print(element.find_element_by_css_selector('div.image-wrapper').text + ' Элемент найден')


