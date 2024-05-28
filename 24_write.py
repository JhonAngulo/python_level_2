
with open('./text.txt', 'r+') as file:
    for line in file:
        print(line)
    file.write('\n')
    file.write('This is a new line\n')
    file.write('Other line\n')


# con este permiso se sobre escribe el archivo

# with open('./text.txt', 'w+') as file:
#     for line in file:
#         print(line)
#     file.write('\n')
#     file.write('This is a new line\n')
#     file.write('Other line\n')