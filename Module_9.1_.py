def apply_all_func(int_list, *functions):
    rezults = {}

    for function in functions:
        rezults[function.__name__] = function(int_list)

    return rezults

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
