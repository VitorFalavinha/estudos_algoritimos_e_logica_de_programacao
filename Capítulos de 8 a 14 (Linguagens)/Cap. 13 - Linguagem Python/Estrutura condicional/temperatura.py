scale = str(input("Qual a escala da temperatura, Celsius ou Fahrenheit? "))

while scale != "f" and scale != "F" and scale !="c" and scale != "C":
    print("CÓDIGO INVÁLIDO!!! Digite uma escala válida (F/f ou C/c)")
    scale = str(input("Qual a escala da temperatura, Celsius ou Fahrenheit? "))

if scale == "f" or scale == "F":
    temp = float(input("Digite a temperatura em Fahrenheit: "))

    conversion = 5/9 * (temp - 32)

    print(f'Temperatura equivalente em Celsius: {conversion:.2f} C°')

elif scale == "c" or scale == "C": 
    temp = float(input("Digite a temperatura em Celsius: "))
    conversion = 1.8 * temp + 32
    
    print(f'Temperatura equivalente em Fahrenheit: {conversion:.2f} F°')
