from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SbisMainPage(BasePage):

    URL = 'https://sbis.ru/'
    contacts_selector = (By.XPATH, '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[1]')
    contacts_link = (By.XPATH, '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[2]/a[2]')
    link_to_download_plagin = (By.XPATH, '//a[@href="/download"]')

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get(self.URL)

    def go_to_contacts(self):
        print(f"Оно СБИСА {self.browser.current_url}")
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.contacts_selector)
        )
        self.browser.find_element(*self.contacts_selector).click()
        self.browser.find_element(*self.contacts_link).click()

    # переход по ссылке на скачивание
    def go_to_link_download_plagin(self):
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.link_to_download_plagin)
        )
        return self.find(self.link_to_download_plagin)
    
    def link_download_plagin_click(self):
        self.go_to_link_download_plagin().click()