numbers = list(range(1, 21))
par_numbers = list(filter(lambda number : number % 2 == 0, numbers))

print(par_numbers)