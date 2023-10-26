while True:
    try:
        fraction = input("Дробь: ")
        x, y = map(int, fraction.split('/'))

        if y == 0:
            raise ZeroDivisionError
        if x > y or type(x) is not int or type(y) is not int:
            raise ValueError
        break

    except ValueError:
        print("Invalid input. Please enter a valid expression")

    except ZeroDivisionError:
        print("Invalid input. Please enter a valid second number")

result = round(x / y * 100)

if result <= 1:
    print("E")
elif result >= 99:
    print("F")
else:
    print(f"{result}%")
