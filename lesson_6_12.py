import pytest
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

def SetDatepicker(driver, selector, date):
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, selector)))
    driver.execute_script("$('s[0]').datepicker('setDate', 's[0]')", date)


def test_example(driver):
    driver.get("http://localhost:8080/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_xpath("//ul[@id='box-apps-menu']//li[2]//a[1]//span[2]").click()
    driver.find_element_by_xpath("//td[@id='content']//div//a[2]").click()


    driver.find_element_by_xpath("//td//label[1]").click()
    driver.find_element_by_xpath("//input[@name='name[en]']").send_keys('уточка')
    driver.find_element_by_xpath("//input[@name='code']").send_keys('12345')

    driver.find_element_by_xpath("//div[@class='input-wrapper']//input[@value='1']").click()

    сategory = Select(driver.find_element_by_xpath("//select[@name='default_category_id']"))
    сategory.select_by_visible_text('Rubber Ducks')

    driver.find_element_by_xpath("//input[@value='1-3']").click()
    driver.find_element_by_xpath("//div[@id='tab-general']//input[@value='0.00']").send_keys('12345')

    driver.find_element_by_xpath('//*[@id="tab-general"]/table/tbody/tr[9]/td/table/tbody/tr[1]/td/input').send_keys('C:\PyProject\SelProject\SelProject\duck.jpg')

    SetDatepicker(driver,"//input[@name='date_valid_from']","04.07.2018")
    pass



