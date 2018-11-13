import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select



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
    #driver.find_element_by_xpath("// option[contains(text(), 'California')]").click()
    zone = Select(driver.find_element_by_xpath("/// option[contains(text(), 'California')]"))
    zone.select_by_visible_text('California')
    pass




