Algoritmo "Retângulo"



Var

base, altura, area, perimetro, diagonal : real


Inicio

escreva ("Digite a base do retângulo:  ")
leia (base)
escreva ("Digite a altura do retângulo: ")
leia (altura)

area <- base * altura
perimetro <- (base + altura) *2
diagonal <- RaizQ(Exp(base,2) + Exp(altura,2))

escreval("Área: ",area:8:4)
escreval("Perímetro: ", perimetro:8:4)
escreval("Diagonal: ",diagonal:8:4)


Fimalgoritmo