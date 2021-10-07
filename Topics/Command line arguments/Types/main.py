args = sys.argv

# further code of the script "add_four_numbers.py"
numbers = [int(x) for x in args[1:]]
print(sum(numbers))
