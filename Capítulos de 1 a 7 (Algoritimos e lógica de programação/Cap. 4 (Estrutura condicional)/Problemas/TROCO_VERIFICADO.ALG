Algoritmo "troco_verificado"



Var
preco_unit, valor_rec, falta, troco : real
quant : inteiro

Inicio

escreva("Preço unitário do produto: ")
leia(preco_unit)
escreva("Quantidade comprada: ")
leia(quant)
escreva("Valor recebido: ")
leia(valor_rec)

se valor_rec < preco_unit * quant então
   falta <- preco_unit * quant - valor_rec
   escreva("DINHEIRO INSUFICIENTE. FALTAM R$ ", falta:4:2)
senão
   troco <- valor_rec - preco_unit * quant
   escreva("TROCO R$ ",troco:4:2)
fimse






Fimalgoritmo