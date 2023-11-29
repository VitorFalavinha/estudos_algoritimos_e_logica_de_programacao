N = int(input('Quantos produtos serao digitados? '))

product:[str] = [0 for x in range(N)]
buyPrice:[float] = [0 for x in range(N)]
sellPrice:[float] = [0 for x in range(N)]

for i in range(N):
    print('Produto ',i+1,':')
    product[i] = str(input('Produto: '))
    buyPrice[i] = float(input('Preco de compra: '))
    sellPrice[i] = float(input('Preco de venda: '))

low = 0
mid = 0
high = 0

for i in range(N):
    if (sellPrice[i] * 100) / buyPrice[i] < 110:
        low = low + 1
    elif  (sellPrice[i] * 100) / buyPrice[i] < 120:
        mid = mid + 1
    else:
        high = high + 1

totalBuy = 0
totalSell = 0
for i in range(N):
    totalBuy = totalBuy + buyPrice[i]
    totalSell = totalSell + sellPrice[i]

profit = totalSell - totalBuy

print()
print('RELATORIO: ')
print('Lucro abaixo de 10%: ', low)
print('Lucro entre 10% e 20%: ', mid)
print('Lucro acima de 20%: ', high)
print(f'Valor total de compra: {totalBuy:.2f}')
print(f'Valor total de venda: {totalSell:.2f}')
print(f'Lucro total: {profit:.2f}')
      