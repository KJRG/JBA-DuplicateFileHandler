seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# create a list of days here
SECONDS_IN_DAY = 60 * 60 * 24
full_days = [s // SECONDS_IN_DAY for s in seconds]
print(full_days)
