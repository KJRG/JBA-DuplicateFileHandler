# read sums.txt
sums_file = open("sums.txt")
for line in sums_file:
    numbers = line.split()
    sum_of_numbers = int(numbers[0]) + int(numbers[1])
    print(sum_of_numbers)
sums_file.close()
