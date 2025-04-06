# import time
#
# # webdriver это и есть набор команд для управления браузером
# from selenium import webdriver
#
# # импортируем класс By, который позволяет выбрать способ поиска элемента
# from selenium.webdriver.common.by import By
#
# # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
# driver = webdriver.Chrome()
#
# # команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
# time.sleep(5)
#
# # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# driver.get("https://stepik.org/lesson/25969/step/12")
# time.sleep(5)
#
# # Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# # Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
# # Ищем поле для ввода текста
# textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")
#
# # Напишем текст ответа в найденное поле
# textarea.send_keys("get()")
# time.sleep(5)
#
# # Найдем кнопку, которая отправляет введенное решение
# submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
#
# # Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
# submit_button.click()
# time.sleep(5)
#
# # После выполнения всех действий мы должны не забыть закрыть окно браузера
# driver.quit()

#--------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By # импортировали класс By, который содержит все возможные локаторы.
#
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
# browser = webdriver.Chrome()
# browser.get(link)
# button = browser.find_element(By.ID, "submit_button")
# button.click()
#
# # закрываем браузер после всех манипуляций
# browser.quit()

#--------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.ID, "submit_button")
#     button.click()
#
# finally:
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# --------------------- Тест на поиск элементов по разным атрибутам

# from selenium import webdriver
# import time
#
# from selenium.webdriver.common.by import By
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
# try:
#     input1 = browser.find_element(By.TAG_NAME, "input") # по тэгу
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name") # по имени
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "city") # по классу
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country") # по айди
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn") # по ccs селектору
#     button.click()
#
# except Exception as error:
#     print(f'Произошла ошибка, вот её трэйсбэк: {error}')
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     browser.close()
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# --------------- поиск элемента по тексту в ссылке

# from selenium import webdriver
# import time
#
# try:
#     link = "http://suninjuly.github.io/find_link_text"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     link = browser.find_element_by_link_text('224592')
#     link.click()
#
#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# except Exception as e:
#     print(e)
#
# finally:
#     time.sleep(5)
#     browser.close()
#     browser.quit()

#-----------------  использование метода find_elements

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.TAG_NAME, 'input')
#     for element in elements:
#         element.send_keys("Иоланда дура")
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#     print(browser._switch_to.alert.text) # вывод в консоль
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# не забываем оставить пустую строку в конце файла

# ---------------   поиск элемента по XPath

# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.by import By
#
# try:
#     browser = webdriver.Chrome()
#     link = "http://suninjuly.github.io/find_xpath_form"
#     browser.get(link)
#     fields = browser.find_elements(By.CSS_SELECTOR, '[type="text"]')
#
#     for field in fields:
#         field.send_keys("test")
#
#     submit = browser.find_element(By.XPATH, '//div[6]/button[3]').click()
#
# finally:
#     sleep(20)
#     browser.quit()

# -------------- регистрация на сайте, заполняя только обязательные поля, отмеченные символом *
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
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

# ----------------- кликаем по checkboxes и radiobuttons (капча для роботов)
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
# # функция для подсчета уравнения
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
#
#
# try:
#     link = "https://suninjuly.github.io/math.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # кликаем радиобаттон
#     robot = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
#     robot.click()
#
#     # кликаем чекбокс
#     imtherobot = browser.find_element(By.ID, "robotCheckbox")
#     imtherobot.click()
#
#     # нашли переменную на сайте, подставляем ее в функцию calc
#     x_element = browser.find_element(By.ID, 'input_value')
#     x = x_element.text
#     y = calc(x)
#
#     # вводим получившицся результат 'y' в инпут
#     input1 = browser.find_element(By.ID, "answer")
#     input1.send_keys(y)
#
#
#     # кликаем кнопку
#     button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# ------------- Задание: поиск сокровища с помощью get_attribute


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
# # функция для подсчета уравнения
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     link = "http://suninjuly.github.io/get_attribute.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # кликаем радиобаттон
#     robot = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
#     robot.click()
#
#     # кликаем чекбокс
#     imtherobot = browser.find_element(By.ID, "robotCheckbox")
#     imtherobot.click()
#
#     # нашли картинку сундука
#     treasure = browser.find_element(By.ID, "treasure")
#     x = treasure.get_attribute("valuex") # находим атрибут valuex и кладем в переменную х
#     y = calc(x)
#
#     # вводим получившицся результат 'y' в инпут
#     input1 = browser.find_element(By.ID, "answer")
#     input1.send_keys(y)
#
#
#     # кликаем кнопку
#     button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# ----------- работа с выпадающим списком

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time
#
# try:
#     link = "https://suninjuly.github.io/selects1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     num1netext = browser.find_element(By.ID, "num1")# находим первое число
#     num2netext = browser.find_element(By.ID, "num2") # находим второе число
#     num1 = num1netext.text # записываем в переменную текст из элемента num1netext
#     num2 = num2netext.text # так как элемент Webdriver, полученный в переменной num1netxt нельзя складывать друг с другом
#     y = str(str(int(num1) + int(num2))) # находим сумму
#     print(y)
#
#     # открываем список
#     select = Select(browser.find_element(By.TAG_NAME, "select"))
#     select.select_by_value(y)  # ищем элемент со значением y
#
#     # кликаем кнопку
#     button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# ------------- Метод execute_script

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element(By.TAG_NAME, "button")
# # В метод execute_script мы передали текст js-скрипта и найденный элемент button, к которому нужно будет проскроллить страницу.
# browser.execute_script("return arguments[0].scrollIntoView(true);", button) #заставить браузер дополнительно проскроллить нужный элемент
# button.click()

