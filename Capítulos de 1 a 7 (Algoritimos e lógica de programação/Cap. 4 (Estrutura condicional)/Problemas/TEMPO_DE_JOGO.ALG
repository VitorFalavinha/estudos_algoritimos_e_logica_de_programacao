Algoritmo "tempo_de_jogo"

Var
h1, h2, total : inteiro

Inicio

escreva("Hora inicial: ")
leia (h1)
escreva("Hora final: ")
leia (h2)

se h1 > h2 então
   total <- (24 - h1) + h2
      senão
         se h1 = h2 entao
         total <- (24 - h2) + h1
            senão
               total <- (h2 - h1)
    fimse
fimse


escreva("O jogo durou ", total, "hora(s)")


Fimalgoritmo