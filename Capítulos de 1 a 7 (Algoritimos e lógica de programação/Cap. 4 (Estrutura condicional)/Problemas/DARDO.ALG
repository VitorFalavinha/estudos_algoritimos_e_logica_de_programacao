Algoritmo "Dardo"
// 
//  

Var
d1, d2, d3 : real



Inicio

escreval("Digite as tr�s dist�ncias: ")
leia(d1)
leia(d2)
leia(d3)

se (d1 > d2) e (d1 > d3) entao
    escreva("MAIOR DIST�NCIA: ",d1)
senao
    se d2 > d3 ent�o
    escreva("MAIOR DIST�NCIA: ", d2)
senao
    escreva("MAIOR DIST�NCIA: ", d3)
    fimse
fimse



Fimalgoritmo