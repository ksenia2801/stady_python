STAVKA = 0.04

cost = float (input("Начальная сумма депозита: "))

first = cost * STAVKA
sum_f = cost + first

second = sum_f * STAVKA
sum_s = sum_f + second

third = sum_s * STAVKA
sum_t = sum_s + third








print ("Первый год %.2f, второй год - %.2f, общая сумма: %.2f" % (sum_f, sum_s, sum_t))