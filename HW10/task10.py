import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
unique_lst = list(set(lst))
one_hot_lst = []
for value in lst:
    one_hot = [0] * len(unique_lst)
    index = unique_lst.index(value)
    one_hot[index] = 1
    one_hot_lst.append(one_hot)
data = pd.DataFrame(one_hot_lst, columns=unique_lst)

print(data.head())