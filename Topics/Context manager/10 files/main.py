# write your code here
for i in range(1, 11):
    filename = f'file{i}.txt'
    with open(filename, 'w') as file_to_write:
        file_to_write.write(str(i))
