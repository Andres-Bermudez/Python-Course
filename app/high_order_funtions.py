# Funcion de orden superior
def sum(number, funct):
    return number + funct 

# Funcion comun 
def numbers(number):
    return number + 2 

# Funcion de orden superior con lambdas
sum_v2 = lambda number, funct : number + funct

# Funcion lambda
numbers_v2 = lambda number : number + 2

print(sum_v2(5, numbers_v2(3)))