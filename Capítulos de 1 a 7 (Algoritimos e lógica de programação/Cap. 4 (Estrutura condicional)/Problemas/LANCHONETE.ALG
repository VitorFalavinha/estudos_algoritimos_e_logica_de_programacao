Algoritmo "lanchonete"
// 


Var

cod , quant : inteiro
valor : real


Inicio
escreva("Código do produto: ")
leia(cod)
escreva("Quantidade comprada: ")
leia(quant)

escolha cod
 caso 1
 valor <- 5 * quant
 caso 2
 valor <- 3.50 * quant
 caso 3
 valor <- 4.80 * quant
 caso 4
 valor <- 8.90 * quant
 caso 5
 valor <- 7.32 * quant
 outrocaso
 valor <- CÓDIGO INVÁLIDO
 
 
 fimescolha
 
 escreval("Valor a pagar: R$ ", valor:4:2)




Fimalgoritmo