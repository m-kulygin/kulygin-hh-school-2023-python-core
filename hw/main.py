import datetime

from wine import Wine
from beer import Beer
from market import Market

"""
TODO: Доработать заготовки классов вина (Wine), пива (Beer) и магазина (Market) таким образом, чтобы через класс Market можно было:

    * получить список всех напитков (вина и пива) отсортированный по наименованию
    * проверить наличие напитка в магазине (за время О(1))
    * получить список напитков (вина и пива) в указанном диапазоне даты производства
    * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
"""

# формируем магазин
wines = [Wine('wine2', datetime.date(2023, 1, 1)),
         Wine('wine3', datetime.date(2023, 1, 2)),
         Wine('wine1', datetime.date(2023, 1, 3))]
beers = [Beer('beer3', datetime.date(2023, 1, 4)),
         Beer('beer1', datetime.date(2023, 1, 5)),
         Beer('beer2', datetime.date(2023, 1, 6))]

market = Market(wines, beers)
print(str(market))

# получение и печать сортированного по названию списка напитков
sorted_drinks = market.get_drinks_sorted_by_title()
for drink in sorted_drinks:
    print(str(drink))

# проверка наличия напитка по названию
print(market.has_drink_with_title('wine3'))
print(market.has_drink_with_title('beer4'))

# получение напитков с датой производства в заданном диапазоне
dated_drinks = market.get_drinks_by_production_date(datetime.date(2023, 1, 2),
                                                    datetime.date(2023, 1, 5))
for drink in dated_drinks:
    print(str(drink))
