Algoritmo "diagonal_negativos"


Var
    N , i, j, q_neg : inteiro
    mat : vetor[0..9, 0..9] de inteiro


Inicio
       escreva("Qual a ordem da matriz? ")
       leia(N)
       
       para i de 0 ate N-1 faca
            para j de 0 ate N-1 faca
                 escreva("Elemento [",i,",",j,"]: ")
                 leia(mat[i,j])
            fimpara
       fimpara

       escreval
       escreval("DIAGONAL PRINCIPAL: ")
       
       para i de 0 ate N-1 faca
            escreva(mat[i,i])
       fimpara
       escreval
       
       q_neg <- 0
       
       para i de 0 ate N-1 faca
            para j de 0 ate N-1 faca
                 se mat[i,j] < 0 entao
                    q_neg <- q_neg + 1
                 fimse
            fimpara
       fimpara
       
       escreva("QUANTIDADE DE NEGATIVOS = ", q_neg)
            
Fimalgoritmo