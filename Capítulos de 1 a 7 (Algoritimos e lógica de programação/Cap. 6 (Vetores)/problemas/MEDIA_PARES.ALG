Algoritmo "media_pares"
// 
Var
   N, i , soma, divisor : inteiro
   A : vetor[0..10] de inteiro
   B : vetor[0..10] de inteiro
   media : real
   
Inicio
      escreva("Quantos elementos vai ter o vetor?")
      leia(N)
      
      para i de 0 ate N-1 faca
           escreva("Digite um numero: ")
           leia (A[i])
      fimpara
      
      soma <- 0
      divisor <- 0
      
      para i de 0 ate N-1 faca
           se A[i] % 2 = 0 entao
              soma <- soma + A[i]
              divisor <- divisor + 1
           fimse
      fimpara
      
      se divisor = 0 entao
         escreva("NENHUM NUMERO PAR")
         senao
            media <- soma / divisor
            escreva("MEDIA DOS PARES: ", media:4:1)
      fimse
Fimalgoritmo