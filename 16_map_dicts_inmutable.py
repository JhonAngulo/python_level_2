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
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * 0.16
    return new_item

new_items = list(map(add_taxes, items))
print('new')
print(new_items)

print('old')
print(items)