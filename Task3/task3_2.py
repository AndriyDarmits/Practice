import random

n = len('Андрій')

m = len("Дарміць")

# Генеруємо масив
array = []
for i in range(m):
    array.append([])
    for j in range(n):
        array[i].append(random.randint(-10, 10))

print(f"Масив - {array}")

negative_elements = []

# Записуємо усі відємні значення другого рядка масиву у список
for i in array[1]:
    if i < 0:
        negative_elements.append(i)

print(f"Список усіх відємних значень другого рядка масиву - {negative_elements}")

# Шукаємо добуток усіх відємних значень другого рядка масиву у список
for i in range(len(negative_elements)):
    if i == 0:
        product = negative_elements[i]
    else:
        product *= negative_elements[i]

print(f"Добуток усіх відємних значень другого рядка масиву = {product}")

# Шукаємо кількість числел у другому стовпці не кратні 5
count = 0
for i in array:
    if i[1] % 5 != 0:
        count += 1

print(f"Кількість числел у другому стовпці не кратні 5 - {count}")

