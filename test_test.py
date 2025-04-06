from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual("http://suninjuly.github.io/registration1.html")

    def test_abs2(self):
        self.assertEqual("http://suninjuly.github.io/registration2.html")


if __name__ == "__main__":
    unittest.main()

#
# try:
#     link = "http://suninjuly.github.io/registration1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Ваш код, который заполняет обязательные поля
#     label=browser.find_elements(By.TAG_NAME,"label")
#     _input=browser.find_elements(By.TAG_NAME,"input")
#
#     for i,k in enumerate(label):
#         k=k.text
#         if k[-1]=="*":
#             _input[i].send_keys("заполнить")
#     # Отправляем заполненную форму
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(5)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()