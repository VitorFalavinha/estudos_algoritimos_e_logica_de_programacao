n = 200

for i in range(100,n):
    if i % 2 != 0:
        print(i, end='')
        print(' e ' if i < 199 else ' ', end='')
