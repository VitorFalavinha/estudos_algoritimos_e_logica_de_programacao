Algoritmo "Aumento"

Var
salario, novo_salario, aumento, porcentagem : real

Inicio
   escreva("Digite o salário do funcionário: ")
   leia(salario)

      se salario <= 1000 então
         porcentagem <- 20
      senao
         se salario <= 3000 então
            porcentagem <- 15
         senao
            se salario <= 8000 então
               porcentagem <-10
            senao
               porcentagem <- 5
          fimse
      fimse
   fimse
   
   aumento <- salario * porcentagem / 100
   novo_salario <- salario + aumento
   
   escreval("Faixa de porcentagem = ", porcentagem, " % ")
   escreval("Aumento: R$ ",aumento:4:2)
   escreval("Novo salario: R$ ", novo_salario:4:2)

Fimalgoritmo
