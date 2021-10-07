# write your code here
# remember: the variable email is already defined
at_symbol_index = email.index("@")
local_part_of_address = email[:at_symbol_index]
print(local_part_of_address)
