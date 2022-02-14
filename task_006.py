NALOG = 0.13
TIPS = 0.18
cost = float (input("Сумма счета: "))
nalog = cost * NALOG
tips = cost * TIPS
total = cost + nalog + tips

print ("Налог %.2f, чаевые - %.2f, общая сумма заказа: %.2f" % (nalog,tips,total))
