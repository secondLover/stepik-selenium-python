from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
#link = "http://suninjuly.github.io/registration2.html"

browser = webdriver.Chrome()
browser.get(link)

# Заполнение поля "Имя"
nameInput = browser.find_element_by_css_selector(".first_class [placeholder='Введите имя']")
nameInput.send_keys("Тимур")

# Заполнение поля "Фамилия"
lastnameInput = browser.find_element_by_css_selector(".second_class [placeholder='Введите фамилию']")
lastnameInput.send_keys("Бекбамбетов")

# Заполнение поля "Email"
emailInput = browser.find_element_by_css_selector(".third_class [placeholder='Введите Email']")
emailInput.send_keys("test@kekw.com")

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

time.sleep(5)
browser.close()