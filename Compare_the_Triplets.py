def compare(x, y):
    m = 0
    n = 0
    for i in range(3):
        if x[i] > y[i]:
            m = m + 1 
        
        elif x[i] < y[i]:
            n = n + 1
        
    print(m, n)

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()] 



compare(a, b)
