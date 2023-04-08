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

