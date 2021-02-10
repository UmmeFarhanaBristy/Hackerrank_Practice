lis = []
for _ in range(int(input())):
    name = input()
    score = float(input())

    lis.append([name, score])
s_highest = sorted(set([score for name, score in lis]))[1]
print('\n'.join(sorted([name for name, score in lis if score == s_highest])))