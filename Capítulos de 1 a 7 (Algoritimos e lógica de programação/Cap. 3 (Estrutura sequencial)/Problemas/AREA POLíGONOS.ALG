Algoritmo "Area polígonos"




Var

a, b, c, area_qua, area_tri, area_trap : real



Inicio
escreva("Digite o valor A: ")
leia(a)
escreva("Digite o valor B: ")
leia(b)
escreva("Digite o valor C: ")
leia(c)

area_qua <- Exp(a,2)
area_tri <- (a * b) / 2
area_trap <- ((a + b) * c) / 2

escreval("Área do QUADRADO = ", area_qua:8:4)
escreval("Área do TRIÂNGULO = ", area_tri:8:4)
escreval("Área do TRAPÉZIO = ", area_trap:8:4)



Fimalgoritmo