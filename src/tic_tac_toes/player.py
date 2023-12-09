class Player:
    def __init__(self, symbol):
        self._name = None
        self._symbol = symbol

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def get_symbol(self):
        return self._symbol
