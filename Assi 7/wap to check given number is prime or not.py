#wap to check given number is prime or not

num=int(input("Enter a number "))
prime=True
for i in range(2,num):
    if(num%i==0):
        prime=False
        break
if prime:
    print("This is prime")
else:
    print("This is not prime")
