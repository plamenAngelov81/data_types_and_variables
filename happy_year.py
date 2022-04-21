year = int(input())
next_year = year
while True:
    next_year += 1
    str_next_year = str(next_year)
    set_next_year = set(str_next_year)
    if len(str_next_year) == len(set_next_year):
        print(next_year)
        break
