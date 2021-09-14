import sys


def left_cyclic_shift1(list_, k):
    for i in range(k):
        list_ = list_[1:] + [list_[0]]
    return list_


def left_cyclic_shift2(list_, k):
    k = k % len(list_)
    return list_[k:] + list_[:k]


def left_cyclic_shift3(list_, k):
    for i in range(k):
        list_.append(list_.pop(0))
    return list_


def validate(x):
    try:
        n = int(x)
    except:
        print('must be integer')
        sys.exit()
    if n < 0:
        print('must be positive')
        sys.exit()
    return n

array = []
quantity = input("Input quantity of the list: ")
quantity = validate(quantity)

for i in range(quantity):
    array.append(input(f"Input element {i+1}: "))
print(f"initial list: {array}")

k = input("Input k: ")
k = validate(k)


print("final list: ")
i = 1
for func in [left_cyclic_shift1, left_cyclic_shift2, left_cyclic_shift3]:
    print(f'method {i}: {func(array, k)}')
    i += 1



