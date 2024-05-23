def find_volume(length=1, width=1, depth=1):
    return length * width * depth, width, 'hola'

result = find_volume(10, 20, 3)
print(result)

result_2 = find_volume(width=10)
print(result_2)


print(result_2[0])

result, width, text = find_volume(width=20)
print(result, width, text)