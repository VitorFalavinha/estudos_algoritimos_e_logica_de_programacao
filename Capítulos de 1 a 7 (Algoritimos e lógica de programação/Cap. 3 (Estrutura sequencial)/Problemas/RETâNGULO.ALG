Algoritmo "Ret�ngulo"



Var

base, altura, area, perimetro, diagonal : real


Inicio

escreva ("Digite a base do ret�ngulo:  ")
leia (base)
escreva ("Digite a altura do ret�ngulo: ")
leia (altura)

area <- base * altura
perimetro <- (base + altura) *2
diagonal <- RaizQ(Exp(base,2) + Exp(altura,2))

escreval("�rea: ",area:8:4)
escreval("Per�metro: ", perimetro:8:4)
escreval("Diagonal: ",diagonal:8:4)


Fimalgoritmo