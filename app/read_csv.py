import csv

def read_csv(location_file):
    # Leer el archivo 'csv' fila x fila
    with open(location_file, 'r') as file:
        reader = csv.reader(file, delimiter = ',') # delimiter: Caracter que divide cada uno de los datos
        for row in reader:
            print('*' * 50) # Division de cada fila
            print(row)

# Para poder ejecutarlo como un script
if __name__ == '__main__':
    read_csv('./python_course/data.csv')