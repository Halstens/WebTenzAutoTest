from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TensorAboutPage(BasePage):
    URL = 'https://tensor.ru/about'
    block_working = (By.CLASS_NAME, 'tensor_ru-container tensor_ru-section tensor_ru-About__block3')
    links_images = (By.CLASS_NAME, 'tensor_ru-About__block3-image-filter')

    def __init__(self, browser):
        super().__init__(browser)
        # self.check_windows()
    
    def open(self):
        self.browser.get(self.URL)

    def verify_page(self):
        if self.browser.current_url == self.URL:
            return True
        else: 
            return False
        
    def check_windows(self):
        if self.browser.current_url != self.URL:
            for window_item in self.browser.window_handles:
                print(f"ПЕНИС 1 {window_item}")
                if window_item != self.browser.current_url:
                    self.browser.switch_to.window(window_item)

    # Блок "Работаем"
    def section_working(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.block_working)
        )
        return self.find(self.block_working)

    def section_working_is_displayed(self):
        return self.section_working.is_displayed()
    
    
    def images(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located(self.links_images)
        )
        return self.finds(self.links_images)
    
    # Проверка размера картинок в разделе "Работаем"
    def check_same_images(self):
        elements_images = self.images()
        first_image = elements_images[0]
        width = first_image.get_attribute("width")
        height = first_image.get_attribute("height")

        for img in elements_images:
            if width != img.get_attribute("width"):
                return False
            if height != img.get_attribute("height"):
                return False
            
        return True
