import pytest
from selenium import webdriver
from dataclasses import dataclass
from pathlib import Path


@pytest.fixture()
def browser():
    driver_browser = webdriver.Chrome()
    driver_browser.implicitly_wait(10)
    return driver_browser


@dataclass
class Chrome:
    driver: webdriver.Chrome
    download: Path

@pytest.fixture(scope="function")
def chrome(tmp_path):
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": str(tmp_path),
            "download.prompt_for_download": False,
            "safebrowsing.enabled": True,
        },
    )
    
    driver = webdriver.Chrome(options=options)
    yield Chrome(driver=driver, download=tmp_path)
    driver.quit()