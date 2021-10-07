# read test_file.txt
test_file = open('test_file.txt', 'rt', encoding='utf-16')
print(test_file.readline())
test_file.close()
