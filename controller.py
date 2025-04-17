import re
from model import Registrator
from view import OrderView
import json

class DataChecker:
    @classmethod
    def check_date(cls, date):
        if re.match(r'^(?:(?:31\.(?:0[13578]|1[02])|(?:29|30)\.(?:0[13-9]|1[0-2]))\.\d{4}|(?:0[1-9]|1\d|2[0-8])\.(?:0[1-9]|1[0-2])\.\d{4}|29\.02\.(?:\d{2}(?:0[48]|[2468][048]|[13579][26])|(?:[02468][048]|[13579][26])00))$', date):
            return True
        return False

class RegistrationController:
    @classmethod
    def crate_account(cls):
        print('Приветствую тебя во второй версии пиццерии!\nДля начала тебе необходимо пройти регистрацию/авторизацию!')
        name = input('Введите ваше имя:')
        surname = input('Введите вашу фамилию:')
        phone_number = int(input('Введите ван номер телефона без + и пробелов:'))
        while True:
            try:
                born_date = input('Введите вашу дату рождения:')
                if not DataChecker.check_date(born_date):
                    raise ValueError
                break
            except:
                print('Дата введена неверно, попробуйте снова')
        Registrator.crate_account(name, surname, phone_number, born_date)

class StartProgramm:
    @classmethod
    def start(cls):
        if RegistrationController.crate_account() == 'Is admin':
            cls.admin_interface()
        else:
            cls.user_interface()

    @classmethod
    def user_interface(cls):
        products = cls.load_pizzas_from_json("products.json")
        OrderView.product_selection(products)
        while True:
            product_num = input("Введите цифру соответствующую вашему выбору: ")
            if product_num not in products.keys():
                print("Uncorrect num")
                continue
            break
        while True:
            try:
                product_quantity = int(input("Введите количество (макс 10): "))
                if 0 < product_quantity <= 10:
                    raise ValueError
            except ValueError:
                print("Uncorrect num")
                continue
            break

    @classmethod
    def admin_interface(cls):
        AdminView.admin_action_selection()
        action_num = int(input('Выберите номер действия: '))
        if action_num == 1:
            pass # Логи ожидают настойки
        elif action_num == 2:
            pass # Логи ожидают настойки
        elif action_num == 3:
            nums = {
                'Pepperoni': Pepperoni(),
                'Margarita': Margarita(),
                'FourCheeses': FourCheeses(),
                'HamCheese': HamCheese(),
                'Hawaiian': Hawaiian()
            }
            for _ in nums:
                print(f'{_} - {nums[_].price}')
        elif action_num == 4:
            with open('warehouse.json', 'r', encoding='utf-8') as file:
                poducts = file.read()
            print(poducts)

StartProgramm.start()
