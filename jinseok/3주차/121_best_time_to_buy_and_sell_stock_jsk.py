import sys
stock = [7,1,5,3,6,4]


profit = 0
min_price = sys.maxsize

for price in stock:
  if price < min_price:
    min_price = price
  profit = max(profit, price-min_price)
print(profit) 
