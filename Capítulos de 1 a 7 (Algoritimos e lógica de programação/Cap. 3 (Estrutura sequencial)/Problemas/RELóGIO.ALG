Algoritmo "Relógio"




Var
seg_dig, dias, horas, minutos, segundos : inteiro



Inicio

escreva("Digite uma quantidade de segundos: ")
leia (seg_dig)

dias <- seg_dig \ 86400

horas <- seg_dig % 86400 \ 3600

minutos <- seg_dig % 3600 \ 60

segundos <- seg_dig % 60

escreva(dias:6, " :  ")
escreva(horas:6, " :  ")
escreva(minutos:6, " :  ")
escreval(segundos:6)

escreva("   Dias ")
escreva("   Horas ")
escreva("   Minutos ")
escreva("  Segundos ")



Fimalgoritmo