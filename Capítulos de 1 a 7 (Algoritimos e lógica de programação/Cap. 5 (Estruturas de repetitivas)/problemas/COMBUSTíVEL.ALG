Algoritmo "combustível"
// 

Var
cod, a, g, d : inteiro

Inicio
      escreva("Informe um codigo (1, 2, 3) ou 4 para parar: ")
      leia(cod)
      
      a <- 0
      g <- 0
      d <- 0
      
      enquanto cod <> 4 faca
              escreva("Informe um codigo (1, 2, 3) ou 4 para parar: ")
              leia(cod)
              
              se cod = 1 entao
                 a <- a + 1
                 
                 senao
                    se cod = 2 entao
                    g <- g + 1
                    
                    senao
                       se cod = 3 entao
                       d <- d + 1
                       
                       fimse
                 fimse
              fimse
      fimenquanto
      
      escreval("MUITO OBRIGADO")
      escreval("Alcool: ", a)
      escreval("Gasolina: ", g)
      escreva("Diesel: ", d)



Fimalgoritmo