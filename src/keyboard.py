from src.item import Item

class MixinLanguage:
    __language = 'EN'

    @property
    def language(self):
        # Сеттер
        return self.__language

    def change_lang(self):
        # смена раскладки клавиатуры
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self

class KeyBoard(Item, MixinLanguage):

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)

