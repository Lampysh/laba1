#Read data
n = int(input("Enter a three-digit number: "))
#Extract digits
a = n // 100
b = (n // 10) % 10
c = n % 10
#Reverse digits 
reverse = c * 100 + b * 10 + a
#Print the result
print("The reversed number is:", reverse)
