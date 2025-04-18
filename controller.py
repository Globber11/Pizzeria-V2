import re
from model import Registrator, Warehouse
from view import OrderView, CheckGenerator, AdminView
import json
from model import Busket, CustomPizzaBuilder, CustomPizza


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
        with open(f'logs/log {log_num}.txt', 'x'):
            pass
        with open('logs/log_counter.txt', 'w') as f:
            f.write(str(int(log_num) + 1))
        return f'logs/log {log_num}.txt'

    def create_log(cls, log):
        with open('logs/log_counter.txt', 'r') as f:
            log_num = f.read()
        with open(f'logs/log {log_num}.txt', 'a') as f:
            f.write(log)


class UserInterface:
    @staticmethod
    def load_from_json(file_path):
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

    @classmethod
    def run(cls):
        products = cls.load_from_json("products.json")
        order_stop = False
        busket = Busket({})

        while True:
            OrderView.product_selection(products)
            while True:
                try:
                    product_num = int(input("Введите цифру соответствующую вашему выбору: "))
                    if product_num == 0:
                        order_stop = True
                        break
                    if product_num == 6:
                        break
                    elif str(product_num) not in products.keys():
                        print("Uncorrect num")
                        continue
                    break
                except ValueError:
                    print("Пожалуйста, введите число")

            if order_stop:
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
            if product_num == 6:
                pizza_obj = cls.create_custom_pizza()
            else:
                pizza_obj = Warehouse.num_to_pizza(product_num)
            if Warehouse.availability_check(pizza_obj, product_quantity):
                Warehouse.subtraction_from_warehouse(pizza_obj, product_quantity)
                busket.add_to_busket(pizza_obj, product_quantity)
            else:
                print("Продуктов для вашей пиццы не хватает на складе, попробуйте сделать другой заказ, либо измените количество")
                continue

        CheckGenerator.print_check(busket.get_busket())

    @classmethod
    def create_custom_pizza(cls) -> CustomPizza:
        order_stop = False
        custom_pizza = CustomPizzaBuilder()
        ingredients_name = cls.load_from_json("ingredients_name.json")
        while True:
            OrderView.ingredient_selection(ingredients_name)
            while True:
                try:
                    product_num = int(input("Введите цифру соответствующую вашему выбору: "))
                    if product_num == 0:
                        order_stop = True
                        break
                    elif product_num > len(ingredients_name)+1:
                        print("Uncorrect num")
                        continue
                    break
                except ValueError:
                    print("Пожалуйста, введите число")

            if order_stop:
                break

            while True:
                try:
                    product_quantity = int(input("Введите количество (макс 20): "))
                    if product_quantity > 20 or product_quantity <= 0:
                        raise ValueError
                except ValueError:
                    print("Uncorrect num")
                    continue
                break
            custom_pizza.add_ingredients(ingredients_name[str(product_num)], product_quantity)
        return custom_pizza.build()






class AdminInterface:
    @classmethod
    def run(cls):
        AdminView.admin_action_selection()
        action_num = int(input('Выберите номер действия: '))
        if action_num == 1:
            pass  # Логи ожидают настойки
        elif action_num == 2:
            pass  # Логи ожидают настойки
        elif action_num == 3:
            for _ in range(1, 6):
                print(f'{Warehouse.num_to_pizza(_).name} - {Warehouse.num_to_pizza(_).price}')
        elif action_num == 4:
            with open('warehouse.json', 'r', encoding='utf-8') as file:
                products = file.read()
            print(products)


class Program:
    log_file = 0

    @classmethod
    def start(cls):
        log_file = Logger.create_log_file()
        if RegistrationController.crate_account() == 'Is admin':
            AdminInterface.run()
        else:
            UserInterface.run()
