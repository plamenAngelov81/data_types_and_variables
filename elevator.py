people = int(input())
capacity = int(input())

turns = 0

while True:
    people -= capacity
    turns += 1
    if people <= 0:
        break
print(turns)
