import csv


def cls(param, param1, param2):
    pass


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else f'Файл item.csv поврежден'

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    all = []

    def __init__(self):
        self.name = None
        self.price = None
        self.quantity = None

    @staticmethod
    def string_to_number(str_num):
        try:
            num = float(str_num)
        except ValueError:
            return None
        if num.is_integer():
            return int(num)
        return int(num)

    @classmethod
    def instantiate_from_csv(cls):
        """
        данные из csv-файла.
        """
        cls.all.clear()

    try:
        with open('/Users/alisavorotnikova/project4/electronics-shop-project/src/items.csv', 'r', encoding="cp1251",
                  newline='', ) as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    cls(row['name'], row['price'], row['quantity'])
                except:
                    raise InstantiateCSVError
    except FileNotFoundError:
        raise FileNotFoundError('Отсутствует файл items.csv')

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создаем экземпляры класса item.
        name: Название товара.
        price: Цена за единицу товара.
        quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        #  метод для отображения информации об объекте класса для разработчиков
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        #  метод для отображения информации об объекте класса для пользователей
        return self.__name

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(type(self), type(other)))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        """
    Наименование товара, проверяем, что длина наименования товара не больше 10 символов.
    """
        if len(value) > 10:
            raise ValueError("Длина наименования товара превышает 10 символов")
        else:
            self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитываем общую стоимость товара в магазине.
        Возвращаем общую стоимость товара.
       """
        return self.quantity * self.price

    def apply_discount(self):
        self.pay_rate = 0.8
        return self.price * self.pay_rate
        """
       скидка для конкретного товара.
       """
