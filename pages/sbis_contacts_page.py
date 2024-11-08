from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SbisContactsPage(BasePage):
    URL = 'https://sbis.ru/contacts/'
    tensor_banner = (By.CSS_SELECTOR, "a[href='https://tensor.ru/']")
    region_span = (By.XPATH, '//span[@class="sbis_ru-Region-Chooser__text sbis_ru-link"][text()="Республика Татарстан"]')
    region_span_update = (By.XPATH, '//span[@class="sbis_ru-Region-Chooser__text sbis_ru-link"]["Камчатский край"]')
    list_partners = (By.XPATH, '//div[@item-parent-key="-2"]')
    search_region = (By.XPATH, '//span[text()="41 Камчатский край"]')
    url_search_region = '41-kamchatskij-kraj'
    title_search_region = 'Камчатский край'
    partner_title_search_region = (By.XPATH, '//div[@title="СБИС - Камчатка"]')

    def __init__(self, browser):
        super().__init__(browser)
        self.check_windows()

    def check_windows(self):
        if self.browser.current_url != self.URL:
            for window_item in self.browser.window_handles:
                print(f"ПЕНИС 1 {window_item}")
                if window_item != self.browser.current_url:
                    self.browser.switch_to.window(window_item)

    def open(self):
        self.browser.get(self.URL)

    def click_tensor_banner(self):
        print(f"Действующее окно(ID): {self.browser.current_window_handle}")
        # Ожидание появления баннера после перехода на страницу Контакты
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.tensor_banner)
        )
        self.browser.find_element(*self.tensor_banner).click()

    def span_region_presence(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located(self.region_span)
        )
        return self.finds(self.region_span)[0]
    
    def span_region_is_displayed(self):
        return self.span_region_presence().is_displayed()
    
    def span_region_clickable(self):
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.region_span)
        )
        print(f"Ссылки {self.find(self.region_span)}")
        test = self.find(self.region_span)
        print(test.text)
        return test
    
    # Кликаем по региону и ищем Камчатский край
    def span_region_click(self):
        self.span_region_clickable().click()
    
    def searching_region(self):
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.search_region)
        )
        return self.find(self.search_region)
    
    def searching_region_click(self):
        self.searching_region().click()

    # Проверяем что подставился выбранный регион
    def check_url_seacrh_region(self):
        print(f"Действующий УРЛ {self.browser.current_url}")
        if self.url_search_region in self.browser.current_url:
            return True
        else:
            return False
    
    def updated_span_region(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.region_span_update)
        )
        return self.find(self.region_span_update)
    
    def updated_span_region_is_displayed(self):
        return self.updated_span_region().is_displayed()
    
    def title_url_page(self):
        WebDriverWait(self.browser, 10).until(
            EC.title_contains(self.title_search_region)
        )
        print(f"Действующий УРЛ {self.browser.current_url}")
        if self.url_search_region in self.browser.current_url:
            return True
        else:
            return False
    
    def update_check_partner(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.partner_title_search_region)
        )
        return self.find(self.partner_title_search_region)
    
    def check_partner_is_displayed(self):
        return self.update_check_partner().is_displayed()

    # Проверяем наличие списка партнеров
    def list_partners_func(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located(self.list_partners)
        )
        return self.finds(self.list_partners)[0]
    
    def list_partners_is_displayed(self):
        return self.list_partners_func().is_displayed()