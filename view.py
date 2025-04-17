from typing import Dict

class OrderView:
    @classmethod
    def product_selection(cls, product_names: Dict):
        print("Выберите продукт:")
        for _ in range(1,len(product_names)+1):
            print(f"\t{_}. {product_names[str(_)]}")
        print("\t0. Exit order")

class AdminView:
    @classmethod
    def admin_action_selection(cls):
        print('Добро пожаловать в систему администратор, выберите действие:')
        print('Доступные функции:    \n 1 - вывод логов    \n 2 - чистка логов    \n 3 - вывод данных пользователей    \n 4 - просмотр кол-ва продуктов на складе')

class CheckGenerator:
    @classmethod
    def print_check(cls, busket: dict[str, list[int]]):
        for _ in busket:
            print(f'{_} {busket[_][0]}rub x {busket[_][1]}шт.')
        print(f'Total to pay: {sum(busket[_][0] * busket[_][1] for _ in busket)}')
        print("=" * 30)
