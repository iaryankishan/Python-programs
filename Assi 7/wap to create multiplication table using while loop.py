#wap to create multiplication table using while loop

num= int(input("Enter the number "))
i=1
while(i<=10):
    print(str(num) + " X " + str(i) + " = " + str(i*num))
    #print(f"{num} X {i} = {num*i}")
    i=i+1
