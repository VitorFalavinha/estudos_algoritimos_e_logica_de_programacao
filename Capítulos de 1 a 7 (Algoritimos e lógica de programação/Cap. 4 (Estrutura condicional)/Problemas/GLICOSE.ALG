Algoritmo "glicose"
// 

Var
taxa : real


Inicio
escreva("Digite a medida da glicose: ")
leia(taxa)

se taxa <= 100 entao
   escreva("CLASSIFICAÇÃO: normal")
senao
   se taxa <= 140 entao
   escreva("CLASSIFICAÇÃO: elevado")
senao
    escreva("CLASSIFICAÇÃO: diabetes")
fimse
fimse



Fimalgoritmo