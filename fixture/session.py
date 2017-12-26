from selenium.webdriver import ActionChains
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def logout(self):
        wd = self.app.wd
        logout = wd.find_element_by_css_selector('a[href = "http://uae.microless.com/account/"][class ="button-link"]')
        ActionChains(wd).move_to_element(logout).perform()
        #WebDriverWait(wd, 10000).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[5]/a[1]")))
        wd.execute_script('$(".pull-right > div:nth-child(1) > div:nth-child(2)")[0].setAttribute("style", "display: block")')
        sleep(5)
        wd.find_element_by_xpath("(//a[text() = 'Log Out'])[2]").click()


    def login(self, username, password):
        wd = self.app.wd
        self.app.main.open_home_page()
        wd.find_element_by_link_text("Your Account").click()
        wd.find_element_by_id("email").click()
        wd.find_element_by_id("email").clear()
        wd.find_element_by_id("email").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath('//button[text() = "Log in"]').click()