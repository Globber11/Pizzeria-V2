class Pizza:
    def __init__(self, price: int, ingredients: dict[str, int], name: strпппп):
        self.__name = name
        self.__ingredients = ingredients
        self.__price = price

    @property
    def get_price(self):
        return self.__price

    @get_price.setter
    def set_price(self):
        return self.__price

class Margarita(Pizza):
    pass

class Pepperoni(Pizza):
    pass

class FourCheeses(Pizza):
    pass

class HamCheese(Pizza):
    pass

class Hawaiian(Pizza):
    pass
