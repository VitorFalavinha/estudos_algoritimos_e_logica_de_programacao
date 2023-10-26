Algoritmo "Menor_de_tres"



Var
  v1, v2, v3 : real


Inicio
escreva("Primeiro valor: ")
leia(v1)
escreva("Segundo valor: ")
leia(v2)
escreva("Terceiro valor: ")
leia(v3)

    se (v1 < v2) e (v1 < v3) entao
       escreva("MENOR = ", v1)
senao
    se v2 < v3 entao
       escreva("MENOR = ", v2)
senao
       escreva("MENOR = ",v3)
    fimse
fimse



Fimalgoritmo