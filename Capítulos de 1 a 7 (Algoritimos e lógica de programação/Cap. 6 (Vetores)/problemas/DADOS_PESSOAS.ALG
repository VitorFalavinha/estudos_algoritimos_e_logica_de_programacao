Algoritmo "dados_pessoas"

Var
   N, i,n_mulheres, n_homens : inteiro
   ALTURA : vetor[0..9] de real
   GENERO : vetor[0..9] de caractere
   maior_alt, menor_alt, somaAlt_mulheres, mediaAlt_mulheres: real
   
Inicio
      escreva("Quantas pessoas serão digitadas? ")
      leia(N)
      
      para i de 0 ate N-1 faca
           escreva("Altura da ",i+1,"ª pessoa: ")
           leia(ALTURA[i])
           escreva("Genero da ",i+1,"ª pessoa: ")
           leia(GENERO[i])
      fimpara
      
      maior_alt <- ALTURA[0]
      
      para i de 1 ate N-1 faca
           se ALTURA[i] > maior_alt entao
              maior_alt <- ALTURA[i]
           fimse
      fimpara
      
      menor_alt <- ALTURA[0]
      
      para i de 1 ate N-1 faca
           se ALTURA[i] < menor_alt entao
              menor_alt <- ALTURA[i]
           fimse
      fimpara
      n_homens <- 0
      para i de 0 ate N-1 faca
           se (GENERO[i] = "F") OU (GENERO[i] = "f") entao
               n_mulheres <- n_mulheres + 1
           fimse
      fimpara
      
        escreval("MENOR ALTURA = ", menor_alt:4:2)
        escreval("MAIOR ALTURA = ", maior_alt:4:2)
      
      somaAlt_mulheres <- 0

      
      para i de 0 ate N-1 faca
           se (GENERO[i] = "f") ou (GENERO[i] = "F") entao
               somaAlt_mulheres <- somaAlt_mulheres + ALTURA[i]
           fimse
      fimpara
      
      se n_mulheres = 0 entao
         escreval("Não mulheres para se calcular a média!")
      senao
         mediaAlt_mulheres <- somaAlt_mulheres / n_mulheres
         escreval("MEDIA DAS ALTURAS DAS MULHERES = ",mediaAlt_mulheres:4:2)
      fimse
      
      n_homens <- N - n_mulheres

      escrevaL("NUMERO DE HOMENS = ", n_homens)
      
Fimalgoritmo