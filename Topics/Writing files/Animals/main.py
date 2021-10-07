# read animals.txt
# and write animals_new.txt
animals_file = open('animals.txt', 'r')
animals_new_file = open('animals_new.txt', 'w')
for line in animals_file:
    text_to_write = line.replace('\n', ' ')
    animals_new_file.write(text_to_write)
animals_new_file.close()
animals_file.close()
