Algoritmo "tempo_de_jogo"

Var
h1, h2, total : inteiro

Inicio

escreva("Hora inicial: ")
leia (h1)
escreva("Hora final: ")
leia (h2)

se h1 > h2 ent�o
   total <- (24 - h1) + h2
      sen�o
         se h1 = h2 entao
         total <- (24 - h2) + h1
            sen�o
               total <- (h2 - h1)
    fimse
fimse


escreva("O jogo durou ", total, "hora(s)")


Fimalgoritmo