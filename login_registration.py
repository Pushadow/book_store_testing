# #регистрация аккаунта
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# #пункт 1
# driver.get("https://practice.automationtesting.in/")
# #пункт 2
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
# #пункт 3
# email_reg = driver.find_element_by_id("reg_email")
# email_reg.send_keys("Maxnovskii_Ant@mail.ru")
# #пункт 4
# password_reg = driver.find_element_by_id("reg_password")
# password_reg.send_keys("abcdeF12345^")
# #пункт 5
# register_btn = driver.find_element_by_css_selector(".u-column2 .woocommerce-Button.button")
# register_btn.click()
# driver.quit()

#логин в систему
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
#пункт 1
driver.get("https://practice.automationtesting.in/")
#пункт 2
my_account = driver.find_element_by_id("menu-item-50")
my_account.click()
#пункт 3
email = driver.find_element_by_id("username")
email.send_keys("Maxnovskii_Ant@mail.ru")
#пункт 4
password = driver.find_element_by_id("password")
password.send_keys("abcdeF12345^")
#пункт 5
login_btn = driver.find_element_by_css_selector(".u-column1 .woocommerce-Button.button")
login_btn.click()
#пункт 6
logout = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link--customer-logout :nth-child(1)")))
driver.quit()