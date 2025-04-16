import re
from model import Registrator
from view import OrderView

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

class Order:
    @classmethod
    def start(cls):
        RegistrationController.crate_account()
        OrderView.product_selection(["Pepperoni", "Margarita", "Four Cheeses", "Ham and Cheese", "Hawaiian"])

Order.start()
