
                  # ПРИМЕР 1
        #Преобразование в верхний регистр

# directions = ["север", "юг", "восток", "запад"]
# directions_upper = []
# for direction in directions:
#     d = direction.upper()
#     directions_upper.append(d)
# print(directions_upper)

       #Преобразование в верхний регистр с функцией map

# def to_upper_case(s):
#     return s.upper()
# directions = ["север", "юг", "восток", "запад"]
# directions_upper = map(to_upper_case, directions)
# print(list(directions_upper))

                     # Пример 2
#создать список квадратных чисел от 1 до 10
# n = []
# for i in range(1, 11):
#      n.append(i**2)
# print(n)

#создать список квадратных чисел от 1 до 10 с функцией map

squares = map(lambda n: n*n, range(1, 11))
print(list(squares))