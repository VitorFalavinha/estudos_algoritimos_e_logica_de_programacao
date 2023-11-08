Algoritmo "negativos"
// 

Var
   N, i, x : inteiro
   A : vetor[0..9] de inteiro


Inicio
      escreva("Quantos numeros voce vai digitar? ")
      leia(N)
      
      para i de 0 ate N-1 faca
           escreva("Digite um numero: ")
           leia (x)
           A[i] <- x
      fimpara
      
      para i de 0 ate N-1 faca
           se A[i] < 0 entao
              escreval(A[i])
           fimse
      fimpara


Fimalgoritmo