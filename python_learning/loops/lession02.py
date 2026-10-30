fruites =["apple","banana","mango"]

for idx, fruit in enumerate(fruites, start=1):
  print(idx,fruit)



prices =[10,20,30]

for fruit , price in zip(fruites,prices):
  print(fruit,price)