# -------------- Задание на execute_script

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
# # функция для подсчета уравнения
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     link = "https://SunInJuly.github.io/execute_script.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # считываем значение переменной х
#     treasure = browser.find_element(By.ID, "input_value")
#     x = treasure.text # считываем текст с переменной treasure и кладем в переменную х
#     y = calc(x)
#
#     # вводим получившицся результат 'y' в инпут
#     input1 = browser.find_element(By.ID, "answer")
#     input1.send_keys(y)
#
#     # кликаем чекбокс
#     imtherobot = browser.find_element(By.ID, "robotCheckbox")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", imtherobot) # делаем прокрутку в область видимости элементов, перекрытых футером.
#     imtherobot.click()
#
#     # кликаем радиобаттон
#     robot = browser.find_element(By.ID, "robotsRule")
#     robot.click()
#
#     # кликаем кнопку
#     button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# ---------------------- Задание: загрузка файла ---------- попробовать ННК заполнить

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import os
#
# try:
#     link = "http://suninjuly.github.io/file_input.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # заполняем данные
#     input1 = browser.find_element(By.NAME, 'firstname')
#     input1.send_keys("Irinka")
#     input2 = browser.find_element(By.NAME, 'lastname')
#     input2.send_keys("Nelep")
#     input3 = browser.find_element(By.NAME, 'email')
#     input3.send_keys("iranelep@gmail.com")
#
#     # загрузка файла
#     current_dir = os.path.abspath(os.path.dirname("C:\\"))  # получаем путь к директории текущего исполняемого файла, экранировать слэш
#     file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
#     element = browser.find_element(By.CSS_SELECTOR, "[type='file']") # находим кнопку с названием Добавить файл
#     element.send_keys(file_path)
#
#
#     button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()

# ------------------ Задание: принимаем alert


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time, math
# import os
#
# # # функция для подсчета уравнения
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
#
# try:
#     link = "http://suninjuly.github.io/alert_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # нажимаем кнопку
#     button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
#     button.click()
#
#     # нажимаем ДА в алерте
#     confirm = browser.switch_to.alert
#     confirm.accept()
#
#     # считываем значение переменной х
#     number = browser.find_element(By.ID, "input_value")
#     x = number.text # считываем число с переменной number и кладем в переменную х
#     y = calc(x)
#
#     # вводим получившицся результат 'y' в инпут
#     input1 = browser.find_element(By.ID, "answer")
#     input1.send_keys(y)
#
#     # нажимаем кнопку подтвердить
#     button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()

# ---------------- открываем вторую вкладку

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time, math
# import os
#
# # # функция для подсчета уравнения
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
#
# try:
#     link = "http://suninjuly.github.io/redirect_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # нажимаем кнопку
#     button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
#     button.click()
#
#     # переходим на новую вкладку
#     new_window = browser.window_handles[1] # сначала объявляем переменную второй вкладки
#     browser.switch_to.window(new_window) # затем говорим браузеру перейти на новую вкладку
#
#     # считываем значение переменной х
#     number = browser.find_element(By.ID, "input_value")
#     x = number.text # считываем число с переменной number и кладем в переменную х
#     y = calc(x)
#
#     # вводим получившицся результат 'y' в инпут
#     input1 = browser.find_element(By.ID, "answer")
#     input1.send_keys(y)
#
#     # нажимаем кнопку подтвердить
#     button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()

# --------------------- понятие неявных ожиданий (Explicit Waits)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# # говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait1.html")
#
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text

# -------------- понятие явных ожиданий (Explicit Waits)

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# browser = webdriver.Chrome()
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text

# ------------------- Задание: ждем нужный текст на странице

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time, math
#
# # функция для подсчета уравнения
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
# browser = webdriver.Chrome()
#
# try:
#     browser.get("http://suninjuly.github.io/explicit_wait2.html")
#     button = browser.find_element(By.ID, "book")
#
#     # говорим Selenium проверять в течение 5 секунд, пока значение не станет 100 долларов
#     WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
#
#     button.click() # нажимаем на кнопку, после того как значение станет 100 долларов
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button) # после нажатия кнопки нужно проскроллить страниц вниз
#
#     # считываем значение переменной х
#     number = browser.find_element(By.ID, "input_value")
#     x = number.text # считываем число с переменной number и кладем в переменную х
#     y = calc(x)
#
#     # вводим получившийся результат 'y' в инпут
#     input1 = browser.find_element(By.ID, "answer")
#     input1.send_keys(y)
#
#     # нажимаем кнопку подтвердить
#     button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()

# --------------- падающий тест

# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of a number"
#
# def test_abs2():
#     assert abs(-42) == -42, "Should be absolute value of a number"
#
# if __name__ == "__main__":
#     test_abs1()
#     test_abs2()
#     print("Everything passed")

