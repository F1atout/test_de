purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]


def total_revenue(purchases):

    return sum(i['price'] * i['quantity'] for i in purchases)


def items_by_category(purchases):
    items = {}

    for i in purchases:
        items[i['category']] = items.get(i['category'], [])
        items[i['category']].append(i['item'])

    return items



def expensive_purchases(purchases, min_price):

    return list([i for i in purchases if i['price'] > min_price])




def average_price_by_category(purchases):
    average = {}

    for i in purchases:
        average[i['category']] = average.get(i['category'], [])
        average[i['category']].append(i['price'])

    return {a : sum(b)/len(b) for a, b in average.items()}


def most_frequent_category(purchases):
    a = sum(i['quantity'] for i in purchases if i['category'] == 'fruit')
    b = sum(i['quantity'] for i in purchases if i['category'] == 'dairy')
    c = sum(i['quantity'] for i in purchases if i['category'] == 'bakery')

    if max(a, b , c) == a:
        return 'fruit'
    elif max(a, b, c) == b:
        return 'dairy'
    else:
        return 'bakery'



print(
    f'Общая выручка: {total_revenue(purchases)}\n'
    f'Товары по категориям: {items_by_category(purchases)}\n'
    f'Покупки дороже 1.0: {expensive_purchases(purchases, 1)}\n'
    f'Средняя цена по категориям: {average_price_by_category(purchases)}\n'
    f'Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}'
)