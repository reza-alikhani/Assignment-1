name = input("NAME:")
family = input("FAMILY:")

a = float(input("First grade:"))
b = float(input("Second grade:"))
c = float(input("Third grade:"))

GPA = (a + b + c) / 3

if GPA >= 17 :
    result = "Great!"
if 12 <= GPA < 17 :
    result = "Normal!"
if GPA < 12 :
    result = "Fail!"

print (result)
