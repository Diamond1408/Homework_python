import pandas as pd
import random
# генерируем исходный список
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
# создаем уникальный список значений
unique_lst = list(set(lst))
# создаем пустой список для one-hot представления
one_hot_lst = []
# создаем one-hot представление для каждого значения списка lst
for value in lst:
    one_hot = [0] * len(unique_lst)
    index = unique_lst.index(value)
    one_hot[index] = 1
    one_hot_lst.append(one_hot)
# создаем DataFrame из списка one-hot представлений
data = pd.DataFrame(one_hot_lst, columns=unique_lst)
# выводим результат
print(data.head())