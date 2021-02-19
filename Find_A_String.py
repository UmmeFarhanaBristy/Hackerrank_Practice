def count_substring(s, sub_s):
    c = 0
    for i in range(len(s) - len(sub_s) + 1):
        if s[i:i + len(sub_s)] == sub_s:
            c = c + 1

    return c


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
