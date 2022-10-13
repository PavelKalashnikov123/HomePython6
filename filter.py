
# Фильтрация нечетных значений    Пример 1
# numbers = [1,2,3,4,5,6]
# for number in numbers:
#    if number % 2 == 1:
#     print(number)


numbers = [x for x in range(7)]
res = list(filter(lambda x: x%2==1, numbers))
print(res)


                     # ПРИМЕР 2
                     # Перечень булевых значений, которые могут принимать вид True или False

# bools = ['bool', 0, None, True, False, 1, 1-1, 2%2]
# print (bools[0])
# print (bools[2])
# print (bools[5])


# # Перечень булевых значений, которые могут принимать вид True или False
bools = ['bool', 0, None, True, False, 1, 1-1, 2%2]
out = filter(None, bools)
# Вывод результата
for iter in out:
    print(iter)

