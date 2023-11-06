Algoritmo "experiencias"
// 

Var
   i, casos, quant_cob, total_cob, total_coe, total_rat, total_sap : inteiro
   
   perc_coe, perc_rat, perc_sap : real
   
   tipo_cob : caractere

Inicio
      escreva("Quantos casos serão digitados? ")
      leia(casos)
      
      total_cob <- 0
      total_coe <- 0
      total_rat <- 0
      total_sap <- 0
      
      para i de 1 ate casos faca
           escreva("Quantidade de cobaias: ")
           leia(quant_cob)
           escreva("Tipo de cobaia: ")
           leia(tipo_cob)
           
           total_cob <- quant_cob + total_cob
           
           se (tipo_cob = "C") ou (tipo_cob = "c") entao
              total_coe <- total_coe + quant_cob
              
              senao
                   se (tipo_cob = "R") ou (tipo_cob = "r") entao
                      total_rat <- total_rat + quant_cob
                      
                   senao
                        se (tipo_cob = "S") ou (tipo_cob = "s") entao
                           total_sap <- total_sap + quant_cob
                        fimse
                   fimse
           fimse
      fimpara
      
      perc_coe <- (total_coe * 100) / total_cob
      perc_rat <- (total_rat * 100) / total_cob
      perc_sap <- (total_sap * 100) / total_cob
      
      escreval
      escreval("RELATÓRIO FINAL")
      escreval("Total: ", total_cob, " cobaias")
      escreval("Total de coelhos: ", total_coe)
      escreval("Total de ratos: ", total_rat)
      escreval("Total de sapos: ", total_sap)
      escreval("Percentual de coelhos: ", perc_coe:4:2)
      escreval("Percentual de ratos: ", perc_rat:4:2)
      escreval("Percentual de sapos: ", perc_sap:4:2)

Fimalgoritmo