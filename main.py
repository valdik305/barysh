from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

file = open("log.txt","w" )
driver = webdriver.Chrome()
option = webdriver.ChromeOptions()
option.add_argument("--headless")
# option.add_experimental_option('detach', True)
driver =webdriver.Chrome(options=option)


def set_ap():
    driver.get("http://www.saucedemo.com/")


def login():
    user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    login = "standard_user"
    user_name.send_keys(login)
    file.write("OK!\n")

    user_pasw = driver.find_element(By.XPATH, '//input[@id="password"]')
    password = "secret_sauce"
    user_pasw.send_keys(password)
    file.write("OK!\n")

    # sleep(3)


    login_batt = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    login_batt.click()
    file.write("OK!\n")

    # sleep(5)

def test_login_redirect():
    correct_url = "https://www.saucedemo.com/inventory.html"
    get_url = driver.current_url

    assert correct_url==get_url,"test login xyi"
    file.write("test_login OK!\n")

def test_contrxt():
    correct_text = "Products"
    current_text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
    assert correct_text==current_text.text, "test_contex_is_xyi"
    file.write("test_contrxt OK!\n")

set_ap()
login()
test_login_redirect()
test_contrxt()