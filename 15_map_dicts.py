items = [
    {
        'product': 'apple',
        'price': 10
    },
    {
        'product': 'banana',
        'price': 5
    },
    {
        'product': 'orange',
        'price': 8
    },
    {
        'product': 'pineapple',
        'price': 15
    }
]

# Map the list of dictionaries to a list of prices
prices = list(map(lambda item: item['price'], items))
print(prices)

def add_taxes(item):
    item['taxes'] = item['price'] * 0.16
    return item

new_items = list(map(add_taxes, items))
print(new_items)
