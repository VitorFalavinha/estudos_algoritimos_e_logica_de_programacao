Algoritmo "par_impar"
// 

Var
    i, n, q : inteiro

Inicio
      escreva("Quantos numeros voce vai digitar? ")
      leia(q)
      
      para i de 1 ate q faça
           escreva("Digite um numero: ")
           leia(n)
           
             se (n % 2 = 0) e (n > 0) entao
                 escreval("PAR POSITIVO")
             senao
                 se (n % 2 <> 0) e (n > 0) entao
                     escreval("IMPAR POSITIVO")
                 senao
                     se (n % 2 = 0) e (n < 0) entao
                         escreval("PAR NEGATIVO")
                         senao
                            se (n % 2 <> 0) e (n < 0) entao
                                escreval("IMPAR NEGATIVO")
                                 senao
                                    escreval("NULO")
                            fimse
                     fimse
                 fimse
            fimse
      fimpara

Fimalgoritmo