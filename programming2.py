from random import randint
import sys


def print_matrix(matrix, name=''):
    print(f"Matrix {name}:")
    for row in matrix:
        for item in row:
            print(f"{item}\t", end='')
        print()
    print()


def generate_new_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    new_matrix = [[0 for col in range(cols)] for row in range(rows)]
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                new_matrix[i][j] += matrix[k][j]
    return new_matrix


def int_and_posit_checking(x):
    try:
        temp_var = int(x)
    except:
        print('must be integer')
        sys.exit()
    if temp_var <= 0:
        print('must be positive')
        sys.exit()
    return temp_var


rows = input("Quantity of rows: ")
rows = int_and_posit_checking(rows)
cols = input("Quantity of columns: ")
cols = int_and_posit_checking(cols)

matrix = [[randint(0, 100) for col in range(cols)] for row in range(rows)]
print_matrix(matrix, 'previous matrix')
new_matrix = generate_new_matrix(matrix)
print_matrix(new_matrix, 'new matrix')

