my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    number = my_list[i]
    i += 1
    if number == 0:
     continue
    elif number < 0:
     break
    elif i == len(my_list):
        print(number)
    else:
     print(number)





