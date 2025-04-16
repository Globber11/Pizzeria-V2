from random import *
import json
from typing import Dict
from abc import ABC, abstractmethod

class Registrator:
    def crate_account(self, name, surname, phone_number, born_date):
        def load_users():
            try:
                with open('acoounts.json', 'r', encoding='utf-8') as file:
                    content = file.read()
                    if content.strip():
                        return json.loads(content)
                    return []
            except (FileNotFoundError, json.JSONDecodeError):
                return []

        def save_users(users_):
            with open('acoounts.json', 'w', encoding='utf-8') as file:
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

class Basket:
    def __init__(self, basket: Dict[str, int]):
        self.__basket = basket

    def add_to_basket(self, product, quantity):
        if product in self.__basket.keys():
            self.__basket[product] += quantity
        else:
            self.__basket[product] = quantity
            
    @property
    def basket(self):
        return self.__basket
