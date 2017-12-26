from selene.driver import SeleneDriver
from fixture.session import SessionHelper
from fixture.main_page import MainPage
from fixture.goods import Goods
from selenium import webdriver
from fixture.product import Product


class Application:

    def __init__(self, browser):
        if browser == "chrome":
            self.tb = webdriver.Chrome("/home/ivn/Downloads/chromedriver")
        elif browser == "firefox":
            self.tb = webdriver.Firefox(executable_path="/home/ivn/Downloads/geckodriver")
        self.wd = SeleneDriver.wrap(self.tb)
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.main = MainPage(self)
        self.goods = Goods(self)
        self.product = Product(self)

    def destroy(self):
        self.wd.quit()

        ####

