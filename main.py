import datetime
from xml.sax.handler import feature_namespaces
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v129.network import load_network_resource

file = open("log.txt","w" )
# driver = webdriver.Chrome()
option = webdriver.ChromeOptions()
# option.add_argument("--headless")
option.add_experimental_option('detach', True)
driver =webdriver.Chrome(options=option)

# end to setup функции для сценариев

def set_ap():   #вход на сайт
    driver.get("http://www.saucedemo.com/") #

def login(): #проверка входа с ВАЛИДНЫМ логином и паролем         #
    user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    login1 = "standard_user"
    user_name.send_keys(login1)
    # file.write("OK!\n")

    user_pasw = driver.find_element(By.XPATH, '//input[@id="password"]')
    password = "secret_sauce"
    user_pasw.send_keys(password)
    # file.write("OK!\n")

    login_butt = driver.find_element(By.XPATH,'//*[@id="login-button"]')
    login_butt.click()
    file.write("Login is OK\n")
    # sleep(5)

def fake_login(): # проверка входа  с НЕВАЛИДНЫМ паролем
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

def login_with_enter(): # функция нажатия клавиши ENTER
        user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
        login1 = "standard_user"
        user_name.send_keys(login1)
       #file.write("OK!\n")

        user_pasw = driver.find_element(By.XPATH, '//input[@id="password"]')
        password = "secret_sauce"
        user_pasw.send_keys(password)
        # file.write("OK!\n")

        user_pasw.send_keys(Keys.ENTER)
        file.write("login_with_enter is OK\n")

def fake_login_text(): #проверка текста пhи неправильном вводе пароля
    correct_text = "Epic sadface: Username and password do not match any user in this service"
    current_text = driver.find_element(By. XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
    assert correct_text == current_text.text, "fake_login_text is fail"
    file.write("fake_login_text is OK")

def test_login_redirect(): # функция перенаправление пользователя с одного URL-адреса на другой
    correct_url = "https://www.saucedemo.com/inventory.html"
    get_url = driver.current_url

    assert correct_url==get_url,"test_login_redirect - XYI"
    file.write("test_login OK!\n")

def test_context(): #проверка текста на странице
    correct_text = "Products"
    current_text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
    driver.save_screenshot(f"sc_real_login\\screenshot_test_context"
                           f"{datetime.datetime.now().strftime('%H.%M.%S- %Y.%m.%d')}.png")
    assert correct_text==current_text.text, "test_contex_is_xyi"
    file.write("test_contrxt OK!\n")


def add_in_korzina():# добавление товара в корзину
    tovar1 = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
    tovar2 = driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-bike-light']")
    tovar1.click()
    tovar2.click()

def klik():
    korz = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    korz.click()

def klik_checkout():
    checkout = driver.find_element(By.XPATH,'//*[@id="checkout"]')
    checkout.click()



def test_context1(): #проверка текста на странице
    correct_text = "Sauce Labs Backpack"
    current_text = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    assert correct_text==current_text.text, "test_contex_is_xyi"
    file.write("test_context OK!\n")

def test_redirect1(): # функция перенаправление пользователя с одного URL-адреса на другой
    correct_url = "https://www.saucedemo.com/checkout-step-one.html"
    get_url = driver.current_url

def dostsvka_login():
    f_n = driver.find_element(By.XPATH, '//*[@id="first-name"]')
    fr = "A"
    l_n =driver.find_element(By.XPATH, '//*[@id="last-name"]')
    ln = "S"
    z_p_c = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
    zps = "D"
    f_n.send_keys(fr)
    l_n.send_keys(ln)
    z_p_c.send_keys(zps)

def klik_cont():
    cont = driver.find_element(By.XPATH,'//*[@id="continue"]')
    cont.click()





def valid_price():
        price1 = 9.99
        price2 = 29.99
        tax = 3.20
        valid = price1 + price2 + tax
        # Получаем текст элемента
        valid1_text = driver.find_element(By.XPATH,
                                          '//*[@id="checkout_summary_container"]/div/div[2]/div[8]').get_attribute(
            'innerText')
        # Извлекаем числа из строки с помощью регулярного выражения
        numbers = re.findall(r'\d+\.\d+', valid1_text)

        # Преобразуем извлеченные строки в числа и суммируем их
        extracted_price = sum(float(num) for num in numbers)
        assert valid == extracted_price, "valid_price_xyi"
        file.write("valid_price OK!\n")

def klik_finish():
    finish = driver.find_element(By.XPATH, '//*[@id="finish"]')
    finish.click()


def test_finish():
    text = "Thank you for your order!"
    texst = driver.find_element(By.XPATH , '//*[@id="checkout_complete_container"]/h2')
    assert text == texst.text , "test_finish_ Faled"
    file.write("test_finish OK")


def refresh_page():  # обновление страницы
    driver.refresh()


# main blok тестовые сценарии
def sc_polzovatel_valid():
    set_ap()
    login()
    add_in_korzina()
    klik()
    test_context1()
    klik_checkout()
    test_redirect1()
    dostsvka_login()
    klik_cont()
    valid_price()
    klik_finish()
    test_finish()


# def sc_polzovatel_NO_valid():
#     set_ap()
#     fake_login()
#     fake_login_text()
#
# def sc_polzovatel_valid_with_enter():
#     set_ap()
#     login_with_enter()
#     test_login_redirect()
#     test_context()

sc_polzovatel_valid()
# # sc_polzovatel_NO_valid()
# # sc_polzovatel_valid_with_enter()
file.close()
