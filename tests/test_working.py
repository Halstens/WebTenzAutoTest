from pages.tensor_about_page import TensorAboutPage

def test_work_and_check(browser):
    tensor_about = TensorAboutPage(browser)
    tensor_about.open()
    assert tensor_about.check_same_images()
    
