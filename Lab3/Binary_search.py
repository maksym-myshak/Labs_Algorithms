import random

# ---------- ШВИДКЕ СОРТУВАННЯ ----------
def quicksort(arr):
 if len(arr) <= 1:
  return arr
 pivot = arr[len(arr) // 2]
 left = []
 middle = []
 right = []
 for x in arr:
  if x < pivot:
   left.append(x)
  elif x > pivot:
   right.append(x)
  else:
   middle.append(x)
 return quicksort(left) + middle + quicksort(right)

# ---------- БІНАРНИЙ ПОШУК ----------
def binary_search(array, x):
 left = 0
 right = len(array) - 1
 while left <= right:
  mid = (left + right) // 2
  if array[mid] == x:
   return mid
  elif array[mid] < x:
   left = mid + 1
  else:
   right = mid - 1
 return -1

# ---------- ГОЛОВНА ПРОГРАМА ----------
# Генерація масиву з 100 випадкових чисел
array = [random.randint(-100, 100) for _ in range(100)]
print("Початковий масив:")
print(array)

# Сортування
sorted_array = quicksort(array)
print("\nВідсортований масив:")
print(sorted_array)

# Ввід числа
x = int(input("\nВведіть шуканий елемент: "))
# Бінарний пошук

index = binary_search(sorted_array, x)
if index != -1:
 print(f"Елемент {x} знайдено на індексі: {index}")
else:
 print("Елемент не знайдено")