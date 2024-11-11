immutable_var = 5, 6, 7, 'apple', 'true'
print('Immutable tuple:', immutable_var)
#immutable_var[2] = 1
#print(immutable_var) ошибка - неизменяемая коллекция
mutable_list = [7, 6, 5, 'apple', 'true']
mutable_list[3] = 'world'
print('Mutable list:', mutable_list)
