from random import randint


def create_random_list(size: int) -> list:
    arr = []
    for _ in range(size):
        arr.append(randint(0, 20))

    return arr


def return_max_sum(arr: list) -> int:
    max = 0
    for i in range(1, len(arr) + 1):
        temp = arr[i - 1] + arr[i % len(arr)] + arr[(i + 1) % len(arr)]
        print(f'{i} : [{arr[i - 1]}, {arr[i % len(arr)]}, {arr[(i + 1) % len(arr)]}]')
        if temp > max:
            max = temp
            print(f'new max = {max}')

    return max

arr = create_random_list(10)
print(arr)
print(f'max = {return_max_sum(arr)}')