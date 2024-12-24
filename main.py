import datetime

from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

file = open("log.txt","w" )
# driver = webdriver.Chrome()
option = webdriver.ChromeOptions()
# option.add_argument("--headless")
option.add_experimental_option('detach', True)
driver =webdriver.Chrome(options=option)

# end to setup функции для сценариев

def set_ap():
    driver.get("http://www.saucedemo.com/")

def login():
    user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    login1 = "standard_user"
    user_name.send_keys(login1)
    file.write("OK!\n")

    user_pasw = driver.find_element(By.XPATH, '//input[@id="password"]')
    password = "secret_sauce"
    user_pasw.send_keys(password)
    file.write("OK!\n")

    login_butt = driver.find_element(By.XPATH,'//*[@id="login-button"]')
    login_butt.click()
    file.write(" logi is OK\n")

    # sleep(5)

def fake_login():
    user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    login = "standard_user"
    user_name.send_keys(login)
    file.write("OK!\n")

    user_pasw = driver.find_element(By.XPATH, '//input[@id="password"]')
    password = "secret_sauce1"
    user_pasw.send_keys(password)
    file.write("fake_login is OK!\n")

    login_batt = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    login_batt.click()
    file.write("OK!\n")

def login_with_enter():
        user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
        login1 = "standard_user"
        user_name.send_keys(login1)
        file.write("OK!\n")

        user_pasw = driver.find_element(By.XPATH, '//input[@id="password"]')
        password = "secret_sauce"
        user_pasw.send_keys(password)
        # file.write("OK!\n")

        user_pasw.send_keys(Keys.ENTER)
        file.write("login_with_enter is OK\n")

def fake_login_text():
    correct_text = "Epic sadface: Username and password do not match any user in this service"
    current_text = driver.find_element(By. XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
    assert correct_text == current_text.text, "fake_login_text is fail"
    file.write("fake_login_text is OK")

def test_login_redirect():
    correct_url = "https://www.saucedemo.com/inventory.html"
    get_url = driver.current_url

    assert correct_url==get_url,"test login xyi"
    file.write("test_login OK!\n")

def test_context():
    correct_text = "Products"
    current_text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
    driver.save_screenshot(f"sc_real_login\\screenshot_test_context"
                           f"{datetime.datetime.now().strftime('%H.%M.%S- %Y.%m.%d')}.png")
    assert correct_text==current_text.text, "test_contex_is_xyi"
    file.write("test_contrxt OK!\n")

def refresh_page():
    driver.refresh()


# main blok тестовые сценарии
def sc_polzovatel_valid():
    set_ap()
    login()
    test_login_redirect()
    test_context()

def sc_polzovatel_NO_valid():
    set_ap()
    fake_login()
    fake_login_text()

def sc_polzovatel_valid_with_enter():
    set_ap()
    login_with_enter()
    test_login_redirect()
    test_context()

sc_polzovatel_valid()
# sc_polzovatel_NO_valid()
# sc_polzovatel_valid_with_enter()
file.close()