import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver_firefox(request):
    wd = webdriver.Firefox()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def driver_chrome(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver_firefox.get("http://localhost/litecart/admin/login.php")
    driver_firefox.find_element_by_name("username").send_keys("admin")
    driver_firefox.find_element_by_name("password").send_keys("admin")
    driver_firefox.find_element_by_name("login").click()
    WebDriverWait(driver_firefox, 10).until(EC.title_is("My Store"))



