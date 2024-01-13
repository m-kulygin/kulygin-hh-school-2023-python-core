from datetime import datetime


def started_decorator(function):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        print(f'Function {function.__name__} started at: ' + str(start))
        wrap_result = function(*args, **kwargs)
        finish = datetime.now()
        print('Finished at: ' + str(finish) + '. Execution time: ' + str(finish-start))
        return wrap_result
    return wrapper


class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        drinks = wines + beers
        self.drinks = {}
        for drink in drinks:
            self.drinks[drink.title] = drink

    def __str__(self):
        return 'MARKET: ' + ', '.join('{}'.format(drink) for drink in self.drinks.values())

    @started_decorator
    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)

        :param title:
        :return: True|False
        """
        return title in self.drinks

    @started_decorator
    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        sorted_keys = sorted(self.drinks.keys())
        result = []
        for key in sorted_keys:
            result.append(self.drinks[key])
        return result

    @started_decorator
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        result = []
        for drink in self.drinks.values():
            if from_date <= drink.production_date <= to_date:
                result.append(drink)
        return result
