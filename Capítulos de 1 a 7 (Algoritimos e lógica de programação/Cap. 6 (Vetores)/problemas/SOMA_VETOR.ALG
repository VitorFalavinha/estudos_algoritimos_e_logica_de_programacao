Algoritmo "soma_vetor"
// 

Var
   N, i : inteiro
   x, soma, media : real
   A : vetor [0..9] de real


Inicio
      escreva("Quantos numeros voce vai digitar? ")
      leia(N)
      
      para i de 0 ate N-1 faca
           escreva("Digite um numero: ")
           leia(x)
           A[i] <- x
      fimpara
      
      soma <- 0

      escreva("VALORES =")
      para i de 0 ate N-1 faca
           escreva(A[i]:6:1)
           soma <- soma + A[i]
      fimpara
      
      media <- soma / N
      escreval
      escreval("SOMA = ", soma:4:2)
      escreva("MEDIA = ", media:4:2)


Fimalgoritmo