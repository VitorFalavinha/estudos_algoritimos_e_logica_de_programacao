n: int; res:int

n = int(input('Deseja a tabuada de qual numero?'))

for i in range(1, 11):
    res = n * i
    print(f'{n} X {i} = {res}')