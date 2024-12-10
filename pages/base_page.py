from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    base_url = 'https://www.sportgoodsstore.ru'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url is not None:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page error')

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

