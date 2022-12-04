txt = open("input_day04.txt", 'r').read()
txt_list = txt.split("\n")

count_p1 = 0
count_p2 = 0

for pair in txt_list:
    pair = pair.replace("-",",")
    pair_list = pair.split(",")

    clean1 = list(range(int(pair_list[0]),int(pair_list[1])+1))
    clean2 = list(range(int(pair_list[2]),int(pair_list[3])+1))

    # Count the subset
    if set(clean1).issubset(set(clean2)) or set(clean2).issubset(set(clean1)):
        count_p1 += 1

    # Count the overlap
    if bool(set(clean1).intersection(set(clean2))) or bool(set(clean2).intersection(set(clean1))):
        count_p2 += 1

# Part 1 answer
print("Part 1 answer: ", str(count_p1))

# Part 2 answer
print("Part 2 answer: ", str(count_p2))


