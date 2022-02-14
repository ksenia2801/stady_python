souvenir = int(input("Введите кол-во сувениров: "))
trinkets = int(input("Введите кол-во безделушек: "))

ves_s = int (75)
ves_t = int (112)

sum_s = souvenir * ves_s
sum_t = trinkets * ves_t
total = sum_s + sum_t

print("Общий вес посылки:" , total)