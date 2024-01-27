# #отображение страницы товара
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# #пункт 1
# driver.get("https://practice.automationtesting.in/")
# #пункт 2
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
# email = driver.find_element_by_id("username")
# email.send_keys("Maxnovskii_Ant@mail.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("abcdeF12345^")
# login_btn = driver.find_element_by_css_selector(".u-column1 .woocommerce-Button.button")
# login_btn.click()
# #пункт 3
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# #пункт 4
# book_html_5_forms = driver.find_element_by_css_selector(".post-181 .woocommerce-LoopProduct-link > :nth-child(2)")
# book_html_5_forms.click()
# #пункт 5
# name_book = driver.find_element_by_class_name("entry-title")
# name_book_text = name_book.text
# assert name_book_text == "HTML5 Forms"
# driver.quit()

# #количество товаров в категории
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# #пункт 1
# driver.get("https://practice.automationtesting.in/")
# #пункт 2
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
# email = driver.find_element_by_id("username")
# email.send_keys("Maxnovskii_Ant@mail.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("abcdeF12345^")
# login_btn = driver.find_element_by_css_selector(".u-column1 .woocommerce-Button.button")
# login_btn.click()
# #пункт 3
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# #пункт 4
# HTML = driver.find_element_by_css_selector(".cat-item-19 :nth-child(1)")
# HTML.click()
# #пункт 5
# sum_tovarov = driver.find_element_by_css_selector(".cat-item-19 :nth-child(2)")
# sum_tovarov_text = sum_tovarov.text
# assert "3" in sum_tovarov_text
# driver.quit()

# #сортировка товаров
# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# #пункт 1
# driver.get("https://practice.automationtesting.in/")
# #пункт 2
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
# email = driver.find_element_by_id("username")
# email.send_keys("Maxnovskii_Ant@mail.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("abcdeF12345^")
# login_btn = driver.find_element_by_css_selector(".u-column1 .woocommerce-Button.button")
# login_btn.click()
# #пункт 3
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# #пункт 4
# sortirovka = driver.find_element_by_class_name("orderby")
# sortirovka_check = sortirovka.get_attribute("value")
# assert sortirovka_check == "menu_order"
# #пункт 5
# price_max_min = Select(sortirovka)
# price_max_min.select_by_value("price-desc")
# #пункт 6
# sortirovka = driver.find_element_by_class_name("orderby")
# #пункт 7
# sortirovka_check1 = sortirovka.get_attribute("value")
# assert sortirovka_check1 == "price-desc"
# driver.quit()

# #отображение,скидка товара
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# #пункт 1
# driver.get("https://practice.automationtesting.in/")
# #пункт 2
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
# email = driver.find_element_by_id("username")
# email.send_keys("Maxnovskii_Ant@mail.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("abcdeF12345^")
# login_btn = driver.find_element_by_css_selector(".u-column1 .woocommerce-Button.button")
# login_btn.click()
# #пункт 3
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# #пункт 4
# book_android_qsg = driver.find_element_by_css_selector(".post-169 h3")
# book_android_qsg.click()
# #пункт 5
# old_price = driver.find_element_by_css_selector(".price > del > .amount")
# old_price_text = old_price.text
# assert old_price_text == "₹600.00"
# #пункт 6
# new_price = driver.find_element_by_css_selector(".price > ins > .amount")
# new_price_text = new_price.text
# assert new_price_text == "₹450.00"
# #пункт 7
# wait = WebDriverWait(driver, 10)
# android_qsg_picture = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "zoom")))
# android_qsg_picture.click()
# #пункт 7
# close_picture = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
# close_picture.click()
# driver.quit()

# #проверка цены в корзине
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# #пункт 1
# driver.get("https://practice.automationtesting.in/")
# #пункт 2
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# #пункт 3
# add_to_basket = driver.find_element_by_css_selector(".post-182 >:nth-child(2)")
# add_to_basket.click()
# #пункт 4
# time.sleep(3)
# item = driver.find_element_by_class_name("cartcontents")
# item_text = item.text
# assert item_text == "1 Item"
# cost = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
# cost_text = cost.text
# assert cost_text == "₹180.00"
# #пункт 5
# basket = driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0")
# basket.click()
# wait = WebDriverWait(driver, 10)
# #пункт 6
# Subtotal_cost = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .amount"), "₹180.00"))
# #пункт 7
# Total_cost = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .amount"), "₹183.60"))
# driver.quit()

