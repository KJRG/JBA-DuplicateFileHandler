input_text = input()
digits = [int(x) for x in input_text]
odd_digits = [x for x in digits if x % 2 == 1]
print(odd_digits)
