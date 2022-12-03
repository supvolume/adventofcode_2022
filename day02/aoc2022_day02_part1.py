txt = open("input_day02.txt", 'r').read()
txt_list = list(txt.split("\n"))

# PART1
# A/X == rock (1)
# B/Y == paper (2)
# C/Z == scissors (3)

# lost >> 0
# draw >> 3
# win >> 6

total_points = 0
for i in txt_list:
    if i[0] == "A":    # rock
        if i[2] == "X":    # rock
            total_points += (3+1)    # draw
        if i[2] == "Y":    # paper
            total_points += (6+2)    # win
        if i[2] == "Z":    # scissors
            total_points += (0+3)    # lost
            
    if i[0] == "B":    # paper
        if i[2] == "X":    # rock
            total_points += (0+1)    # lost
        if i[2] == "Y":    # paper
            total_points += (3+2)    # draw
        if i[2] == "Z":    # scissors
            total_points += (6+3)    # win

    if i[0] == "C":    # scissors
        if i[2] == "X":    # rock
            total_points += (6+1)    # win
        if i[2] == "Y":    # paper
            total_points += (0+2)    # lost
        if i[2] == "Z":    # scissors
            total_points += (3+3)    # draw

# part 1 answer
print("Part 1 answer: ", str(total_points))
            
            
