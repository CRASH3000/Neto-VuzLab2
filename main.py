def input_prices_for_shop(shop_name, items):
    print(f"Введите цены для магазина {shop_name}:")
    prices = {}
    for item in items:
        # запросим цену каждого товара для текущего магазина
        price = float(input(f"Цена для {item}: "))
        prices[item] = price
    return prices

def calculate_total_cost(prices):
    # функция просто суммирует все цены из переданного словаря
    return sum(prices.values())

def main():
    items = ["яблоки", "бананы", "хлеб"]
    shops = ["Магазин1", "Магазин2", "Магазин3"]

    # словарь для хранения данных по каждому магазину
    shop_data = {}

    # запрашиваем цены для каждого магазина
    for shop in shops:
        prices = input_prices_for_shop(shop, items)
        shop_data[shop] = prices

    # вычисляем и выводим общую стоимость для каждого магазина
    costs = {}
    for shop, prices in shop_data.items():
        total_cost = calculate_total_cost(prices)
        costs[shop] = total_cost
        print(f"Общая стоимость в {shop}: {total_cost} руб.")

    # находим магазин с минимальной стоимостью
    cheapest_shop = min(costs, key=costs.get)
    print(f"Самые дешевые покупки в {cheapest_shop}!")

if __name__ == "__main__":
    main()
