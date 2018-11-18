import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()


    driver.find_element_by_xpath("//ul[@id='box-apps-menu']//li[2]//a[1]//span[2]").click()
    driver.find_element_by_xpath("//td[@id='content']//div//a[2]").click()


    driver.find_element_by_xpath("//td//label[1]").click()
    name = 'ducky duck'
    driver.find_element_by_xpath("//input[@name='name[en]']").send_keys(name)
    driver.find_element_by_xpath("//input[@name='code']").send_keys('12345')
    driver.find_element_by_xpath("//div[@class='input-wrapper']//input[@value='1']").click()

    сategory = Select(driver.find_element_by_xpath("//select[@name='default_category_id']"))
    сategory.select_by_visible_text('Rubber Ducks')

    driver.find_element_by_xpath("//input[@value='1-3']").click()
    driver.find_element_by_xpath("//div[@id='tab-general']//input[@value='0.00']").send_keys('12345')

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'duck.jpg')
    driver.find_element_by_xpath('//*[@id="tab-general"]/table/tbody/tr[9]/td/table/tbody/tr[1]/td/input').send_keys(filename)

    driver.find_element_by_xpath("//input[@name='date_valid_from']").send_keys('01.10.2018')
    driver.find_element_by_xpath("//input[@name='date_valid_to']").send_keys('12.12.2018')


    driver.find_element_by_xpath("//a[contains(text(),'Information')]").click()

    manufacturer = Select(driver.find_element_by_xpath("//select[@name='manufacturer_id']"))
    manufacturer.select_by_visible_text('ACME Corp.')

    driver.find_element_by_xpath("//input[@name='keywords']").send_keys('duck')
    driver.find_element_by_xpath("//input[@name='short_description[en]']").send_keys('Best duck')
    driver.find_element_by_xpath("//div[@class='trumbowyg-editor']").send_keys('Best duck in the world')
    driver.find_element_by_xpath("//input[@name='head_title[en]']").send_keys('Best duck')
    driver.find_element_by_xpath("//input[@name='meta_description[en]']").send_keys('Best')

    driver.find_element_by_xpath("//a[contains(text(),'Prices')]").click()

    driver.find_element_by_xpath("//input[@name='purchase_price']").send_keys('duck')

    manufacturer = Select(driver.find_element_by_xpath("//select[@name='purchase_price_currency_code']"))
    manufacturer.select_by_visible_text('US Dollars')

    tax = Select(driver.find_element_by_xpath("//select[@name='tax_class_id']"))
    tax.select_by_visible_text('-- Select --')

    driver.find_element_by_xpath("//input[@name='prices[USD]']").send_keys('30')
    driver.find_element_by_xpath("//input[@name='prices[EUR]']").send_keys('35')

    driver.find_element_by_xpath("//button[@value='Save']").click()

    driver.find_element_by_xpath("//ul[@id='box-apps-menu']//li[2]//a[1]//span[2]").click()

    driver.find_element_by_xpath("//a[contains(text(),'Rubber Ducks')]").click()

    elements = driver.find_elements_by_xpath("//tbody//tr[@class = 'row']//td[3]")
    for element in elements:
        name_check = element.text
        if name == name_check:
            print('Товар занесен')
            break

    pass



