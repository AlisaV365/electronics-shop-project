import csv


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    all = []

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
        with open('../src/items.csv', 'r', encoding="cp1251", newline='', ) as f:
            reader = csv.DictReader(f)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

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

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Нельзя сложить Phone или Item с экземплярами не Phone или Item классов.')
        return self.quantity + other.quantity


    def __repr__(self):
        #  метод для отображения информации об объекте класса для разработчиков
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        #  метод для отображения информации об объекте класса для пользователей
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        """
    Наименование товара, проверяем, что длина наименования товара не больше 10 символов.
    """
        if len(value) > 10:
            print("Длина наименования товара превышает 10 символов")
        else:
            self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитываем общую стоимость товара в магазине.
        Возвращаем общую стоимость товара.
       """
        return self.quantity * self.price

    def apply_discount(self):
        return self.price * self.pay_rate
        """
       скидка для конкретного товара.
       """





