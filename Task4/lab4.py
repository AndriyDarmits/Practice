# Вводимо необхідні слова
word_a = input("Введіть перше слово - ")
word_b = input("Введіть друге слово - ")

list_of_letters = []

# Шукаємо букви які є у першому слові, але немає у другому
for i in word_a:
    if i not in word_b:
        list_of_letters.append(i)

# Шукаємо букви які є у другому слові, але немає у першому
for i in word_b:
    if i not in word_a:
        list_of_letters.append(i)

print(list_of_letters)
