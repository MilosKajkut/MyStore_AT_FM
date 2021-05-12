from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest


@pytest.fixture(params=['Firefox'], scope='class')
def init_driver(request):
    if request.param == 'Chrome':
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
        web_driver.maximize_window()
    elif request.param == 'Firefox':
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        web_driver.maximize_window()

    request.cls.driver = web_driver
    yield
    web_driver.close()