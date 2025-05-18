# Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики, такие как адрес, название и ассортимент товаров. Ваша задача — создать класс Store, который можно будет использовать для создания различных магазинов.

# Шаги:
# 1. Создай класс Store:
# - Атрибуты класса:
# name: название магазина.
# address: адрес магазина.
# items: словарь, где ключ - название товара, а значение - его цена. Например, {'apples': 0.5, 'bananas': 0.75}.
# - Методы класса:
# __init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для items`.
# Метод для добавления товара в ассортимент.
# Метод для удаления товара из ассортимента.
# Метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
# Метод для обновления цены товара.

# 2. Создай несколько объектов класса Store:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.

# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.

class Store():

    def __init__(self, name: str, address: float):
        self.name = name
        self.address = address
        self.items: dict[str, float] = {}

    def validate_price(self, price: float):
        try:
            return float(price)
        except ValueError:
            print("Цена должна быть числом!")

    def add_item(self, product_name: str, price: float):
        valid_price = self.validate_price(price)
        if valid_price is not None:
            self.items[str(product_name)] = float(price)

    def remove_item(self, product_name: str):
        if product_name in self.items:
            del self.items[product_name]
        else:
            print(f"Товар '{product_name}' не найден!")

    def get_price(self, product_name: str):
        return self.items.get(product_name)

    def update_price(self, product_name: str, new_price: float):
        if product_name not in self.items:
            print(f"Товар '{product_name}' не найден!")

        valid_price = self.validate_price(new_price)
        if valid_price is not None:
            self.items[product_name] = valid_price
