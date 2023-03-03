import numpy as np

# 1
print('#1')
loaded_data = np.genfromtxt('minutes_n_ingredients.csv', dtype=int, names=True, delimiter=',')
print(loaded_data[:5])

from statistics import mean
from statistics import median
# 2
print('#2')
print(mean(loaded_data['id']))
print(min(loaded_data['id']))
print(max(loaded_data['id']))
print(median(loaded_data['id']))

#3
print('#3')
oasis = np.quantile(loaded_data['minutes'], 0.75)
print(oasis)
loaded_data['minutes'] = np.clip(loaded_data['minutes'], 0, oasis)
print(loaded_data)

#4
print('#4')
a = np.count_nonzero(loaded_data['minutes'] == 0)
print(a)
loaded_data['minutes'][loaded_data['minutes'] == 0] = 1
print(loaded_data[410:420])

#5
print('#5')
b = len(np.unique(loaded_data['id']))
print(b)

#6
print('#6')
c = len(np.unique(loaded_data['n_ingredients']))
print(c)
d = np.unique(loaded_data['n_ingredients'])
print(*d)

#7
print('#7')
d = loaded_data[loaded_data['n_ingredients'] < 6]
print(d[:20])

#8
print('#8')
loaded_data2 = loaded_data.flatten()
h = loaded_data['n_ingredients']/loaded_data['minutes']
print(max(h))

#9
print('#9')
loaded_data_sorted_desc = loaded_data[loaded_data['minutes']. argsort ()[::-1]]
print(mean(loaded_data_sorted_desc['n_ingredients'][:100]))

#10
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

#11
print('#11')
f = mean(loaded_data['n_ingredients'])
lena = np.count_nonzero(loaded_data['n_ingredients'] < f)
lena_all = len(loaded_data)
procent = lena / lena_all * 100
print(procent)



#12
print('#12')
new_data = np.loadtxt("minutes_n_ingredients.csv", delimiter=",", dtype=int, skiprows=1)
w = np.zeros((100000, 1), dtype=int)
new_data = np.hstack([new_data, w])
new_data[3][(new_data[2] < 6 ) & (new_data[1] < 21 )] = 1
print(new_data[:50])


#13
print('#13')
simple = np.count_nonzero(new_data[3] > 0)
lena_new = len(new_data)
procent_simple = simple / lena_new * 100
print(procent_simple)


#14
print('#14')
bitch = np.zeros((100000, 1), dtype=int)
new_data = np.hstack([bitch, new_data])
print(new_data[:5])
new_data[0][(new_data[2] <= 10 )] = 1
new_data[0][(new_data[2] > 10 ) & (new_data[1] < 20 )] = 2
new_data[0][(new_data[2] >= 20 )] = 3
print(new_data[:5])