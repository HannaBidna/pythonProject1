import pytest
import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="module")
def driver():
    print("Init driver")
    driver = Chrome()
    yield driver
    print("Quit driver")
    driver.quit()


def test_reg_text(driver):
    # driver = Chrome()
    # driver = webdriver.Chrome()
    driver.implicity_wait(3)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    signup = driver.find_element(By.CLASS_NAME, "hero-descriptor_btn")
    signup.click()
    name = driver.find_element(By.ID, "signupName")
    name.send_keys("Zhanna")
    lastname = driver.find_element(By.ID, "signupLastName")
    lastname.send_keys("Orl")
    email = driver.find_element(By.ID, "signupEmail")
    email.send_keys("jane@gmail.com")
    password = driver.find_element(By.ID, "signupPassword")
    password.send_keys("Welcomej12345")
    repassword = driver.find_element(By.ID, "signupRepeatPassword")
    repassword.send_keys("Welcomej12345")
    register = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-signup-modal/div[3]/button")
    jtitle = driver.find_element(By.CLASS_NAME, "modal-title")
    assert 'jhfkuhgckygd' in jtitle.text
    register.click()
    time.sleep(3)
    # useralert = driver.find_element(By., "")
    time.sleep(3)
    driver.close()