Algoritmo "mais_velho"

Var
   N, i , maior, posMaior: inteiro
   NOME : vetor[0..10] de caractere
   IDADE : vetor[0..10] de inteiro

Inicio
      escreva("Quantas pessoas voce vai digitar? ")
      leia(N)
      
      para i de 0 ate N-1 faca
           escreval("Dados da ",i + 1,"ª pessoa")
           escreva("Nome: ")
           leia (NOME[i])
           escreva("Idade: ")
           leia(IDADE[i])
      fimpara
      
      maior <- IDADE[0]
      posMaior <- 0
      
      para i de 1 ate N-1 faca
           se IDADE[i] > maior entao
              maior <- IDADE[i]
              posMaior <- i
           fimse
      fimpara
      
      escreva("PESSOA MAIS VELHA: ",NOME[posMaior])

           
Fimalgoritmo