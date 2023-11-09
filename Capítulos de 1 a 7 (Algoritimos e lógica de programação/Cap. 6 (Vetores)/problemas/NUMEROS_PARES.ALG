Algoritmo "numeros_pares"
// 

Var
   N, i, x, q_par : inteiro
   vet : vetor[0..15] de inteiro

Inicio
      escreva("Escreva quantos números serão digitados: ")
      leia(N)
      
      para i de 0 ate N-1 faca
           escreva("Digite um número: ")
           leia(vet[i])
      fimpara
      
      escreval
      escreva("Numeros pares: ")
      escreval
      
      q_par <- 0
      
      para i de 0 ate N-1 faca
           se vet[i] % 2 = 0 entao
              escreva(vet[i]:4)
              q_par <- q_par + 1
           fimse
      fimpara
      
      escreval
      escreva("Quantidade de pares: ",q_par)



Fimalgoritmo