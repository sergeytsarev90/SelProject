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
    driver.get("http://localhost/litecart/en/")

    element = driver.find_element_by_xpath('//*[@id="box-campaigns"]/div/ul/li/a[1]')
    name_main = driver.find_element_by_xpath('//*[@id="box-campaigns"]/div/ul/li/a[1]/div[2]').text
    price_normal_main = driver.find_element_by_xpath('//*[@id="box-campaigns"]/div/ul/li/a[1]/div[4]/s').text
    price_discount_main = driver.find_element_by_xpath('//*[@id="box-campaigns"]/div/ul/li/a[1]/div[4]/strong').text
    color_price_normal_main = driver.find_element_by_xpath('//*[@id="box-campaigns"]/div/ul/li/a[1]/div[4]/s').value_of_css_property('color')
    color_price_discount_main = driver.find_element_by_xpath('//*[@id="box-campaigns"]/div/ul/li/a[1]/div[4]/strong').value_of_css_property('color')
    font_weight_price_discount_main = driver.find_element_by_xpath('//*[@id="box-campaigns"]/div/ul/li/a[1]/div[4]/strong').value_of_css_property('font-weight')
    font_size_price_normal_main = driver.find_element_by_xpath('//*[@id="box-campaigns"]/div/ul/li/a[1]/div[4]/s').value_of_css_property('font-size')
    font_size_price_discount_main = driver.find_element_by_xpath('//*[@id="box-campaigns"]/div/ul/li/a[1]/div[4]/strong').value_of_css_property('font-size')


    element.click()
    name_second = driver.find_element_by_xpath('//*[@id="box-product"]/div[1]/h1').text
    price_normal_second = driver.find_element_by_xpath('//*[@id="box-product"]/div[2]/div[2]/div[2]/s').text
    price_discount_second = driver.find_element_by_xpath('//*[@id="box-product"]/div[2]/div[2]/div[2]/strong').text
    color_price_normal_second = driver.find_element_by_xpath('//*[@id="box-product"]/div[2]/div[2]/div[2]/s').value_of_css_property('color')
    color_price_discount_second = driver.find_element_by_xpath('//*[@id="box-product"]/div[2]/div[2]/div[2]/strong').value_of_css_property('color')
    font_weight_price_discount_second = driver.find_element_by_xpath('//*[@id="box-product"]/div[2]/div[2]/div[2]/strong').value_of_css_property('font-weight')
    font_size_price_normal_second = driver.find_element_by_xpath('//*[@id="box-product"]/div[2]/div[2]/div[2]/s').value_of_css_property('font-size')
    font_size_price_discount_second = driver.find_element_by_xpath('//*[@id="box-product"]/div[2]/div[2]/div[2]/strong').value_of_css_property('font-size')

    if(name_main==name_second):
        print("Имена товаров совпадают")
    else:
        print("Имена товаров не совпадают")

    if(price_discount_main==price_discount_second):
        print("Имена товаров совпадают")
    else:
        print("Имена товаров не совпадают")

    if (price_normal_main == price_normal_second):
        print("Имена товаров совпадают")
    else:
        print("Имена товаров не совпадают")

    if(color_price_normal_main==(0,0,0,1)):
        print("Имена товаров совпадают")
    else:
        print("Имена товаров не совпадают")



    pass

