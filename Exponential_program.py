num = int(input("Enter the number: "))
exp = int(input("Enter the exponent: "))
result= 1
for i in range(1, (exp+1)):
    result = result *num
print("The result is: ",result)
    