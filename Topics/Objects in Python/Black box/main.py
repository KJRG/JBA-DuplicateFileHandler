# use the function blackbox(lst) that is already defined
my_list = [1, 2, 3]
list_from_blackbox = blackbox(my_list)
print("modifies" if id(my_list) == id(list_from_blackbox) else "new")
