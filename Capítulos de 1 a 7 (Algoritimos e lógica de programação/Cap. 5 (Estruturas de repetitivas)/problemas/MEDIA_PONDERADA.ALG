Algoritmo "media_ponderada"
// 

Var
   i, q : inteiro
   n1, n2, n3, media : real

Inicio
       escreva("Quantos casos você vai digitar? ")
       leia (q)
       
       media <- 0
       
       para i de 1 ate q faca
            escreval("Digite os 3 numeros: ")
            leia(n1)
            leia(n2)
            leia(n3)
            
            media <- ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10

            escreval("MEDIA = ", media:4:1)
        fimpara

Fimalgoritmo