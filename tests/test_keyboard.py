import pytest
from src.keyboard import Keyboard


@pytest.fixture
def item_keyboard():
    return Keyboard("keyboardSamsung", 123456, 2)


def test_lang(item_keyboard):
    assert item_keyboard.language == "EN"


def test_change_lang(item_keyboard):
    item_keyboard.change_lang()
    assert item_keyboard.language == "RU"


def test_name_keyborad():
    name = 'Dark Project KD87A'
    assert name == 'Dark Project KD87A'


def test_price_keyboard():
    price = 9600
    assert price == 9600

def test_quantity_keyboard():
    quantity = 5
    assert quantity == 5


