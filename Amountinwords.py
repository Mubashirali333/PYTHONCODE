amount = int(input("Enter value "))

thousand = amount//1000
rem = amount%1000

hundred = temp//100
temp = temp%100

ten = temp//10
one = temp%10

print(thousand)
print(hundred)
print(ten)
print(one)