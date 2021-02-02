import numpy

a, b = input().split(' ')

matrix = []
for i in range(max(int(a), int(b))):
    matrix.append(input().split(' '))

array = numpy.array(matrix, int)

print(numpy.transpose(array))
print(array.flatten())
