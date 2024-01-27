#добавление комментария
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
#пункт 1
driver.get("https://practice.automationtesting.in/")
#пункт 2
driver.execute_script("window.scrollBy(0, 600);")
#пункт 3
selenium_ruby = driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0 .woocommerce-LoopProduct-link>:nth-child(2)")
selenium_ruby.click()
#пункт 4
reviews = driver.find_element_by_css_selector(".reviews_tab>:nth-child(1)")
reviews.click()
#пункт 5
five_star = driver.find_element_by_class_name("star-5")
five_star.click()
#пункт 6
your_review = driver.find_element_by_id("comment")
your_review.send_keys("Nice book!")
#пункт 7
name = driver.find_element_by_id("author")
name.send_keys("Anton")
#пункт 8
email = driver.find_element_by_id("email")
email.send_keys("Maxnovskii_Ant@mail.ru")
#пункт 9
submit_btn = driver.find_element_by_id("submit")
submit_btn.click()
driver.quit()