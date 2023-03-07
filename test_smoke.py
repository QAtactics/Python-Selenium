import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_product_view_sku():
    """
    Test case WERT-1
    """
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
   
    service = Service(ChromeDriverManager().install())
 
    driver = webdriver.Chrome(service=service, options=chrome_options)

    url = "https://test.qa.studio"
    driver.get(url=url)
		
    element = driver.find_element(by=By.CSS_SELECTOR, value="[class='tab-featured ']")
    element.click()
	
    x_path_table = '//*[@id="rz-shop-content"]/ul/li[1]/div/div[2]/h2/a'
    element = driver.find_element(By.XPATH, value=x_path_table)
    element.click()

    sku = driver.find_element(By.CLASS_NAME, value="sku")

    assert sku.text == 'C0MSSDSUM7', "Unexpected sku"