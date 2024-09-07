# Acceder al sistema operativo
import sys
print(sys.path)

# Trabajar con expresiones regulares
import re
text = "Numbers is : 3147686543, email: user@mail.com"

result = re.findall('[a-c]', text)
print(result)

# Acceder a la hora del dispositivo
import time
actual_time = time.localtime()
result = time.asctime(actual_time)
print(result)

# Colecciones
import collections
numbers = [1,1,1,1,2,2,2,3,3,4,4,4,4,4,5,5,6,6,6]

result = collections.Counter(numbers)
print(result)