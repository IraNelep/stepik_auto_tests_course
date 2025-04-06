from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {

        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }

#---------------
# def test_add_todo(page):
#     page.goto("https://demo.playwright.dev/todomvc/#/")
#     page.get_by_placeholder("What needs to be done?").click()
#     page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
#     page.get_by_placeholder("What needs to be done?").press("Enter")
# --------------
# def test_add_todo(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
# --------------
# def test_checkbox(page, playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context() # показывает браузер
#     page = context.new_page()
#     page.goto('https://zimaev.github.io/checks-radios/')
#     page.locator("text=Default checkbox").check() #  по очереди нажимаем на все чекбоксы и радио-кнопки на сайте
#     page.locator("text=Checked checkbox").check()
#     page.locator("text=Default radio").check()
#     page.locator("text=Default checked radio").check()
#     page.locator("text=Checked switch checkbox input").check()
# ----------------

# def test_select(page): # выпадающий список
#     page.goto('https://zimaev.github.io/select/')
#     page.select_option('#floatingSelect', value="3")
#     page.select_option('#floatingSelect', index=1)
#     page.select_option('#floatingSelect', label="Нашел и завел bug")
#
# # -----------------
#
# def test_select_multiple(page): # множественный выбор в выпадающем списке
#     page.goto('https://zimaev.github.io/select/')
#     page.select_option('#skills', value=["playwright", "python"])
#
# # -------------------
#
#
# def test_drag_and_drop(page): # операцию перетаскивания
#     page.goto('https://zimaev.github.io/draganddrop/')
#     page.drag_and_drop("#drag", "#drop")
#
# --------------
# def test_dialogs(page: Page): # диалоговые окна
#     page.goto("https://zimaev.github.io/dialog/")
#     page.get_by_text("Диалог Alert").click()
#     page.get_by_text("Диалог Confirmation").click()
#     page.get_by_text("Диалог Prompt").click()
#
# # -----------------
# def test_dialogs(page: Page): # сценарий в котором необходимо нажать кнопку "OK"
#     page.goto("https://zimaev.github.io/dialog/")
#     page.on("dialog", lambda dialog: dialog.accept()) # анонимная функция, в качестве параметра принимает экземпляр класса Dialog
#     page.get_by_text("Диалог Confirmation").click() #Далее метод dialog.accept()  заставляет Playwright нажимать на кнопку OK в диалоговом окне

# ---------------------

# def test_select_multiple(page): # Загрузка файла
#     page.goto('https://zimaev.github.io/upload/') # сначала найти элемент ввода для загрузки файла и использовать метод чтобы указать путь к необходимому файлу.
#     page.set_input_files("#formFile", "hello.txt")
#     page.locator("#file-submit").click()
#
# def test_select_multiple(page): #используется обработчик события "filechooser" и получить тот-же результат
#     page.goto('https://zimaev.github.io/upload/')
#     page.on("filechooser", lambda file_chooser: file_chooser.set_files("hello.txt"))
#     page.locator("#formFile").click()
#
# def test_select_multiple(page):# используется with as
#     page.goto('https://zimaev.github.io/upload/')
#     with page.expect_file_chooser() as fc_info:
#         page.locator("#formFile").click()
#     file_chooser = fc_info.value
#     file_chooser.set_files("hello.txt")

# ------------------

# def test_download(page): # Скачать файл
#
#     page.goto("https://demoqa.com/upload-download")
#
#     with page.expect_download() as download_info:
#         page.locator("a:has-text(\"Download\")").click()
#
#     download = download_info.value
#     file_name = download.suggested_filename # получить оригинальное имя файла, используя свойство suggested_filename
#     destination_folder_path = "./data/" #  куда сохранить этот файл
#     download.save_as(os.path.join(destination_folder_path, file_name)) # сохраним результат загрузки в указанный путь назначения
#
# --------------------
# def test_download(page): #Получение значений элемента
#     page.goto('https://zimaev.github.io/table/')
#     row = page.locator("tr")
#     print(row.all_inner_texts()) # innerText умеет считывать стили и не возвращает содержимое скрытых элементов
#
#
# def test_download(page):
#     page.goto('https://zimaev.github.io/table/')
#     row = page.locator("tr")
#     print(row.all_text_contents()) # textContent получает содержимое всех элементов, включая <script> и <style>
#
# def test_download(page): # получить текст всех схожих элементов
#     page.goto('https://zimaev.github.io/table/')
#     row = page.locator("tr")
#     print(row.all_inner_texts())
#
# def test_download(page):
#     page.goto('https://zimaev.github.io/table/')
#     row = page.locator("tr")
#     print(row.all_text_contents())

