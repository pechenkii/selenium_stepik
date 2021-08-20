from .pages.product_page import *
import pytest

#@pytest.mark.parametrize('link', ["okay_link", pytest.param("bugged_link", marks=pytest.mark.xfail), "okay_link"])
@pytest.mark.parametrize('promo', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail(reason = "fixing this bug")), "8", "9"])
def test_guest_can_add_product_to_basket(browser,promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    page = ProductPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_basket() # добавляем товар в корзину
    page.solve_quiz_and_get_code() # вычисляем код и подставляем его в алерт
    page.should_be_product_in_message() # проверка, что в сообщении правильное название товара
    page.product_price_equals_basket_price() # проверка, что цена товара совпадает со стоимостьюб в корзине

