import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

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




def test_example(driver):
    i=1
    while i<4:

        driver.get("http://localhost:8080/litecart/en/")
        driver.find_element_by_xpath("//div[@id='box-most-popular']").click()

        if(is_element_present(driver,By.XPATH,"//td[@class='options']")):
            size = Select(driver.find_element_by_xpath("//select[@name='options[Size]']"))
            size.select_by_visible_text('Small')



        driver.find_element_by_xpath("//button[@value='Add To Cart']").click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='quantity' and text()='"+str(i)+"']")))
        i+=1

    driver.find_element_by_xpath("//a[contains(text(),'Checkout »')]").click()


    table_size = driver.find_elements_by_css_selector("table.dataTable td.item")

    i=0


    while is_element_present(driver, By.NAME, "remove_cart_item"):
        driver.find_element_by_xpath("//button[@value='Remove']").click()
        wait = WebDriverWait(driver, 10)
        table = driver.find_element(By.CSS_SELECTOR, ".dataTable")
        wait.until(EC.staleness_of((table)))

    pass


