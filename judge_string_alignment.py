price = map(int, input().split(';'))
price_list = list(price)
price_list.sort(reverse=True)

for i in range(len(price_list)):
    print('{0:>9,}'.format(price_list[i]))
