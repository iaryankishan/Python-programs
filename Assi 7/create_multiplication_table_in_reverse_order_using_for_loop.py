#wap to create multiplication table in reverse order using for loop
num= int(input("Enter the number "))
for i in range(10,5,-1):
    print(str(num) + " X " + str(i) + " = " + str(i*num))
    #print(f"{num} X {i} = {num*i}")
    
