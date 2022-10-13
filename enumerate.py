
                    # Пример 1
# users = ["users1","users2","users3","users4","users5"]
# data = list(enumerate(users))
# print(data)
                    # Пример 2
# names = ["users1","users2","users3","users4","users5"]
# data = enumerate(names, 10)
# print(list(data))
                    # Пример 3
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_d = [(i, x) for i, x in enumerate(list_a)]
print(list_d)