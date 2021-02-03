import numpy

a, b, c = input().split(' ')

matrix1 = []
for i in range(max(int(a), int(c))):
    matrix1.append(input().split(' '))

matrix2 = []
for i in range(max(int(b), int(c))):
    matrix2.append(input().split(' '))

array1 = numpy.array(matrix1, int)
array2 = numpy.array(matrix2, int)

print(numpy.concatenate(array1, array2))
