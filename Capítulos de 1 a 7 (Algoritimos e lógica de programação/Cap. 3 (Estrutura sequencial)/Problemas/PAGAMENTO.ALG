Algoritmo "Pagamento"




Var
nome : caractere
val_hora, horas, salario : real



Inicio
escreva("Nome do funcionário: ")
leia(nome)
escreva("Valor por hora: ")
leia(val_hora)
escreva("Quantidade de horas trabalhadas: ")
leia(horas)

salario <- val_hora * horas

escreva("Salário do funcionário ",nome,":  ",salario:8:2," reais.")



Fimalgoritmo