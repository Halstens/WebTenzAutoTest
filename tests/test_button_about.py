from pages.sbis_main_page import SbisMainPage
from pages.sbis_contacts_page import SbisContactsPage
from pages.tensor_page import TensorPage
from pages.tensor_about_page import TensorAboutPage


# в блоке находим кнопку "Подробнее" и проверяем открытие страницы

def test_button_about(browser):
    tensor_page = TensorPage(browser)
    tensor_page.open()
    tensor_page.click_link_about()
    tensor_about = TensorAboutPage(browser)
    assert tensor_about.verify_page()