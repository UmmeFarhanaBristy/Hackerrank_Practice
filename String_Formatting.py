def print_formatted(n):
    w = len(str(bin(n)).replace('0b',''))

    for i in range(1, n+1):
        b = bin(int(i)).replace('0b','').rjust(w, ' ')
        o = oct(int(i)).replace('0o','').rjust(w, ' ')
        h = hex(int(i)).replace('0x','').upper().rjust(w, ' ')
        j = str(i).rjust(w, ' ')
        print (j, o, h, b)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)