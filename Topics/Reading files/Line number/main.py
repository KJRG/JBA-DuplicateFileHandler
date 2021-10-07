# read sample.txt and print the number of lines
sample_file = open("sample.txt")
number_of_lines = sum([1 for line in sample_file])
sample_file.close()
print(number_of_lines)
