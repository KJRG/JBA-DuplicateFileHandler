#  You can experiment here, it won’t be checked
import sys


def count_occurrences_in_file(filepath, text_to_find):
    file = open(filepath)
    total_occurrences_in_file = 0
    for line in file:
        if line[:-1] == text_to_find:
            total_occurrences_in_file += 1
    file.close()
    return total_occurrences_in_file


if len(sys.argv) > 1:
    print(count_occurrences_in_file(sys.argv[1], "summer"))
else:
    print("Wrong number of arguments. You have to pass the filename.")
