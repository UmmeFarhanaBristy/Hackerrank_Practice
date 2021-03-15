def average(array):
    e = set(array)
    return sum(e) / len(e)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
