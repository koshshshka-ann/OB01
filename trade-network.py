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

    # Инициация объекта
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.items: dict[str, float] = {}

    # Проверка цены (значение, тип данных)
    def validate_price(self, price: float):
        try:
            if price <= 0:
                raise ValueError("Цена должна быть больше 0!")
            return float(price)
        except (TypeError, ValueError):
            print("Цена должна быть положительным числом!")
            return None

    # Добавление товара
    def add_item(self, product_name: str, price: float):
        valid_price = self.validate_price(price)
        if valid_price is not None:
            self.items[str(product_name)] = float(price)

    # Удаление товара
    def remove_item(self, product_name: str):
        if product_name in self.items:
            del self.items[product_name]
        else:
            print(f"\nТовар '{product_name}' не найден!")

    # Получение цены товара по его названию
    def get_price(self, product_name: str):
        gotten_price = self.items.get(product_name)
        if gotten_price is not None:
            print(f"\nЦена на '{product_name}': {gotten_price}")
        else:
            print(f"\nТовар '{product_name}' не найден!")
        return gotten_price

    # Изменение цены
    def update_price(self, product_name: str, new_price: float):
        if product_name in self.items:
            valid_price = self.validate_price(new_price)
            if valid_price is not None:
                self.items[product_name] = valid_price
                print(f"\nНовая цена на '{product_name}': {valid_price}")
        else:
            print(f"\nТовар '{product_name}' не найден!")

# === Создание объектов ===

# Объект 1
store1 = Store("Свежие продукты", "г. Москва, ул. Строителей, д.12")
store1.items = {
    "Хлеб свежий": 75.00,
    "Молоко свежее": 130.00
}

# Объект 2
store2 = Store("Питерские фрукты", "г. С.-Петербург, Невский пр-т, д.50")
store2.items = {
    "Бананы из Питера": 100.00,
    "Ананасы из Питера": 250.00
}

# Объект 3
store3 = Store("Крутой гастроном", "г. Казань, ул. Садовая, д.19")
store3.items = {
    "Колбаса отменная": 500.00,
    "Сосиски шикарные": 275.00
}

# Вывод информации о созданных объектах
print(f"\nНазвание: '{store1.name}',\nАдрес: {store1.address},\nТовары в наличии: {store1.items}")
print(f"\nНазвание: '{store2.name}',\nАдрес: {store2.address},\nТовары в наличии: {store2.items}")
print(f"\nНазвание: '{store3.name}',\nАдрес: {store3.address},\nТовары в наличии: {store3.items}")

# === Тестирование Объекта 1 ===

# Добавление товара
store1.add_item("Масло свежее", 250.00) # Корректное добавление
store1.add_item("Кефир свежий", 150.00) # Корректное добавление
store1.add_item("Баклажан свежий", -150.00) # НЕ корректное добавление (отрицательное число)
store1.add_item("Артишок свежий", "150.00 рублей") # НЕ корректное добавление (не число)
store1.add_item("Эскалоп свежий", 0) # НЕ корректное добавление (число равно 0)
print(f"\nТовары в магазине '{store1.name}' в наличии: {store1.items}")

# Удаление товара
store1.remove_item("Молоко свежее") # Корректное удаление
store1.remove_item("Мандарины свежие") # НЕ корректное удаление (такой товар отсутствует)
print(f"\nТовары в магазине '{store1.name}' в наличии: {store1.items}")

# Получение цены товара по его названию
store1.get_price("Хлеб свежий") # Корректное получение
store1.get_price("Баклажан свежий") # НЕ корректное получение (такой товар отсутствует)

# Изменение цены
store1.update_price("Хлеб свежий", 85.00) # Корректное изменение
store1.update_price("Масло свежее", 0.00) # НЕ корректное изменение (неверное значение цены)
store1.update_price("Артишок свежий", 185.00) # НЕ корректное изменение (такой товар отсутствует)