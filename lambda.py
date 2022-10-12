# Вычисление максимального значения между двумя числами
                      #Пример 1
# a = 15
# b = 13
# if a>b:
#     max = a
# else:
#  max = b
# print(max)
    

# Вычисление максимального значения между двумя числами lambda
                   
max = (lambda a, b: a if a>b else b)
print(max(15, 13))


# Сумма и произведение чисел, Пример 2

# def sum (x,y):
#      return x + y
# print(sum(5,4))

# def mylt(x,y):
#     return x * y
# print(mylt(5,4))

# Сумма и произведение чисел lambda

sum = lambda x, y: x+y
print(sum(5,7))
mylt = lambda x, y: x*y
print(mylt(5,7))