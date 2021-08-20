from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BTN_ADD_BASKET = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_IN_MESSAGE = (By.TAG_NAME, ".alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1) .alertinner>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRICE_BASKET = (By.CSS_SELECTOR, ".alertinner p:first-child strong")