Algoritmo "fatorial"
//  

Var
   n, fat, i : inteiro

Inicio
      escreva("Digite o valor de N: ")
      leia(n)

      fat <- 0
      
      para i de 0 ate n faca

        fat <- i
        fat(i + 1)
               
      fimpara
          escreva("FATORIAL = ", fat)

Fimalgoritmo