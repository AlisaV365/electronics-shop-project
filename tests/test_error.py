from src.item import InstantiateCSVError, Item
import pytest

"""проверяем, что при инициализации объекта `InstantiateCSVError` будет возвращаться str"""


def test_instantiate_from_csv_str():
    csv_error = InstantiateCSVError()
    assert str(csv_error) == 'Файл item.csv поврежден'


"""если файл `items.csv`, из которого по умолчанию считываются данные, 
не найден → выбрасывается исключение `FileNotFoundError` с сообщением “_Отсутствует файл item.csv_" """


def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()
        raise FileNotFoundError("Отсутствует файл items.csv")


"""если файл `item.csv` поврежден (например, отсутствует одна из колонок данных) → выбрасывается 
исключение `InstantiateCSVError` с сообщением “_Файл item.csv поврежден_” """


def test_instantiate_from_csv_error():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()
        raise InstantiateCSVError
