def avg(x, y):
    return (x + y) / 2


digits = [int(x) for x in input()]
running_average = list()
for i in range(len(digits) - 1):
    running_average.append(avg(digits[i], digits[i + 1]))
print(running_average)
