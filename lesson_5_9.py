import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def alphabet_check(abc_val):
    a=0
    abc_val_sort = sorted(abc_val)
    print(abc_val)

    while a < abc_val.__len__():
        if(abc_val[a] != abc_val_sort[a]):
            return False
        a+=1
    return True

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost:8080/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    elements = driver.find_elements_by_xpath("//*[contains(@class,'row')]")

    countries = []

    zone_countries = []
    a = 0

    for element in elements:
        countries.append(element.find_element_by_css_selector('[href]').text)
        if(int(element.find_element_by_css_selector("td:nth-child(6)").text) > 0):
            zone_countries.append(element.find_element_by_css_selector("td:nth-child(5)").text)

    # for element in elements:
    #     if(zone_countries[0]==element.find_element_by_css_selector("td:nth-child(5)").text):
    #         element.find_element_by_xpath("// a[contains(text(),'"+zone_countries[0]+"')]").click()
    #         a+=1

    alphabet_check(countries)

    i = 0
    zones = []

    # content > form > table > tbody > tr:nth-child(2) > td:nth-child(5) > a
    # table-zones > tbody > tr:nth-child(2) > td:nth-child(3)

    count1 = elements.__len__()
    while i<count1:
        elements = driver.find_elements_by_xpath("//*[contains(@class,'row')]")
        if (zone_countries[a] == elements[i].find_element_by_css_selector("td:nth-child(5)").text):
            elements[i].find_element_by_xpath("// a[contains(text(),'" + zone_countries[a] + "')]").click()
            elements_into = driver.find_elements_by_xpath('//*[@id="table-zones"]/tbody/tr[position()>1]')
            for element in elements_into:
                zones.append(element.find_element_by_css_selector('td:nth-child(3)').text)
            a += 1
            driver.get("http://localhost:8080/litecart/admin/?app=countries&doc=countries")
            if a==zone_countries.__len__():
                break
        i += 1

    a=0
    #element.find_element_by_css_selector('td:nth-child(4)')

    pass

