import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def alphabet_check(abc_val):
    a=0
    abc_val = [value for value in abc_val if value]
    abc_val_sort = sorted(abc_val)
    print(abc_val)

    while a < abc_val.__len__():
        if(abc_val[a] != abc_val_sort[a]):
            return False
        a+=1
    return True

def is_element_present(driver, *args):
  try:
    driver.find_element(*args)
    return True
  except NoSuchElementException:
    return False

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example_country(driver):
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
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


    if(alphabet_check(countries)):
        print("Названия в странах расположены по алфавиту")
    else:
        print("Названия в странах расположены не по алфавиту")


    i = 0
    count1 = elements.__len__()
    while i<count1:
        elements = driver.find_elements_by_xpath("//*[contains(@class,'row')]")

        if (zone_countries[a] == elements[i].find_element_by_css_selector("td:nth-child(5)").text):
            zones = []
            elements[i].find_element_by_xpath("// a[contains(text(),'" + zone_countries[a] + "')]").click()
            elements_into = driver.find_elements_by_xpath('//*[@id="table-zones"]/tbody/tr[position()>1]')

            for element in elements_into:
                zones.append(element.find_element_by_css_selector('td:nth-child(3)').text)

            if (alphabet_check(zones)):
                print("Названия в зонах у "+zone_countries[a]+" расположены по алфавиту")
            else:
                print("Названия в зонах у " + zone_countries[a] + " расположены не по алфавиту")

            a += 1
            driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")

            if a==zone_countries.__len__():
                break
        i += 1
    a=0

def test_example_zone(driver):
    driver.get("http://localhost:8080/litecart/admin/?app=geo_zones&doc=geo_zones")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    elements = driver.find_elements_by_xpath("//*[contains(@class,'row')]")

    zones = []
    zone_countries = []
    i=0
    count1 = elements.__len__()

    while i<count1:
        zone_countries.append(elements[i].find_element_by_css_selector('[href]').text)
        elements[i].find_element_by_css_selector('[href]').click()

        elements_zone = driver.find_elements_by_xpath("//table[@id='table-zones']//tbody//tr[position() > 1]")

        for element in elements_zone:
            if(is_element_present(element,By.CSS_SELECTOR,'td:nth-child(3) > select:nth-child(1) > option[selected="selected"]')):
                zones.append(element.find_element_by_css_selector('td:nth-child(3) > select:nth-child(1) > option[selected="selected"]').text)

        if (alphabet_check(zones)):
            print("Названия в зонах у " + zone_countries[i] + " расположены по алфавиту")
        else:
            print("Названия в зонах у " + zone_countries[i] + " расположены не по алфавиту")
        pass

        driver.get("http://localhost:8080/litecart/admin/?app=geo_zones&doc=geo_zones")
        elements = driver.find_elements_by_xpath("//*[contains(@class,'row')]")
        i+=1
        zones = []


    pass
