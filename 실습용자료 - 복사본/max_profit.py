def maxProfit_bruteforce (prices):
   max_price = 0

   for i, price in enumerate(prices):
       for j in range(i, len(prices)):
           max_price = max(prices[j] - price, max_price)
	print("어 형이야")
   return

