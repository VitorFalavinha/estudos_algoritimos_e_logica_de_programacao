Algoritmo "pares_consecutivos"


Var
n, soma : inteiro

Inicio
      escreva("Digite um número: ")
      leia(n)
      
      enquanto n <> 0 faca
               se n % 2 = 0 entao
               soma <- n + (n + 2) + (n + 4) + (n + 6) + (n + 8)
               
               senao
               soma <- (n + 1) + (n + 3) + (n + 5) + (n + 7) + (n + 9)
               
               fimse
               escreval("SOMA = ", soma)
               escreva("Digite um numero inteiro: ")
               leia(n)
      fimenquanto

Fimalgoritmo