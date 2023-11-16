Algoritmo "soma_matrizes"
// 

Var
    M, N, i, j : inteiro
    A : vetor[0..9, 0..9] de inteiro
    B : vetor[0..9, 0..9] de inteiro
    C : vetor[0..9, 0..9] de inteiro

Inicio
      escreva("Linhas de cada matriz: ")
      leia(M)
      escreva("Colunas de cada matriz: ")
      leia(N)
      

           escreval("Digite os valores da matriz A: ")
           
           para i de 0 ate M-1 faca
                para j de 0 ate N-1 faca
                     escreva("Elemento [",i,",",j,"]: ")
                     leia(A[i,j])
                fimpara
           fimpara
           
           escreval("Digite os valores da matriz B: ")

           para i de 0 ate M-1 faca
                para j de 0 ate N-1 faca
                     escreva("Elemento [",i,",",j,"]: ")
                     leia(B[i,j])
                fimpara
           fimpara
           
           escreval
           escreval("MATRIZ SOMA: ")
           
           para i de 0 ate M-1 faca
                para j de 0 ate N-1 faca
                     C[i,j] <- A[i,j] + B[i,j]
                     escreva(C[i,j])
                fimpara
                escreval
           fimpara
           
Fimalgoritmo