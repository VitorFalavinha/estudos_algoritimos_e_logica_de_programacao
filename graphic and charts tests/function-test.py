import numpy as np
import matplotlib.pyplot as plt

# Definindo a função
def f(x):
    return  -2*x + 10

# Gerando valores de x
x_values = np.linspace(-10, 10, 400)

# Gerando valores de y usando a função
y_values = f(x_values)

# Plotando o gráfico
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='f(x) = -2x + 10', color='blue')
plt.title('Gráfico da função f(x) = -2x + 10')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.legend()
plt.show()
