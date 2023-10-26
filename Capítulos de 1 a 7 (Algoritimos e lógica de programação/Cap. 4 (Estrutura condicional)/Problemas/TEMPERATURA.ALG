Algoritmo "temperatura"
// 

Var
escala : caractere
temperatura, conversaoC, conversaoF : real



Inicio
escreval("Voce vai digitar a temperatura em qual escala C° ou F°?")
escreva("Digite (C) para graus Celcius ou (F) para graus Fahrenheit: ")
leia(escala)

enquanto (escala <> "f") e (escala <> "c") faca
    escreval("OPÇÃO INVÁLIDA.")
    escreva("Digite (C) para graus Celsius ou (F) para graus Fahrenheit: ")
    leia(escala)
fimenquanto

   se escala = "f" entao
        escreva("Digite a temperatura em Fahrenheit: ")
        leia(temperatura)
        
        conversaoC <-  5/9 * (temperatura - 32)
        escreval("Temperatura equivalente em Celsius: ", conversaoC:4:2)


   senao
      se escala = "c" entao
         escreva("Digite a temperatura em Celsius: ")
         leia(temperatura)
         
         conversaoF <- 1.8 * temperatura + 32
         escreva("Temperatura equivalente em Fahrenheit: ", conversaoF:4:2)
         

      fimse
   fimse



Fimalgoritmo