# -----------------
# def test_new_tab(page: Page): #Работа с несколькими вкладками
#     page.goto("https://zimaev.github.io/tabs/")
#     with page.context.expect_page() as tab:
#         page.get_by_text("Переход к Dashboard").click() #нажатие на элемент "Переход к Dashboard" открывает новую вкладку в контексте браузера
#
#     new_tab = tab.value #Переменная tab - это класс EventInfo, возвращаемый менеджером контекста with. Мы можем получить доступ к классу с помощью свойства value.
#     assert new_tab.url == "htt  ps://zimaev.github.io/tabs/dashboard/index.html?" #написать проверку для этого элемента, что он видим. И проверим, что url данной вкладки соответсвует нужному нам
#     sign_out = new_tab.locator('.nav-link', has_text='Sign out') #Найдем элемент в панели навигации c текстом Sign out и проверим его на видимость
#     assert sign_out.is_visible()

# --------
# Тест проверки заполнения формы
# from playwright.sync_api import expect
#
#
# def test_todo(page, playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context() # показывает браузер
#     page = context.new_page()
#     page.goto('https://demo.playwright.dev/todomvc/#/') #  открыть сайт
#     expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/") # проверить что открытая страница имеет нужный нам адрес
#     input_field = page.get_by_placeholder('What needs to be done?') # ищем поле ввода задачи по плейсхолдеру
#     expect(input_field).to_be_empty() # проверить что оно пустое
#     input_field.fill("Закончить курс по playwright") # в сохраненный с переменной input_field веб-элемент вводим первой текст задачи
#     input_field.press('Enter') # т.к нет специальной кнопки для сохранения задачи, сохранение происходит с нажатием клавиши Enter.
#     input_field.fill("Добавить в резюме, что умею автоматизировать") # в сохраненный с переменной input_field веб-элемент вводим второй текст задачи
#     input_field.press('Enter') # сохраняем
#     page.pause() # вызывается перед шагом который нужно проверить.Playwright приостановит выполнение скрипта, откроет Playwright Inspector  и будет ждать
#     todo_item = page.get_by_test_id('todo-item') # нужно получить количество задач в приложении, использовуем метод get_by_test_id для локализации всех задач и сохраним результат поиска в переменную
#     expect(todo_item).to_have_count(2) # Проверяем количество задач
#     todo_item.get_by_role('checkbox').nth(0).click() # Для того чтобы отметить выполненной, нужно нажать на элемент <input>  c типом checkbox внутри  задачи.
#     expect(todo_item.nth(0)).to_have_class('completed') # убеждаемся, что задача выполнена - У элемента который мы отмечаем сделанным появляется класс completed.

# -----------------
# Мониторинг сетевых запросов
# Для того чтобы начать прослушивать сеть, необходимо дать команду слушать события request и response и обрабатывать их
from playwright.sync_api import Page

# def test_listen_network(page: Page):
#     page.on("request", lambda request: print(">>", request.method, request.url))
#     page.on("response", lambda response: print("<<", response.status, response.url))
#     page.goto('https://osinit.ru/')
#
# # -----
# # изменение передаваемых данных
#
# def test_network(page):
#     page.route("**/register", lambda route: route.continue_(post_data='{"email": "user","password": "secret"}')) # page.route - функция позволяющая обрабатывать сетевые запросы, route.continue - изменить
#     page.goto('https://reqres.in/')
#     page.get_by_text(' Register - successful ').click()

# создание json, но уже со своими значениями
# def test_mock_tags(page):
#     page.route("**/api/tags", lambda route: route.fulfill(path="data.json"))
#     page.goto('https://demo.realworld.io/')

from playwright.sync_api import Page, Route, expect


# def test_intercepted(page: Page):
#     def handle_route(route: Route):
#         response = route.fetch() # выполняет запрос на сервер и получает результат на данный запрос
#         json = response.json()
#         json["tags"] = ["open", "solutions"] #Изменить полученные данные
#         route.fulfill(json=json) #отправляется запрос с исправленным телом ответа
#
#     page.route("**/api/tags", handle_route)
#
#     page.goto("https://demo.realworld.io/")
#     sidebar = page.locator('css=div.sidebar')
#     expect(sidebar.get_by_role('link')).to_contain_text(["open", "solutions"])
#
# Подмена ответов из HAR
# def test_replace_from_har(page):
#     page.goto("https://reqres.in/")
#     page.route_from_har("example.har")
#     users_single = page.locator('li[data-id="users-single"]')
#     users_single.click()
#     response = page.locator('[data-key="output-response"]')
#     expect(response).to_contain_text("Open Solutions")

#  Тестирование API GET запрос
# def test_inventory(page):
#     response = page.request.get('https://petstore.swagger.io/v2/store/inventory')
#     print(response.status)
#     print(response.json())
#
# # Тестирование API POST запрос
# def test_add_user(page):
#     data = [
#               {
#                 "id": 9743,
#                 "username": "fsd",
#                 "firstName": "fff",
#                 "lastName": "ggg",
#                 "email": "bbb",
#                 "password": "tt",
#                 "phone": "333",
#                 "userStatus": 0
#               }
#             ]
#     header = {
#         'accept': 'application/json',
#         'content-Type': 'application/json'
#     }
#     response = page.request.post('https://petstore.swagger.io/v2/user/createWithArray',data=data, headers=header)
#     print(response.status)
#     print(response.json())

# -----------------




