with open("try.py") as f:
    print(f.closed)
    print('----------------------------------------------------')
    for line in f:
        print(line, end="")

print('----------------------------------------------------')
print(f.closed)
