class Drink:
    def __init__(self, title=None, production_date=None):
        self.title = title
        self.production_date = production_date

    def __str__(self):
        return f'{self.title} {self.production_date}'