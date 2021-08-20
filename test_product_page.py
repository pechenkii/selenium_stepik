from .pages.product_page import *

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_basket() # добавляем товар в корзину
    page.solve_quiz_and_get_code() # вычисляем код и подставляем его в алерт
    page.should_be_product_in_message() # проверка, что в сообщении правильное название товара
    page.product_price_equals_basket_price() # проверка, что цена товара совпадает со стоимостьюб в корзине

