prime=int(input("Enter a number\n"))
count=0

for i in range(1,prime+1):
  if prime%i==0:
    count+=1
if(count==2):
  print(f"given {prime} is Prime number")
else:
  print(f"given {prime} is not a prime number")