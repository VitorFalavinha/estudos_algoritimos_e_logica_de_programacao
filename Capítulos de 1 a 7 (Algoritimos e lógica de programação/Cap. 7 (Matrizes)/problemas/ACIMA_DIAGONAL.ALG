Algoritmo "acima_diagonal"
// 

Var
   N, i, j , soma : inteiro
   mat : vetor[0..9,0..9] de inteiro

Inicio
      escreva("Qual a ordem da matriz? ")
      leia(N)
      
      para i de 0 ate N-1 faca
           para j de 0 ate N-1 faca
                escreva("Elemento [",i,",",j,"]: ")
                leia(mat[i,j])
           fimpara
      fimpara
      
      para i de 0 ate N-1 faca
           para j de i+1 ate N-1 faca
                soma <- soma + mat[i, j]
           fimpara
      fimpara
      
      escreva("SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL = ",  soma)
           


Fimalgoritmo