Algoritmo "dentro fora"
// 

Var
   i, n, q, dentro, fora : inteiro


Inicio
      escreva("Quantos numeros voce vai digitar? ")
      leia(q)
      
      dentro <- 0
      fora <- 0
      
      para i de 1 ate q faca
            escreva("Digite um numero:")
            leia(n)
            
            se (n < 10) ou (n > 20) entao
                fora <- fora + 1)
                
                senao
                     dentro <- dentro + 1
            fimse
      fimpara
      escreval(dentro, " DENTRO")
      escreva(fora, " FORA")



Fimalgoritmo