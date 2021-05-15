from selenium import webdriver
import pytest

def test_loginpage():
    driver = webdriver.Chrome("c:\\chromedriver.exe")
    URl = "https://www.comm100.com/"
    driver.get(URl)
    driver.maximize_window()
    driver.find_element_by_link_text("Sign In").click()
    driver.implicitly_wait(20)
    driver.find_element_by_id("txtEmail").send_keys("dolid@mirai.re")
    driver.find_element_by_id("txtPassword").send_keys("123456789")
    driver.implicitly_wait(10)
    error= driver.find_element_by_xpath("//div[@id='ajaxErrorMsg']")
    print(error.text)
    assert error.text == "Email or password is incorrect."
