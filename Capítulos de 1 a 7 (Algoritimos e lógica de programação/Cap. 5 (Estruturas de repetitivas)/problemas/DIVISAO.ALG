Algoritmo "divisao"
// 

Var
   num, den, divisao : real
   i, q : inteiro

Inicio
      escreva("Quantos casos voce vai digitar? ")
      leia(q)
      
      para i de 1 ate q faca
           escreva("Entre com o numerador: ")
           leia(num)
           escreva("Entre com o denominador: ")
           leia(den)
           
           se den = 0 entao
              escreval("DIVIS�O IMPOSS�VEL")
              
              senao
                  divisao <- num / den
                  escreval("DIVIS�O: ", divisao:4:2)
           fimse
      fimpara


Fimalgoritmo