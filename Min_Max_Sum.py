if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    x = sum(arr)
    print(x - max(arr), x - min(arr))
