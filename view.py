class CheckGenerator:
    def __init__(self, busket: dict[str, list[int, int]]):
        self.__busket = busket
    def print_check(self):
        print("\n" + "=" * 30)
        for _ in self.__busket:
