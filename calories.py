fruitDict = {
    'Apple': 130,
    'Avocado': 50,
    'Lime': 20,
}

fruit = input("Фрукт: ")

if fruit in fruitDict:
    print(f"Калории: {fruitDict.get(fruit)}")