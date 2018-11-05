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


def are_elements_present(element, args):
    return len(element.find_elements_by_css_selector(args)) == 1

def test_example(driver):
    driver.get("http://localhost/litecart/en/")

    elements = driver.find_elements_by_css_selector('.product')

    for element in elements:
        if are_elements_present(element,'.sticker'):
            print(element.find_element_by_css_selector('.sticker').text + ' Элемент найден')


