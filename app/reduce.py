from functools import reduce

numbers = list(range(1, 5))

result = reduce(lambda counter, number : counter + number, numbers)
print(result)