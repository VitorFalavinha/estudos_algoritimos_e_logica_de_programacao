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
              escreval("DIVISÃO IMPOSSÍVEL")
              
              senao
                  divisao <- num / den
                  escreval("DIVISÃO: ", divisao:4:2)
           fimse
      fimpara


Fimalgoritmo