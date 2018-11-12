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
    driver.get("http://localhost:8080/litecart/en/")

    name_main = driver.find_element_by_xpath("//div[@id='box-campaigns']//div[@class='name']").text

    xpath_normal_main = "//div[@id='box-campaigns']//s[@class='regular-price']"

    price_normal_main = driver.find_element_by_xpath(xpath_normal_main).text
    color_price_normal_main = driver.find_element_by_xpath(xpath_normal_main).value_of_css_property('color')
    font_size_price_normal_main = driver.find_element_by_xpath(xpath_normal_main).value_of_css_property('font-size')
    line_through_price_normal_main = driver.find_element_by_xpath(xpath_normal_main).value_of_css_property('text-decoration')

    xpath_discount_main = "//div[@id='box-campaigns']//strong[@class='campaign-price']"

    price_discount_main = driver.find_element_by_xpath(xpath_discount_main).text
    color_price_discount_main = driver.find_element_by_xpath(xpath_discount_main).value_of_css_property('color')
    font_weight_price_discount_main = driver.find_element_by_xpath(xpath_discount_main).value_of_css_property('font-weight')
    font_size_price_discount_main = driver.find_element_by_xpath(xpath_discount_main).value_of_css_property('font-size')

    driver.find_element_by_xpath("//div[@id='box-campaigns']//img[@class='image']").click()

    name_second = driver.find_element_by_xpath("//h1[@class='title']").text

    xpath_normal_second = "//s[@class='regular-price']"

    price_normal_second = driver.find_element_by_xpath(xpath_normal_second).text
    color_price_normal_second = driver.find_element_by_xpath(xpath_normal_second).value_of_css_property('color')
    font_size_price_normal_second = driver.find_element_by_xpath(xpath_normal_second).value_of_css_property('font-size')
    line_through_price_normal_second = driver.find_element_by_xpath(xpath_normal_second).value_of_css_property('text-decoration')

    xpath_discount_second = "//strong[@class='campaign-price']"

    price_discount_second = driver.find_element_by_xpath(xpath_discount_second).text
    color_price_discount_second = driver.find_element_by_xpath(xpath_discount_second).value_of_css_property('color')
    font_weight_price_discount_second = driver.find_element_by_xpath(xpath_discount_second).value_of_css_property('font-weight')
    font_size_price_discount_second = driver.find_element_by_xpath(xpath_discount_second).value_of_css_property('font-size')

    if(name_main==name_second):
        print("Имена товаров совпадают")
    else:
        print("Имена товаров не совпадают")

    if(price_discount_main==price_discount_second):
        print("Цены акционные товаров совпадают")
    else:
        print("Цены акционные товаров не совпадают")

    if (price_normal_main == price_normal_second):
        print("Цены обычные товаров совпадают")
    else:
        print("Цены обычные товаров не совпадают")

    if (str(line_through_price_normal_main).__contains__("line-through")):
        print("Цена товара обычная на главной странице зачеркнута")
    else:
        print("Цена товара обычная на главной странице не зачеркнута")

    if (str(line_through_price_normal_second).__contains__("line-through")):
        print("Цена товара обычная на странице товара зачеркнута")
    else:
        print("Цена товара обычная на странице товара не зачеркнута")

    if (str(font_weight_price_discount_main).__contains__("700")):
        print("Цена товара акционная на главной товара жирная")
    else:
        print("Цена товара акционная на главной товара не жирная")

    if (str(font_weight_price_discount_second).__contains__("700")):
        print("Цена товара акционная на странице товара жирная")
    else:
        print("Цена товара акционная на странице товара не жирная")

    if (font_size_price_discount_second>font_size_price_normal_second):
        print("Размер шрифта акционной цены больше обычной цены на странице товара")
    else:
        print("Размер шрифта акционной цены меньше обычной цены на странице товара")

    if (font_size_price_discount_main>font_size_price_normal_main):
        print("Размер шрифта акционной цены больше обычной цены на главной странице ")
    else:
        print("Размер шрифта акционной цены меньше обычной цены на главной странице ")

    #color_price_discount_main


    pass

