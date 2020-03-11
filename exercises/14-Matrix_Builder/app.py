import random

complete_array = []
# adds to empty array a given number of times
# def repeat(example):
#     for x in example:
#         complete_array.append(example)

# provides random array of 1 and 0 values depending on the number given (numbr of digits in array)

def function_caller(x,y):
    temp = []
    for x in range(x):
        # print('asdfasdf')
        temp.append(random_matrix_maker(y))
    return(temp)

# makes number of arrays
def random_matrix_maker(x):
    matrix = []
    for x in range(x):
        matrix.append(random.randint(0,1))
    return matrix

def voltron_function(x):
    return function_caller(x,x)
# repeat(function_caller(1))
# print(complete_array)
print(voltron_function(3))

# print(random_array_maker(4))