"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item_obj():
    return Item('name', 2, 12)


def test_func(item_obj):
    assert item_obj.name == 'name'


def test_disc(item_obj):
    assert item_obj.apply_discount() == 2


def test_calc(item_obj):
    assert item_obj.calculate_total_price() == 24


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('abc') is None


def calculate_total_price():
    assert calculate_total_price(3, 10) == 30
    assert calculate_total_price(5, 5) == 25
    assert calculate_total_price(2, 1000) == 2000


def apply_discount():
    assert apply_discount(100, 0.2) == 80
    assert apply_discount(50, 0.1) == 45
    assert apply_discount(100, 0) == 100
    assert apply_discount('100', 0.2) == None


def test_item_str():
    item = Item("Смартфон", 111, 2)
    assert str(item) == "Смартфон"

def test_item_repr():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000, 20)"