#работа в корзине
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# #пункт 1
# driver.get("https://practice.automationtesting.in/")
# #пункт 2
# shop = driver.find_element_by_id("menu-item-40")
# shop.click()
# #пункт 3
# driver.execute_script("window.scrollBy(0, 300);")
# add_to_basket1 = driver.find_element_by_css_selector(".post-182 >:nth-child(2)")
# add_to_basket1.click()
# time.sleep(7)
# add_to_basket2 = driver.find_element_by_css_selector(".post-180 >:nth-child(2)")
# add_to_basket2.click()
# #пункт 4
# basket_btn = driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0")
# basket_btn.click()
# #пункт 5
# time.sleep(3)
# del_first_book = driver.find_element_by_css_selector(".cart>:nth-child(2)>:nth-child(1) .remove")
# del_first_book.click()
# #пункт 6
# undo = driver.find_element_by_link_text("Undo?")
# undo.click()
# #пункт 7
# quantity = driver.find_element_by_css_selector(".cart>:nth-child(2)>:nth-child(1) .text")
# quantity.clear()
# quantity.send_keys("3")
# #пункт 8
# update_basket = driver.find_element_by_name("update_cart")
# update_basket.click()
# #пункт 9
# quantity = driver.find_element_by_css_selector(".cart>:nth-child(2)>:nth-child(1) .text")
# quantity_check = quantity.get_attribute("value")
# assert quantity_check == "3"
# #пункт 10
# time.sleep(3)
# apply_coupon = driver.find_element_by_name("apply_coupon")
# apply_coupon.click()
# #пункт 11
# error = driver.find_element_by_css_selector(".woocommerce-error li")
# error_text = error.text
# assert error_text == "Please enter a coupon code."
# driver.quit()

#покупка товара
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
shop = driver.find_element_by_id("menu-item-40")
shop.click()
#пункт 3
driver.execute_script("window.scrollBy(0, 300);")
add_to_basket1 = driver.find_element_by_css_selector(".post-182 >:nth-child(2)")
add_to_basket1.click()
time.sleep(3)
#пункт 4
basket_btn = driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0")
basket_btn.click()
#пункт 5
wait = WebDriverWait(driver, 10)
proceed_to_checkout_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"wc-forward")))
proceed_to_checkout_btn.click()
#пункт 6
billing_details_check= wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-billing-fields h3"), "Billing Details"))
first_name = driver.find_element_by_id("billing_first_name")
first_name.send_keys ("Anton")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Machnovskii")
email_adress = driver.find_element_by_id("billing_email")
email_adress.send_keys("Maxnovskii_Ant@mail.ru")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("81112223333")
country = driver.find_element_by_id("s2id_billing_country")
country.click()
country_text = driver.find_element_by_id("s2id_autogen1_search")
country_text.send_keys("Russia")
country_click = driver.find_element_by_class_name("select2-result-label")
country_click.click()
street_adress = driver.find_element_by_id("billing_address_1")
street_adress.send_keys("Lenina 33")
appartament = driver.find_element_by_id("billing_address_2")
appartament.send_keys("33")
city = driver.find_element_by_id("billing_city")
city.send_keys("Rostov")
state = driver.find_element_by_id("billing_state")
state.send_keys("Russia")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("192161")
#пункт 7
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(4)
pay = driver.find_element_by_id("payment_method_cheque")
pay.click()
#пункт 8
place_order = driver.find_element_by_id("place_order")
place_order.click()
#пункт 9
check_message= wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-35 .woocommerce p"), "Thank you. Your order has been received"))
#пункт 10
payment_metod = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".shop_table>:nth-child(3)>:nth-child(3) td"), "Check Payments"))
driver.quit()