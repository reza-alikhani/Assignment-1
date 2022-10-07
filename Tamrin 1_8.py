a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the third number"))

if a < b + c and b < a + c and c < a + b :
    result = "Yes, it is possible to draw a triangle"
else :
    result = "No, It isn't possible to draw a triangle"

print (result)


