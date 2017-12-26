from selene.api import *
import re
#import cv2
#import numpy as np

from selene.bys import by_xpath


class Product:

    def __init__(self, app):
        self.app = app

    def click_buy(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('button[data-prodid = "10312"]').click()

    def verify_title(self):
        wd = self.app.wd
        return wd.s('h1.product-title-h1 span').should(be.visible).text

    def verify_price(self):
        wd = self.app.wd
        assert "Price:" == wd.s('div[class="price-text pull-left"]').should(be.visible).text
        price = wd.s('span.product-price').text
        pattern = re.compile("^[0-9],[0-9]{3}.[0-9]{2}$")
        pattern.match(price)

    def verify_warranty(self):
        wd = self.app.wd
        assert "Warranty:" == wd.s("div.warranty-label").should(be.visible).text
        return wd.s("div.no-ext-warranty strong").should(be.visible).text

    def verify_sku(self):
        wd = self.app.wd
        assert "SKU: X7" == wd.s("#product-page-add-to-cart+div").should(be.visible).text

    def verify_section_image(self):
        wd = self.app.wd
        ''' a = cv2.imread("sample1.png")
        b = cv2.imread("sample2.png")
        difference = cv2.subtract(a, b)
        result = not np.any(difference)
        if result is True:
            print("Pictures are the same")
        open("image1.jpg", "rb").read() == open("image2.jpg", "rb").read()'''

    def verify_section_description(self):
        wd = self.app.wd
        assert "PRODUCT DESCRIPTION" == wd.s('form[action ="/cart/"]+br+h2.title span').should(be.visible).text
        return wd.s('h2.title+div p').should(be.visible).text

    def verify_section_specification(self):
        wd = self.app.wd
        assert "PRODUCT SPECIFICATIONS" == wd.s(by_xpath('(//h2[@class ="title"]/span)[2]')).should(be.visible).text
        assert "Brand" == wd.s(by_xpath('(//div[@class ="col-md-3"])[1]')).should(be.visible).text
        assert "Model" == wd.s(by_xpath('(//div[@class ="col-md-3"])[2]')).should(be.visible).text
        spec_brand = wd.s(by_xpath('(//div[@class ="col-md-9"])[1]')).should(be.visible).text
        spec_model = wd.s(by_xpath('(//div[@class ="col-md-9"])[2]')).should(be.visible).text
        result = (spec_brand, spec_model)
        return result

    def verify_section_similar(self):
        wd = self.app.wd
        assert "SIMILAR PRODUCTS" == wd.s('#similar-products-wrap h2.title > span').should(be.visible).text
        return wd.s(by_xpath('(//div[@class = "product-title"]/a)[1]')).should(be.visible).text

    def verify_section_product_review(self):
        wd = self.app.wd
        print(wd.s(by_xpath('(//h2[@class ="title"]/span)[3]')).should(be.visible).text)
        assert "PRODUCT REVIEWS" in wd.s(by_xpath('(//h2[@class ="title"]/span)[4]')).should(be.visible).text

    def verify_button_quantity(self):
        wd = self.app.wd
        assert "Quantity:" == wd.s(by_xpath('//div[@class = "col-md-3 grey-border"]//label')).should(be.visible)\
            .should(be.clickable).text

    def verify_button_buy(self):
        wd = self.app.wd
        assert "BUY NOW" in wd.s('button[data-prodid="10312"]').should(be.visible).should(be.clickable).text

    def verify_button_whishlist(self):
        wd = self.app.wd
        assert "Add To Wishlist" in wd.s('button[class = "btn btn-danger btn-sm btn-block add-to-wish-list"]')\
            .should(be.visible).should(be.clickable).text




