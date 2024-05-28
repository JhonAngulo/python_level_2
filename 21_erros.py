#  print(0 / 0)) unexpected indent

# print(0 / 0)  ZeroDivisionError: division by zero

# print(result)
print('hola')
suma = lambda x, y: x + y
# suma = lambda x, y: x + y + 2 AssertionError
assert suma(2,2) == 4

print('adios')

age = 10    
if age < 18:
    raise Exception('No se permiten menores de edad') # Exception: No se permiten menores de edad


