a = float(input("weight in kg"))
b = float(input("height in meter"))

c = a / b**2

if c < 18.5 :
    result = "UNDERWEIGHT!"
if 18.5 < c < 24.9 :
    result = "NORMAL!"
if 24.9 < c < 29.9 :
    result = "OVERWEIGHT!"
if 29.9 < c < 34.9 :
    result = "OBESE!"
if 34.9 < c :
    result = "EXTREMELY OBESE!"

print (result)
