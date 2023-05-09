"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture
def item_obj():
    return Item('name', 2, 12, )


def test_func(item_obj):
    assert item_obj.name == 'name'


def test_disc(item_obj):
    assert item_obj.apply_discount() == 1.6


def test_calc(item_obj):
    assert item_obj.calculate_total_price() == 24


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('abc') is None

def test_name():
    item = Item('СуперСмартфон', 100, 2)
    assert item.name == 'СуперСмартфон'


def calculate_total_price():
    assert calculate_total_price(3, 10) == 30
    assert calculate_total_price(5, 5) == 25
    assert calculate_total_price(10000, 20) == 200000


def apply_discount():
    assert apply_discount(100, 0.2) == 80
    assert apply_discount(50, 0.1) == 45
    assert apply_discount(100, 0) == 100
    assert apply_discount('100', 0.2) == None


def test_phone_price():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert phone.price == 120_000


def test_phone_number_of_sim():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert phone.number_of_sim == 2


def test__str__():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == "Смартфон"


def test__repr__():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


# def test__add__():
#     item1 = Item("Смартфон", 10000, 20)
#     item2 = Item("iPhone", 100_000, 10)
#     assert item1 + item2 == 30


def test_item_isinstance():
    # используется для проверки принадлежности объекта к определенному классу
    item = Item("test_name", 10.50, 5)
    assert isinstance(item, Item)


def test_item_issubclass():
    # используется для проверки, наследуется ли какой-либо класс от другого
    Phone = Item
    assert issubclass(Phone, Item)

def test_add_item_and_non_item():
    item1 = Item("apple", 2000, 2)
    with pytest.raises(TypeError):
        item1 + "смартфон"


