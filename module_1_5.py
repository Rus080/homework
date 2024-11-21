immutable_var = 1, 2, 'yes', True
print('immutable_var = ', immutable_var)
# immutable_var[0] = 8
print('''"immutable_var[0] = 8" - Изменение внести не возможно, 
так как данные внесенные в кортеж является постоянными,за исключением случаев когда в кортеж внесен список''')

mutable_list = ['apple', 1, 2, True]
print('mutable_list before = ', mutable_list)
mutable_list[0] = 'lemon'
mutable_list[1] = 8
mutable_list[2] = 6
mutable_list[3] = 3 > 5
print('mutable_list after = ', mutable_list)
