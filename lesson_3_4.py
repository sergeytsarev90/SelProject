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

@pytest.fixture
def driver_chrome(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

@pytest.fixture
def driver_ie(request):
    wd = webdriver.Ie(capabilities={"requireWindowFocus": True})
    request.addfinalizer(wd.quit)
    return wd

def test_example_chrome(driver_chrome):
    driver_chrome.get("http://www.google.com")
    WebDriverWait(driver_chrome, 10).until(EC.title_is("Google"))

def test_example_firefox(driver_firefox):
    driver_firefox.get("http://www.google.com")
    WebDriverWait(driver_firefox, 10).until(EC.title_is("Google"))

def test_example_ie(driver_ie):
    driver_ie.get("http://www.google.com")
    WebDriverWait(driver_ie, 10).until(EC.title_is("Google"))


