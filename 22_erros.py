try:
    print(0 / 0)
except ZeroDivisionError as error:
    print(error)

try:
    assert 1 != 1, '1 no es igual a 1'
except AssertionError as error:
    print(error)

try:
    age = 10    
    if age < 18:
        raise Exception('No se permiten menores de edad') # Exception: No se permiten menores de edad
except Exception as error:
    print(error)



print('hola')

# en un solo bloque

try:
    print(0 / 0)
    assert 1 != 1, '1 no es igual a 1'
    age = 10    
    if age < 18:
        raise Exception('No se permiten menores de edad') # Exception: No se permiten menores de edad
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)



print('hola')