import os
import math
product = []
pricelist = []

#檢查有沒有檔案
if os.path.isfile('account.csv'):
	print('file exist')
		#讀取檔案
	with open('account.csv', 'r', encoding= 'utf-8') as a:
		for line in a:		
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			product.append([name, price])
		for p in product:			
			print('The price of ' + str(p[0]) + ' is ' + str(p[1]) + 'NTD')


else:
	print('file need to be generated')

	#要讓使用者反覆輸入
while True:
	name = input('Please enter product name: ')
	if name == 'q':
		break
	price = input('Please enter product price: ')
	product.append([name, price])
print(product)
print('---------------------------------------------')
	
for p in product:
	print('The price of ' + str(p[0]) + ' is ' + str(p[1]) + 'NTD')


#寫入檔案
with open('account.csv', 'w', encoding= 'utf-8') as a:
	a.write('商品,價格\n')
	for p in product:
		a.write(p[0] + ',' + p[1] + '\n')
	