import pytest
from src.phone import Phone

phone1 = Phone("iPhone", 100_000, 10, 2)


def test_init():
    assert phone1.name == 'iPhone'
    assert phone1.price == 100_000
    assert phone1.quantity == 10
    assert phone1.number_of_sim == 2


def test_phone_quantity():
    phone = Phone('Nokia', 249.99, 20, 2)
    assert phone.quantity == 20


def test_repr():
    assert repr(phone1) == "Phone('iPhone', 100000, 10, 2)"


def test_str():
    assert str(phone1) == "iPhone", "SIM-карт должно быть целым числом больше нуля."


def test_phone_isinstance():
    # используется для проверки принадлежности объекта к определенному классу
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert isinstance(phone, Phone)


def test__add__():
    phone1 = Phone("Смартфон", 10000, 20, 2)
    phone2 = Phone("iPhone", 100_000, 10, 2)
    assert phone1 + phone2 == 30


def test_add_phone_and_non_phone():
    phone1 = Phone("nokia", 1300, 10, 1)
    with pytest.raises(TypeError):
        phone1 + "телефон"

