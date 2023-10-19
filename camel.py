camelCase = input('Верблюжий стиль: ')
snake_case = ''

for letter in camelCase:
    if letter.isupper():
        snake_case += "_" + letter.lower()
    else:
        snake_case += letter

print(snake_case)