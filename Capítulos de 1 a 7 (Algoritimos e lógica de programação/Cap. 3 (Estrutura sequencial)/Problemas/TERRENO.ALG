Algoritmo "Terreno"



Var

c, l, valor, area, resultado : real


Inicio


escreva ("Digite o comprimento do terreno: ")
leia(c)
escreva ("Digite a largura do terreno: ")
leia(l)
escreva("Digite o valor do metro quadrado: ")
leia(valor)

area <- c * l
resultado <- area * valor

escreval("�rea do terreno = ", area:8:2, " metros quadrados.")
escreval("Pre�o do terreno = ",resultado:8:2, " reais.")


Fimalgoritmo