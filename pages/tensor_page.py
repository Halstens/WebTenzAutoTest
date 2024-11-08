from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TensorPage(BasePage):
    URL = 'https://tensor.ru/'
    label_power_in_human = (By.XPATH, '//p[@class="tensor_ru-Index__card-title tensor_ru-pb-16"][text()="Сила в людях"]')
    link_about = (By.XPATH, '//a[@href="/about"][text()="Подробнее"]')

    def __init__(self, browser):
        super().__init__(browser)
        self.check_windows()

    def open(self):
        self.browser.get(self.URL)

    def check_windows(self):
        if self.browser.current_url != self.URL:
            for window_item in self.browser.window_handles:
                print(f"ПЕНИС 1 {window_item}")
                if window_item != self.browser.current_url:
                    self.browser.switch_to.window(window_item)

        print(f"Действующее окно(URL): {self.browser.current_url}")
        print(f"Действующее окно(ID): {self.browser.current_window_handle}")


    def block_power_in_human(self):
        # Ожидание появления блока "Сила в людях"
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.label_power_in_human)
        )
        return self.find(self.label_power_in_human)
       
    
    def block_power_in_human_is_displayed(self):
        return self.block_power_in_human().is_displayed()

    # Ссылка "Подробнее"
    def link_about_wait(self):
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.link_about)
        )
        print(f"ССЫЛКИ {self.find(self.link_about)}")
        return self.find(self.link_about)

    def click_link_about(self):
        self.link_about_wait().click()