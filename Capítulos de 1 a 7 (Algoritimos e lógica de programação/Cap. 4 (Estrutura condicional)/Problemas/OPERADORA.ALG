Algoritmo "Operadora"
// 


Var

minutos, valorPagar : REAL

// minutos, amais, extra, valor_final : real

Inicio
escreva("Digite a quantidade de minutos: ")
leia(minutos)

valorPagar <- 50

   se minutos > 100 entao
   
      valorPagar <- valorPagar + 2 * (minutos - 100)
      
      escreva("O valor a pagar é: R$ ", valorPagar:4:2)
   senao
      escreva("O valor a pagar é: ", valorPagar:4:2)
   fimse
   
fimalgoritmo




// MINHA VERSÃO CONDICIONAL

// se minutos <= 100 então
//    escreva("Valor a pagar: R$ 50,00.")
// senao
//    amais <- minutos - 100
//    extra <- amais * 2
//   valor_final <- 50 + extra
   
// escreva("Valor a pagar: R$ ", valor_final:4:2)

// fimse




