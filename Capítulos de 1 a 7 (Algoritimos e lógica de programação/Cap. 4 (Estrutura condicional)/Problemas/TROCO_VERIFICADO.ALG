Algoritmo "troco_verificado"



Var
preco_unit, valor_rec, falta, troco : real
quant : inteiro

Inicio

escreva("Pre�o unit�rio do produto: ")
leia(preco_unit)
escreva("Quantidade comprada: ")
leia(quant)
escreva("Valor recebido: ")
leia(valor_rec)

se valor_rec < preco_unit * quant ent�o
   falta <- preco_unit * quant - valor_rec
   escreva("DINHEIRO INSUFICIENTE. FALTAM R$ ", falta:4:2)
sen�o
   troco <- valor_rec - preco_unit * quant
   escreva("TROCO R$ ",troco:4:2)
fimse






Fimalgoritmo