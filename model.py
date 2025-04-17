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

class CustomPizza(Pizza):
    def __init__(self, name: str, ingredients: Dict[str, int], base_price: int):
        super().__init__(
            name=name,
            ingredients=ingredients,
            base_price=base_price
        )

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
    @classmethod
    def load_products_from_json(cls, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                products = json.load(file)
            return products
        except FileNotFoundError:
            print(f"Ошибка: Файл '{file_path}' не найден.")
        except json.JSONDecodeError:
            print(f"Ошибка: Файл '{file_path}' содержит некорректный JSON.")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")
        return None

    @classmethod
    def subtraction_from_warehouse(cls, pizza_num: int):
        nums = {
            1: Pepperoni(),
            2: Margarita(),
            3: FourCheeses(),
            4: HamCheese(),
            5: Hawaiian()
        }
        pizza = nums[pizza_num]
        data = cls.load_products_from_json("warehouse.json")
        for product_name in pizza.ingredients.keys():
            data[product_name] -= pizza.ingredients[product_name]
        cls.save_pizzas_to_json(data, "warehouse.json")

    @classmethod
    def save_pizzas_to_json(cls, products_dict, file_path, indent=4):
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(products_dict, file, ensure_ascii=False, indent=indent)
            print(f"Данные успешно сохранены в {file_path}")
            return True
        except Exception as e:
            print(f"Ошибка при сохранении файла: {e}")
            return False
