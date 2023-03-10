from main_function import Item
import pytest


def test_item_init():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0