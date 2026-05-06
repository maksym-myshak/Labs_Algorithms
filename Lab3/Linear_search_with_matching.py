array = [5, -3, 12, -7, 0, 9, -1, 4, -6, 2,
 -8, 15, -10, 3, -2, 7, -4, 11, -9, 6,
 8, -5, 14, -12]

print("Масив:")
print(array)

# Перший елемент
first_element = array[0]
count = 0
for el in array:
 if el == first_element:
  count += 1
print("\nКількість елементів, які співпадають з першим:", count)