Algoritmo "aprovados"
// 

Var
    N, i : inteiro
    NOME : vetor[0..9] de caractere
    N1 : vetor[0..9] de real
    N2 : vetor[0..9] de real
    media : real

Inicio
      escreva("Quantos alunos ser�o digitados: ")
      leia(N)
      
      para i de 0 ate N-1 faca
           escreval("Digite nome, primeira e segunda nota do ",i+1,"� aluno:")
           leia(NOME[i])
           leia(N1[i])
           leia(N2[i])
      fimpara
      
      escreval("Alunos aprovados: ")
      para i de 0 ate N-1 faca
           media <- (N1[i] + N2[i]) / 2
              se media >= 6 entao
                 escreval(NOME[i])
              fimse
      fimpara


Fimalgoritmo