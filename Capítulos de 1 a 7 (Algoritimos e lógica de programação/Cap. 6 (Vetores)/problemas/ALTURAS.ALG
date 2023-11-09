Algoritmo "alturas"
// 

Var
   N, i : inteiro
   vet_nome : vetor[1..9] de caractere
   vet_idade : vetor[1..9] de inteiro
   vet_altura : vetor[1..9] de real
   soma_altura, media_altura, idade_abaixo : real

   

   
Inicio
      escreva("Quantas pessoas serão digitadas? ")
      leia(N)

      soma_altura <- 0
      media_altura <- 0
      
      para i de 1 ate N faca
           escreval("Digite os dados da ",i,"a pessoa:")
           escreva("Nome: ")
           leia (vet_nome[i])
           escreva("Idade: ")
           leia(vet_idade[i])
           escreva("Altura: ")
           leia(vet_altura[i])
      fimpara
      
      para i de 1 ate N faca
            soma_altura <- soma_altura + vet_altura[i]
      fimpara
      
      media_altura <- soma_altura / N
      
      escreval
      escreval("Altura média: ",media_altura:4:2)
      
      idade_abaixo <- 0
      
      para i de 1 ate N faca

           se vet_idade[i] < 16 entao
              idade_abaixo <- idade_abaixo + 1
           fimse
      fimpara
      
      idade_abaixo <- idade_abaixo * 100 / N
      

      escreval("Pessoas com menos de 16 anos: ", idade_abaixo:4:1,"%")
      
      para i de 1 ate N faca
           se vet_idade[i] < 16 entao
              escreval(vet_nome[i])
           fimse
      fimpara



Fimalgoritmo