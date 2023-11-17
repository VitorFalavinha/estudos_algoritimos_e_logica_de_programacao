secondsEnt = int(input("Digite a duração em segundos: "))


hours = secondsEnt // 3600

minutes = secondsEnt % 3600 // 60

seconds = secondsEnt % 60


print(f"{hours} : {minutes} : {seconds}")