password = "Amos"
for i in range(3):
    pwd = input("Enter the password: ")
    j = 2
    if (pwd==password):
        print("Login Successful")
        break
    else:
        print("Wrong password, chances left: ",j-i)
        continue
print("Try again in next one hour!")