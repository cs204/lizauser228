from datetime import datetime

months = {
    'январь': 1,
    'февраль': 2,
    'март': 3,
    'апрель': 4,
    'май': 5,
    'июнь': 6,
    'июль': 7,
    'август': 8,
    'сентябрь': 9,
    'октябрь': 10,
    'ноябрь': 11,
    'декабрь': 12
}

while True:
    try:
        date_str = input("Дата: ")

        if ' ' in date_str:
            date_parts = date_str.split(' ')
        elif '.' in date_str:
            date_parts = date_str.split('.')

        day = int(date_parts[0])
        year = int(date_parts[2])

        if date_parts[1] in months:
            month = int(months[date_parts[1].lower()])
        elif int(date_parts[1]) >= 1 and int(date_parts[1]) <= 12:
            month = int(date_parts[1])

        date = datetime(year, month, day)
        iso_date = date.date().isoformat()
        break
    except (ValueError, KeyError, IndexError):
        print("")

print(iso_date)