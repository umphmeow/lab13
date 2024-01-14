import csv

# Функция для чтения CSV-файла и возвращения списка записей
def read_csv(file_path):
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        return []

def calculate_total_ticket_cost(data, age_median, age_range=5):
    total_cost = 0
    for row in data:
        if row['Age'] and float(row['Age']) >= age_median - age_range and float(row['Age']) <= age_median + age_range:
            total_cost += float(row['Fare'])
    return total_cost

def calculate_age_median(data):
    ages = [float(row['Age']) for row in data if row['Age']]
    return sorted(ages)[len(ages) // 2]

file_path = 'titanic.csv'
titanic_data = read_csv(file_path)

if not titanic_data:
    print("Произошла ошибка при чтении данных. Пожалуйста, проверьте файл и его структуру.")
else:
    median_age = calculate_age_median(titanic_data)
    total_ticket_cost = calculate_total_ticket_cost(titanic_data, median_age)
    print(f"Суммарная стоимость билетов взрослых в возрастном интервале {median_age - 5} - {median_age + 5} лет: ${total_ticket_cost:.2f}")
