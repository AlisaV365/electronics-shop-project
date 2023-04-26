from src.phone import Phone


phone1 = Phone("iPhone", 100_000, 10, 2)


def test_init():
    assert phone1.number_of_sim == 2

def test_phone_quantity():
    phone = Phone('Nokia', 249.99, 20, 2)
    assert phone.quantity == 20


def test_repr():
    assert repr(phone1) == "Phone('iPhone', 100000, 10, 2)"


def test_str():
    assert str(phone1) == "iPhone", "SIM-карт должно быть целым числом больше нуля."