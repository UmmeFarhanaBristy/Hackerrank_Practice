import calendar as cd

m, d, y = map(int, input().split())
print(cd.day_name[cd.weekday(y, m, d)].upper())
