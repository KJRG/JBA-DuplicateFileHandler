# write your code here


MONTHS_IN_YEAR = 12


def get_yearly_income(monthly_income):
    return MONTHS_IN_YEAR * monthly_income


with open('salary.txt', 'r') as in_file, open('salary_year.txt', 'w') as out_file:
    for line in in_file:
        yearly_income = get_yearly_income(int(line.strip()))
        out_file.write(str(yearly_income) + '\n')
