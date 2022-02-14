from math import log10

a = int (input("Введите число а: "))
b = int (input("Введите число b: "))

print (a, "+", b, "=", a + b )
print (a, "-", b, "=", a - b )
print (a, "*", b, "=", a * b )
print (a, "/", b, "=", a / b )
print (a, "%", b, "=", a % b )
print ("Десятичный логарифм", a, "=", log10(a))
print (a, "в степени", b, "=", a ** b )