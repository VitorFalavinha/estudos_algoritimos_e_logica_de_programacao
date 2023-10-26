Algoritmo "Troco"




Var

valunit, pag, troco : real
quant : inteiro



Inicio

escreva("Preço unitário do produto: ")
leia(valunit)
escreva("Quantidade comprada: ")
leia(quant)
escreva("Valor recebido: ")
leia(pag)

troco <-  pag - valunit * quant

escreva("TROCO = ", troco:8:2)




Fimalgoritmo