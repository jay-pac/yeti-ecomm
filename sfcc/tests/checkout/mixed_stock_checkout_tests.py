from selenium import webdriver
from selenium.webdriver.common.by import By
from sfcc.pages.login.login_page import LoginPage
from sfcc.pages.product_page import ProductPage
from sfcc.pages.checkout_page import CheckoutPage
import unittest
import time


class MixOrderTests(unittest.TestCase):

    def tests_addtocart(self):
        """Test Scenario: 
        1. Login
        2. Add 3 Stock Glasseware products to Cart
        3. Click on Cart Icon to navigate to Cart Page
        4. Click on Checkout button
        6. Place order to complete
        7. Repeats Steps 2-6
        """
        base_url = 'https://Storefront:Yeti2017@staging-na-yeti.demandware.net/s/Yeti_US/en_US/login'
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get(base_url)

        cookie = {
            'domain': 'staging-na-yeti.demandware.net',
            'httpOnly': False,
            'name': 'consent-accepted',
            'path': '/',
            'secure': False,
            'value': 'true'}
        driver.add_cookie(cookie)
        driver.refresh()
        
        driver.maximize_window()
        
        lp = LoginPage(driver)
        pdp = ProductPage(driver)
        checkout = CheckoutPage(driver)
        lp.login('jason.pacitti011420@yeti.com', 'Tester456!')

        product_urls = [
            '/hard-coolers/roadie-20-cooler/YR20.html',
            '/drinkware/rambler-36-oz-bottle/YRAM36.html',
            '/drinkware/rambler-half-gallon-jug/YRAMHALFJUG.html']
        x = 1
        while x <= 3:
            for product_url in product_urls:
                driver.get('https://staging-na-yeti.demandware.net/s/Yeti_US/en_US' + product_url)
                pdp.addToCart()

            cart_url = 'https://staging-na-yeti.demandware.net/s/Yeti_US/en_US/cart'
            driver.get(cart_url)
            checkout.checkoutBtn()
            checkout.shippingBtn()
            checkout.accountPayment('111')
            order_number = driver.find_element(By.XPATH, '//p[@class="order-number"]//a').text
            print(order_number)

            x += 1

