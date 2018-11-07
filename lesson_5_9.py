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


def test_example(driver):
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    #WebDriverWait(driver, 10).until(EC.title_is("My Store"))

    #elements = driver.find_elements_by_css_selector('[name=countries_form]')
    elements = driver.find_elements_by_xpath("//*[contains(@class,'row')]")

    countries = []

    zone_countries = []


    for element in elements:
        countries.append(element.find_element_by_css_selector('[href]').text)
        if(int(element.find_element_by_css_selector("td:nth-child(6)").text) > 0):
            zone_countries = element.find_element_by_css_selector("td:nth-child(4)")


    countries_1 = sorted(countries)
    print(zone_countries)
    a=0


    element.find_element_by_css_selector('td:nth-child(4)')

    while a < countries.__len__():
        if(countries[a] != countries_1[a]):
            print(countries[a], ' страна расположена не по алфавиту')
        a+=1






    pass

