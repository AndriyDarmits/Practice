import random

list_of_elements = []

# Запитуємо та виводимо значення змінної n
n = int(input("Введіть значення n - "))
print(f"n={n}")

# Запитуємо та виводимо значення змінної t
t = float(input("Введіть значення t - "))
print(f"t={t}")

# Генеруємо список випадкових чисел у заданому діапазоні
i = 0
while i < n:
    list_of_elements.append(random.uniform(0, 1))
    i += 1

# Змінюємо порядок елементів списку у зворотній бік
list_of_elements.reverse()
total = 0

# Виводимо список
print(f"Список елементів - {list_of_elements}")

# Рахуємо суму многочлена
for i in list_of_elements:

    # Якщо елемент списку останній, то додаємо його до значення (за формулою завдання)
    if list_of_elements.index(i) == len(list_of_elements)-1:
        total += i

    # В інакшому випадку множимо точку на значення елементу масиву та підносимо до степення (за формулою завдання)
    else:
        total += i*t**n
    n -= 1

# Виводимо значення багаточлена
print(total)

