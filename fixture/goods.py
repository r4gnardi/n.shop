

class Goods:

    def __init__(self, app):
        self.app = app

    def clicl_first_product(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//div[@class = "product grid-list "][1]//div[@class = "product-image"]').click()


