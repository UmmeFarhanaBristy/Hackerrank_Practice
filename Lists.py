lis = []
for _ in range(int(input())):
    command = input().split()
    cmd = command[0]
    if len(command) > 1:
        i = command[1]
    if len(command) > 2:
        e = command[2]

    if cmd == 'insert':
        lis.insert(int(i), int(e))

    elif cmd == 'print':
        print(lis)

    elif cmd == 'remove':
        lis.remove(int(i))

    elif cmd == 'append':
        lis.append(int(i))

    elif cmd == 'sort':
        lis.sort()

    elif cmd == 'pop':
        lis.pop()

    elif cmd == 'reverse':
        lis.reverse()
