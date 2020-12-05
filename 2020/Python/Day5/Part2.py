passes = open("input.txt", "r").readlines()
passes = [x.replace("\n", "") for x in passes]

seat_ids = []
for s in passes:
    rows = [x for x in range(128)]
    columns = [x for x in range(8)]
    row, column = 0, 0
    for x in s:
        if x == "F":
            rows = rows[:int(len(rows)/2)]
        elif x == "B":
            rows = rows[int(len(rows)/2):]
        elif x == "R":
            columns = columns[int(len(columns)/2):]
        elif x == "L":
            columns = columns[:int(len(columns)/2)]

    seat_ids.append((rows[0]*8)+columns[0])

seats = sorted(seat_ids)

for x in range(len(seats)):
    if seats[x]+1 != seats[x+1] and seats[x]+2 == seats[x+1]:
        print(seats[x]+1)
        break

