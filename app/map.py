animals = ["cow", "chicken", "pig"]

numbers = list(range(1, 10))
numbers2 = list(range(11, 20))

transform = list(map(lambda animal : f"{animal} : cook", animals))
result = list(map(lambda x, y : x + y, numbers, numbers2))

# print(transform)
# print(result)

items = [
  {
    'product': 'camisa',
    'price': 100,
    'taxes': 0.19
  },
  {
    'product': 'pantalones',
    'price': 300,
    'taxes': 0.19
  },
  {
    'product': 'sueters',
    'price': 200,
    'taxes': 0.19
  }
]

def price_taxes(item):
    item["price"] *= item["taxes"]
    return int(item["price"])

prices = list(map(price_taxes, items))
print(prices)
