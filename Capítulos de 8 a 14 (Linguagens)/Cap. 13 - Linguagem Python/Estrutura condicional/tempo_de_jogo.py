start: int; finish: int; duration: int

start = int(input('Hora inicial: '))
finish = int(input('Hora final: '))

if start < finish:
    duration = finish - start
else:
    duration = (24 - start) + finish

print(f'O jogo durou {duration} hora(s)')