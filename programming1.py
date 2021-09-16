import sys


def left_cyclic_shift(list_, k):
    k = k % len(list_)
    return list_[k:] + list_[:k]


def integer_checking(x):
    try:
        temp_var = int(x)
    except:
        print('must be integer')
        sys.exit()
    return temp_var


def full_checking(x, check_index):
    if check_index == 1:
       if integer_checking(x) < 0:
            print('must be positive')
            sys.exit()
       else:
           return integer_checking(x)

    else:
        return integer_checking(x)


int_array = []
quantity = input("Input quantity of the list: ")
quantity = full_checking(quantity, 1)

for i in range(quantity):
    element = (input(f"Input element {i+1}: "))
    element = full_checking(element, 2)
    int_array.append(element)

print(f"initial list: {int_array}")

k = input("Input k: ")
k = full_checking(k, 1)


print("final list: ")
print(left_cyclic_shift(int_array, k))
