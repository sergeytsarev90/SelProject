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
    driver.get("http://localhost:8080/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    driver.find_element_by_xpath("//i[@class='fa fa-plus-circle']").click()

    elements = driver.find_elements_by_xpath("//td/a[@target = '_blank']")
    main_window = driver.current_window_handle

    for element in elements:
        element.click()
        open_windows = driver.window_handles
        for window in open_windows:
            if main_window != window:
                new_window = window


        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to_window(new_window)
        

        driver.close()
        driver.switch_to_window(main_window)

    pass