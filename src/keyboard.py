from src import item


class MixinLanguage:
    __language = 'EN'

    @property
    def language(self):
        # Сеттер
        return self.__language

    @classmethod
    def change_lang(cls):
        # смена раскладки клавиатуры
        if cls.__language == 'EN':
            cls.__language = 'RU'
        else:
            cls.__language = 'EN'
        return cls


class Keyboard(item.Item, MixinLanguage):

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)

