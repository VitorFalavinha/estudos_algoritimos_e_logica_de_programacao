Algoritmo "teste_ate"
// 

Var
   c, f : real
   resp : caractere


Inicio
       repita

         escreva("Digite a temperatura em Celsius: ")
         leia(c)
         f <- 9 * c / 5 + 32
         escreval("Equivalente em Farenheit: ", f:3:1)
         escreva("Deseja repetir (s/n)?")
         leia(resp)
         
       ate resp <> "s"

Fimalgoritmo