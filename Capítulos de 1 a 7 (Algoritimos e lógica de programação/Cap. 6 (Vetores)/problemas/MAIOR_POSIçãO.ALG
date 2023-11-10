Algoritmo "maior_posição"
// 

Var
   N, i, posicao : inteiro
   maior : real
   vet : vetor[0..15] de real



Inicio
      escreva("Quantos numeros voce vai digitar? ")
      leia(N)
      
      para i de 0 ate N-1 faca
           escreva("Digite um numero: ")
           leia(vet[i])
      fimpara
      
      maior <- vet[0]
      posicao <- 0
            
      para i de 1 ate N-1 faca
           se vet[i] > maior entao
              maior <- vet[i]
              posicao <- i

           fimse
           

      fimpara
      
      escreval("MAIOR VALOR: ",maior:4:2)
      escreval("POSIÇÃO: ",posicao)
           
      
Fimalgoritmo