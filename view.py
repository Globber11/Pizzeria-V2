class CheckGenerator:
    def __init__(self, busket: dict[str, list[int, int]]):
        self.__busket = busket
    def print_check(self):
        print("\n" + "=" * 30)
        for _ in self.__busket:
            print(f'{_} {self.__busket[_][1]}шт.')
        print(f'Total to pay: {sum(self.__busket[_][0] * self.__busket[_][1] for _ in self.__busket)}')
        print("=" * 30)
