import random

# Генерація масиву з 80 випадкових цілих чисел
array = [random.randint(-100, 100) for _ in range(80)]
print("Масив:")
print(array)
x = int(input("\nВведіть шуканий елемент: "))

# Перше входження
first_index = -1
for i in range(len(array)):
 if array[i] == x:
  first_index = i
 break

# Останнє входження (в окремому циклі)
last_index = -1
for i in range(len(array)):
 if array[i] == x:
  last_index = i
  
# Вивід результатів
if first_index != -1:
 print(f"\nПерше входження: індекс {first_index}")
 print(f"Останнє входження: індекс {last_index}")
else:
 print("\nЕлемент не знайдено в масиві")