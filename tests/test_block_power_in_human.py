from selenium.webdriver.chrome.webdriver import WebDriver
from pages.sbis_main_page import SbisMainPage
from pages.sbis_contacts_page import SbisContactsPage
from pages.tensor_page import TensorPage


def test_block(browser):
    sbis_page = SbisMainPage(browser)
    sbis_page.open()
    sbis_page.go_to_contacts()

    contacts_page = SbisContactsPage(browser)
    contacts_page.click_tensor_banner()

    # Проверяем блок с надписью "Сила в людях"
    tensor_page = TensorPage(browser)
    assert tensor_page.block_power_in_human_is_displayed()

