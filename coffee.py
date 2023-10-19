requiredAmount = 50
listBills = ["50", "20", "10", "5"]
change = 0

while(requiredAmount > 0):
    print(f"Нужная сумма: {requiredAmount}")
    coin = input("Вставьте монету: ")

    if coin in listBills:
       requiredAmount -= int(coin)

    if requiredAmount < 0:
        change = abs(requiredAmount)

    print(f"Ваша сдача: {change}")
