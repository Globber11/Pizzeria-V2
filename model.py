from random import *
import json
from typing import Dict
from abc import ABC, abstractmethod
from typing import Union

class Registrator:
    @classmethod
    def crate_account(cls, name, surname, phone_number, born_date):
        def load_users():
            try:
                with open('accounts.json', 'r', encoding='utf-8') as file:
                    content = file.read()
                    if content.strip():
                        return json.loads(content)
                    return []
            except (FileNotFoundError, json.JSONDecodeError):
                return []

        def save_users(users_):
            with open('accounts.json', 'w', encoding='utf-8') as file:
                json.dump(users_, file, ensure_ascii=False, indent=4)

        users = load_users()

        seed(name + surname + str(phone_number) + str(born_date))
        ID = int(random() * 10 ** 15)
        for user in users:
            if user['ID'] == ID:
                return f'Авторизация завершена'
        account_data = {
            'ID': ID,
            'name': name,
            'last_name': surname,
            'phone_number': phone_number,
            'born_year': born_date
        }
        users.append(account_data)

        save_users(users)

class Pizza(ABC):
    @abstractmethod
    def __init__(self, name: str, ingredients: Dict[str, int], base_price: int):
        self._name = name
        self._ingredients = ingredients
        self._base_price = base_price

    @property
    def name(self) -> str:
        return self._name

    @property
    def ingredients(self) -> Dict[str, int]:
        return self._ingredients

    @property
    def price(self) -> int:
        return self._base_price

    @price.setter
    def price(self, value: int):
        if value >= 0:
            self._base_price = value
        else:
            raise ValueError("Price cannot be negative")

    def __str__(self):
        return f"{self._name} (Цена: {self._base_price}, Ингредиенты: {self._ingredients})"

class Margarita(Pizza):
    def __init__(self):
        super().__init__(
            name="Margarita",
            ingredients={"cheese": 100, "tomatoes": 200, "sauce": 50, "dough": 300},
            base_price=450
        )

class Pepperoni(Pizza):
    def __init__(self):
        super().__init__(
            name="Pepperoni",
            ingredients={"cheese": 150, "sauce": 50, "sausage": 70, "dough": 300},
            base_price=550
        )

class FourCheeses(Pizza):
    def __init__(self):
        super().__init__(
            name="Four Cheeses",
            ingredients={"cheese": 300, "sauce": 50, "dough": 300},
            base_price=600
        )

class HamCheese(Pizza):
    def __init__(self):
        super().__init__(
            name="Ham and Cheese",
            ingredients={"cheese": 150, "ham": 70, "sauce": 50, "dough": 300},
            base_price=500
        )

class Hawaiian(Pizza):
    def __init__(self):
        super().__init__(
            name="Hawaiian",
            ingredients={"chicken": 100, "pineapple": 70, "cheese": 100, "sauce": 50, "dough": 250},
            base_price=550
        )

class Busket:
    def __init__(self, busket: Dict[str, list[int, int]]):
        self.__busket = busket

    def add_to_busket(self, product: Union[Hawaiian, HamCheese, FourCheeses, Pepperoni, Margarita], quantity):
        name = product.name
        price = product.price
        if name in self.__busket.keys():
            self.__busket[name][1] += quantity # self.__busket[product][0] = price, self.__busket[product][1] = quantity
        else:
            self.__busket[name].append(price)
            self.__busket[name].append(quantity)

    def get_busket(self):
        return self.__busket

class Warehouse:
    def subtract_products(self, product, quantity):
        def load():
            try:
                with open('products.json', 'r', encoding='utf-8') as file:
                    content = file.read()
                    if content.strip():
                        return json.loads(content)
                    return []
            except (FileNotFoundError, json.JSONDecodeError):
                return []
        def edit(products_):
            for _ in products_:
                if _ == product:
                    products_[product] -= quantity
                    return products_
            return False
        def save(products_):
            with open('products.json', 'w', encoding='utf-8') as file:
                json.dump(products_, file, ensure_ascii=False, indent=4)
        products = edit(load())
        if products:
            save(products)
            return True
        else:
            return False

    def check_availability(self, number_product):
        if number_product == 1:
            pizza = Pepperoni()
            ingredients = pizza.ingredients
            for _ in ingredients:
                if self.subtract_products(_, ingredients[_]) == False:
                    return False
        elif number_product == 2:
            pizza = Margarita()
            ingredients = pizza.ingredients
            for _ in ingredients:
                if self.subtract_products(_, ingredients[_]) == False:
                    return False
        elif number_product == 3:
            pizza = FourCheeses()
            ingredients = pizza.ingredients
            for _ in ingredients:
                if self.subtract_products(_, ingredients[_]) == False:
                    return False
        elif number_product == 4:
            pizza = HamCheese()
            ingredients = pizza.ingredients
            for _ in ingredients:
                if self.subtract_products(_, ingredients[_]) == False:
                    return False
        elif number_product == 5:
            pizza = Hawaiian()
            ingredients = pizza.ingredients
            for _ in ingredients:
                if self.subtract_products(_, ingredients[_]) == False:
                    return False
        return True
