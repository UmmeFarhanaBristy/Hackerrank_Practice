import numpy


def array(lis):
    a = numpy.array(lis, int)
    return numpy.reshape(a, (3, 3))


lis = input().strip().split(' ')
result = array(lis)
print(result)
