"""CorelDRAW Graphics Suite X7 - 3 Users"""
"""This test checks product page on example CorelDRAW Graphics Suite X7 software
   on uae.microless.com online shop
   
   Check that product page have fields: product title, price, warranty, SKU
   Check that product page have sections: product image, product description,
   product specification, similar product, product reviews
   Check that product page have buttons: quantity selector, buy now, whishlist
   
   Verify functional:
   Select 3 items
   Make a purchase
   Open "You Cart"
   Assert that goods in You Cart matches with selected product description,
   assert that price displayed properly,
   assert that quantity displayed properly,
   assert that total cost for position calculated properly,
   assert that total cost of purchase calculated properly.
   Assert that click on button "Proceed to checkout" opens checkout page. 
   """


def test_product_page_fields(app):
    app.session.login(username="r4gnardi@gmail.com", password="xnj,znfr;bk")
    app.main.open_home_page()
    app.main.open_corel_draw_page()
    assert "CorelDRAW Graphics Suite X7" in app.product.verify_title()
    app.product.verify_price()
    assert "1 Year" in app.product.verify_warranty()
    app.product.verify_sku()

    app.product.verify_section_image()
    assert "Graphic design software Vector illustration" in app.product.verify_section_description()
    assert "CorelDRAW" in app.product.verify_section_specification()
    assert "X7 / #10312" in app.product.verify_section_specification()
    assert "CorelDRAW Home & Student Suite X7" in app.product.verify_section_similar()
    app.product.verify_section_product_review()

    app.product.verify_button_quantity()
    app.product.verify_button_buy()
    app.product.verify_button_whishlist()
    app.session.logout()


def test_corel_draw_purchase(app):
    app.session.login(username="r4gnardi@gmail.com", password="xnj,znfr;bk")
    app.main.open_product("CorelDRAW Graphics Suite X7")
    price = app.product.get_item_price()
    app.product.select_quantity(3)
    app.product.add_to_whishlist()
    app.product.buy_now()
    assert "CorelDRAW Graphics Suite X7" in app.your_cart.item_description()
    assert price == app.your_cart.item_price()
    assert 3 == app.your_cart.items_quantity()
    assert price*3 == app.your_cart.total_item_cost_for_position()
    assert price*3 == app.your_cart.total_cost()
    app.your_cart.open_checkout()
    assert "Checkout" in app.checkout.get_title()
    assert "Place an Order" in app.checkout.info()
    app.session.logout()

