# Пример 1
#Вывести список

# users = ["users1","users2","users3","users4","users5"]
# ids = [4,5,9,14,17]
# salar = [111,222,333,444,555] 
# print(users)
# print(ids)
# print(salar)

# Объеденить список с помощью zip

users = ["users1","users2","users3","users4","users5"]
ids = [4,5,9,14,17]
salar = [111,222,333,444,555]

data = list(zip(users,ids, salar))
print(data)

                      #Пример 2

# s = 'abc'
# t = (10, 20, 30)
# u = (-5, -10, -15)
# print(s)
# print(t)
# print(u)
                      
s = 'abc'
t = (10, 20, 30)
u = (-5, -10, -15)
data =list(zip(s,t,u))
print(data)