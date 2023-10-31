Algoritmo "media_idades"
// 

Var
idade, soma, i : inteiro
media : real

Inicio
      escreval("Digite as idades: ")
      leia(idade)
      
      soma <- 0
      i <- 0
      
      enquanto idade >= 0 faca
               soma <- soma + idade
               i <- i + 1
               leia(idade)
      fimenquanto
            
      se i = 0 entao
              escreva("IMPOSSÍVEL CALCULAR!")
      senao
              media <- soma / i
              escreva("MEDIA = ", media:4:2)
      fimse
       

Fimalgoritmo