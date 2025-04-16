from random import *
import json

class Registrator:
    def crate_new_account(self, name, surname, phone_number, born_date):
        seed(name + surname + str(phone_number) + str(born_date))
        ID = int(random() * 10 ** 15)
        with open('acoounts.json', 'r', encoding='utf-8') as file:
            content = file.read()
            if content.strip():
                users = json.loads(content)
            else:
                users = []
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
        with open('acoounts.json', 'w', encoding='utf-8') as file:
            json.dump(users, file, ensure_ascii=False, indent=4)
        return f'Регистрация завершена'

class Pizza:
    def __init__(self, price: int, ingredients: dict[str, int], name: str):
        self.__name = name
        self.__ingredients = ingredients
        self.__price = price

    @property
    def get_price(self):
        return self.__price

    @get_price.setter
    def set_price(self):
        self.__price = price
        return self

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
