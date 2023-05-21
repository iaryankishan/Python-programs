#wap to create a multiplication table of given number

num= int(input("Enter the number "))
for i in range(1,11):
    #print(str(num) + " X " + str(i) + " = " + str(i*num))
    print(f"{num} X {i} = {num*i}")
    i=i+1
