Algoritmo "comerciante"
// 

Var
    N, i , Hprofit, Mprofit, Lprofit : inteiro
    NAME : vetor[0..9] de caractere
    buyPrice : vetor[0..9] de real
    salePrice : vetor[0..9] de real
    totalBuy, totalSale, totalProfit : real

Inicio
      escreva("Serao digitados dados de quantos produtos? ")
      leia(N)
      
      para i de 0 ate N-1 faca
         escreval("Produto ",i+1,":")
           escreva("Nome: ")
           leia(NAME[i])
           escreva("Preco de compra: ")
           leia(buyPrice[i])
           escreva("Preco de venda: ")
           leia(salePrice[i])
      fimpara
      
      Lprofit <- 0
      Mprofit <- 0
      Hprofit <- 0
      
      para i de 0 ate N-1 faca
           se (salePrice[i] * 100 / buyPrice[i]) < 110 entao
              Lprofit <- Lprofit + 1
            senao
              se (salePrice[i] * 100 / buyPrice[i] >= 110) e (salePrice[i] * 100 / buyPrice[i] < 120)  entao
                  Mprofit <- Mprofit + 1
              senao
                   Hprofit <- Hprofit + 1
              fimse
            fimse
      fimpara
      
      totalBuy <- 0
      totalSale <- 0
      
      para i de 0 ate N-1 faca
           totalBuy <- totalBuy + buyPrice[i]
           totalSale <- totalSale + salePrice[i]
      fimpara
      
      totalProfit <- totalSale - totalBuy
      
      escreval
      escreval("RELATORIO: ")
      escreval
      escreval("Lucro abaixo de 10%: ", Lprofit)
      escreval("Lucro entre 10% e 20%: ", Mprofit)
      escreval("Lucro acima de 20%: ", Hprofit)
      escreval
      escreval("Valor total de compra: R$ ",totalBuy:4:2)
      escreval("Valor total de venda: R$ ",totalSale:4:2)
      escreval("Lucro total: R$ ",totalProfit:4:2)
      

Fimalgoritmo