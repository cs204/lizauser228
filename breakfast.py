menu = {
    "кофе": 20.00,
    "чай": 10.00,
    "булочка": 5.00,
    "салат": 30.40,
    "пирожное": 45.50,
}

order = []

while True:
    try:
        item = input("Блюдо: ").lower()

        if item in menu:
            order.append(menu[item])
        else:
            print(f"{item} not found")

    except EOFError:
        break

print(f"\nСумма: {sum(order):.2f}")
