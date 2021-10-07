numeric_sequence = input()
digits = [int(x) for x in numeric_sequence]
running_total = [sum(digits[:i+1]) for i in range(len(digits))]
print(running_total)
