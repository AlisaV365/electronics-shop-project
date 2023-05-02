from src.item import Item


class KeyboardMixinLog():
    def __init__(self):
        self.language = None

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'
        return self


class Keyboard(Item, KeyboardMixinLog):
    def __init__(self, name: str, price: float, quantity: int, language='EN') -> None:
        super().__init__(name, price, quantity)
        self.language = language
