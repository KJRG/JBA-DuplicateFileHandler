# The parental gene sequences are stored here
one_ancestor = input()
other_ancestor = input()

# Calculate the identity of a new alien here
id_one = id(one_ancestor)
id_other = id(other_ancestor)
new_alien = (id_one + id_other) // 2
