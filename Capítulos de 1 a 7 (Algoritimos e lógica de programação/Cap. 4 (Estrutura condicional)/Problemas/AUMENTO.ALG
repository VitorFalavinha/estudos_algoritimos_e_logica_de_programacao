Algoritmo "Aumento"

Var
salario, novo_salario, aumento, porcentagem : real

Inicio
   escreva("Digite o sal�rio do funcion�rio: ")
   leia(salario)

      se salario <= 1000 ent�o
         porcentagem <- 20
      senao
         se salario <= 3000 ent�o
            porcentagem <- 15
         senao
            se salario <= 8000 ent�o
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
