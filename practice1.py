import sys

def validate(x):
    try:
        n = int(x)
    except:
        print('must be integer')
        sys.exit()
    if n <= 0:
        print('must be positive')
        sys.exit()
    return n


def points(level):
    return sum(x for x in range(1, level+1))


def counter(level):
    upper_triangles = sum(points(x) for x in range(1, level+1))
    lowers = [0, 1]
    if level == 1:
        lower_triangles = 0
    elif level == 2:
        lower_triangles = 1
    else:
        for n in range (3, level+1):
            lowers.append(points(n-1)+lowers[n-3])
        lower_triangles = lowers[-1]
    return upper_triangles + lower_triangles


number = input("number of levels: ")
number = validate(number)

print('number of triangles: ', counter(number))
