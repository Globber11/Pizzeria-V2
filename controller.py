import re
from model import Registrator, Warehouse
from view import OrderView, CheckGenerator, AdminView
import json
from model import Busket


class DataChecker:
    @classmethod
    def check_date(cls, date):
        if re.match(
                r'^(?:(?:31\.(?:0[13578]|1[02])|(?:29|30)\.(?:0[13-9]|1[0-2]))\.\d{4}|(?:0[1-9]|1\d|2[0-8])\.(?:0[1-9]|1[0-2])\.\d{4}|29\.02\.(?:\d{2}(?:0[48]|[2468][048]|[13579][26])|(?:[02468][048]|[13579][26])00))$',
                date):
            return True
        return False


class RegistrationController:
    @classmethod
    def crate_account(cls):
        print('Приветствую тебя во второй версии пиццерии!\nДля начала тебе необходимо пройти регистрацию/авторизацию!')
        name = input('Введите ваше имя:')
        if name == "admin":
            return "Is admin"
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


class Logger:
    @classmethod
    def create_log_file(cls):
        with open('logs/log_counter.txt', 'r') as f:
            log_num = f.read()
            if log_num == '':
                with open('logs/log_counter.txt', 'w') as f:
                    f.write("0")
        with open(f'logs/log {log_num}', 'x'):
            pass
        with open('logs/log_counter.txt', 'w') as f:
            f.write(str(int(log_num) + 1))
        return f'logs/log {log_num}'

    def create_log(self, log_file, log):
        with open(log_file, 'a') as f:
            f.write(log)


class Programm:
    log_file = 0

    @classmethod
    def start(cls):
        log_file = Logger.create_log_file()
        if RegistrationController.crate_account() == 'Is admin':
            cls.admin_interface()
        else:
            cls.user_interface()

    @classmethod
    def user_interface(cls):
        def load_pizzas_from_json(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    pizzas = json.load(file)
                return pizzas
            except FileNotFoundError:
                print(f"Ошибка: Файл '{file_path}' не найден.")
            except json.JSONDecodeError:
                print(f"Ошибка: Файл '{file_path}' содержит некорректный JSON.")
            except Exception as e:
                print(f"Неожиданная ошибка: {e}")
            return None

        products = load_pizzas_from_json("products.json")
        order_stop = False
        busket = Busket({})
        while True:
            OrderView.product_selection(products)
            while True:
                product_num = int(input("Введите цифру соответствующую вашему выбору: "))
                if product_num == 0:
                    order_stop = True
                    break
                elif str(product_num) not in products.keys():
                    print("Uncorrect num")
                    continue
                break
            if order_stop == True:
                break
            while True:
                try:
                    product_quantity = int(input("Введите количество (макс 10): "))
                    if product_quantity > 10 or product_quantity < 0:
                        raise ValueError
                except ValueError:
                    print("Uncorrect num")
                    continue
                break
            if Warehouse.availability_check(product_num, product_quantity):
                Warehouse.subtraction_from_warehouse(product_num, product_quantity)
                busket.add_to_busket(product_num, product_quantity)
            else:
                print(
                    "Продуктов для вашей пиццы не хватает на складе, попробуйте сделать другой заказ, либо измените количество")
                continue
        CheckGenerator.print_check(busket.get_busket())


    @classmethod
    def admin_interface(cls):
        AdminView.admin_action_selection()
        action_num = int(input('Выберите номер действия: '))
        if action_num == 1:
            pass  # Логи ожидают настойки
        elif action_num == 2:
            pass  # Логи ожидают настойки
        elif action_num == 3:
            for _ in range(1,6):
                print(f'{Warehouse.num_to_pizza(_).name} - {Warehouse.num_to_pizza(_).price}')
        elif action_num == 4:
            with open('warehouse.json', 'r', encoding='utf-8') as file:
                products = file.read()
            print(products)


Programm.start()
