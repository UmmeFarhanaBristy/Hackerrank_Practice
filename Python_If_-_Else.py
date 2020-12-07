x = int(input())

if x % 2 == 0:
    if (x >= 2 and x <= 5) or x > 20:
        print("Not Weird")
        
    elif x >= 6 and x <= 20:
        print("Weird")
        
else:
    print("Weird")
