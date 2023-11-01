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
                 escreval("PAR")
             senao
                 se (n % 2 <> 0) e (n > 0) entao
                     escreval("IMPAR")
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
            
           escreva("Digite um numero: ")
           leia(n)
      fimpara

Fimalgoritmo