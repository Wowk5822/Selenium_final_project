from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(driver):
     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

     #инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
     page = MainPage(driver, link)

     #otwieramy browser za pomocą funkcji która opisana w BasePage
     page.open()

     #idziemy do naszej strony za pomocą funkcji opisanej w MainPage
     page.go_to_login_page()

def test_guest_should_see_login_link(driver):
     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

     page = MainPage(driver, link)
     page.open()
     page.should_be_login_link()










