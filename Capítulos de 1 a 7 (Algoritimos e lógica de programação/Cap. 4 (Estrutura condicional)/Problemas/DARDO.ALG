Algoritmo "Dardo"
// 
//  

Var
d1, d2, d3 : real



Inicio

escreval("Digite as três distâncias: ")
leia(d1)
leia(d2)
leia(d3)

se (d1 > d2) e (d1 > d3) entao
    escreva("MAIOR DISTÂNCIA: ",d1)
senao
    se d2 > d3 então
    escreva("MAIOR DISTÂNCIA: ", d2)
senao
    escreva("MAIOR DISTÂNCIA: ", d3)
    fimse
fimse



Fimalgoritmo