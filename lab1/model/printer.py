class Printer:

    def __init__(self, name=None, price_in_UAH=0, speed_in_pages_per_minute=0):
        self.name = name
        self.price_in_UAH = price_in_UAH
        self.speed_in_pages_per_minute = speed_in_pages_per_minute

    def __repr__(self):
        return f"name: {self.name}, price: {self.price_in_UAH}, " \
               f"speed: {self.speed_in_pages_per_minute}"
