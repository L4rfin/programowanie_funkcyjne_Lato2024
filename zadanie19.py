def update_tuple(original_tuple, value, index):
    temp_list = list(original_tuple)
    temp_list[index] = value
    return tuple(temp_list)


my_tuple = (1, 2, 3)
updated_tuple = update_tuple(my_tuple, 4, 1)

print(updated_tuple)
print(my_tuple)
