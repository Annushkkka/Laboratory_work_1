# Лабораторная работа №1

import numpy as np

# 1.Файл minutes_n_ingredients.csv содержит информацию об идентификаторе рецепта,
# времени его выполнения в минутах и количестве необходимых ингредиентов.
# Считайте данные из этого файла в виде массива numpy типа int32, используя np.loadtxt.
# Выведите на экран первые 5 строк массива.
print('#1')
loaded_data = np.genfromtxt('minutes_n_ingredients.csv', dtype=int, names=True, delimiter=',')
print(loaded_data)

# 2. Вычислите среднее значение, минимум, максимум и медиану по каждому из столбцов, кроме первого.
print('#2')
from statistics import mean
from statistics import median
print(mean(loaded_data['id']))
print(min(loaded_data['id']))
print(max(loaded_data['id']))
print(median(loaded_data['id']))

# 3. Ограничьте сверху значения продолжительности выполнения рецепта значением квантиля  q0.75 .
print('#3')
q = np.quantile(loaded_data['minutes'], q=0.75)
loaded_data['minutes'] = loaded_data['minutes'].clip(max=q)
print(loaded_data)

# 4. Посчитайте, для скольких рецептов указана продолжительность, равная нулю.
# Замените для таких строк значение в данном столбце на 1.
print('#4')
a = np.count_nonzero(loaded_data['minutes'] == 0)
print(a)
loaded_data['minutes'][loaded_data['minutes'] == 0] = 1
print(loaded_data)

# 5. Посчитайте, сколько уникальных рецептов находится в датасете.
print('#5')
unique_data = len(np.unique(loaded_data['id']))
print(unique_data)

# 6. Сколько и каких различных значений кол-ва ингредиентов присутвует в рецептах из датасета?
print('#6')
count_ingr = len(np.unique(loaded_data['n_ingredients']))
print(count_ingr)
un_ingr = np.unique(loaded_data['n_ingredients'])
print(*un_ingr)

# 7. Создайте версию массива, содержащую информацию только о рецептах, состоящих не более чем из 5 ингредиентов.
print('#7')
short_data = loaded_data[loaded_data['n_ingredients'] < 6]
print(short_data)

# 8. Для каждого рецепта посчитайте, сколько в среднем ингредиентов приходится на одну минуту рецепта.
# Найдите максимальное значение этой величины для всего датасета.
print('#8')
loaded_data2 = loaded_data.flatten()
h = loaded_data['n_ingredients']/loaded_data['minutes']
print(max(h))

# 9. Вычислите среднее количество ингредиентов для топ-100 рецептов с наибольшей продолжительностью.
print('#9')
loaded_data_sorted_desc = loaded_data[loaded_data['minutes']. argsort ()[::-1]]
print(mean(loaded_data_sorted_desc['n_ingredients'][:100]))

# 10. Выберите случайным образом и выведите информацию о 10 различных рецептах.
print('#10')
import random
print(loaded_data[random.randint(0,99999)])
print(loaded_data[random.randint(0,99999)])
print(loaded_data[random.randint(0,99999)])
print(loaded_data[random.randint(0,99999)])
print(loaded_data[random.randint(0,99999)])
print(loaded_data[random.randint(0,99999)])
print(loaded_data[random.randint(0,99999)])
print(loaded_data[random.randint(0,99999)])
print(loaded_data[random.randint(0,99999)])
print(loaded_data[random.randint(0,99999)])

# 11. Выведите процент рецептов, кол-во ингредиентов в которых меньше среднего.
print('#11')
f = mean(loaded_data['n_ingredients'])
lena = np.count_nonzero(loaded_data['n_ingredients'] < f)
lena_all = len(loaded_data)
procent = lena / lena_all * 100
print(procent)



# 12. Назовем "простым" такой рецепт, длительность выполнения которого не больше 20 минут и кол-во
# ингредиентов в котором не больше 5. Создайте версию датасета с дополнительным столбцом, з
# начениями которого являются 1, если рецепт простой, и 0 в противном случае.
print('#12')
new_data = np.loadtxt("minutes_n_ingredients.csv", delimiter=",", dtype=int, skiprows=1)
w = np.zeros((100000, 1), dtype=int)
new_data = np.hstack([new_data, w])
new_data[3][(new_data[2] < 6 ) & (new_data[1] < 21 )] = 1
print(new_data)


# 13. Выведите процент "простых" рецептов в датасете.
print('#13')
simple = np.count_nonzero(new_data[3] > 0)
lena_new = len(new_data)
procent_simple = simple / lena_new * 100
print(procent_simple)


# 14. Разделим рецепты на группы по следующему правилу. Назовем рецепты короткими,
# если их продолжительность составляет менее 10 минут; стандартными,
# если их продолжительность составляет более 10, но менее 20 минут;
# и длинными, если их продолжительность составляет не менее 20 минут.
# Создайте трехмерный массив, где нулевая ось отвечает за номер группы
# (короткий, стандартный или длинный рецепт), первая ось - за сам рецепт
# и вторая ось - за характеристики рецепта. Выберите максимальное количество рецептов
# из каждой группы таким образом, чтобы было возможно сформировать трехмерный массив.
# Выведите форму полученного массива.
print('#14')
bitch = np.zeros((100000, 1), dtype=int)
new_data = np.hstack([bitch, new_data])
print(new_data[:5])
new_data[0][(new_data[2] <= 10 )] = 1
new_data[0][(new_data[2] > 10 ) & (new_data[1] < 20 )] = 2
new_data[0][(new_data[2] >= 20 )] = 3
print(new_data)