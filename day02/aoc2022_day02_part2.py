txt = open("input_day02.txt", 'r').read()
txt_list = list(txt.split("\n"))

# PART2
# A == rock (1)
# B == paper (2)
# C == scissors (3)

# X == lose >> 0
# Y == draw >> 3
# Z == win >> 6

total_points = 0
for i in txt_list:
    if i[0] == "A":    # rock
        if i[2] == "X":    # lose
            total_points += (0+3)    # scissors
        if i[2] == "Y":    # draw
            total_points += (3+1)    # rock
        if i[2] == "Z":    #  win
            total_points += (6+2)    # paper
            
    if i[0] == "B":    # paper
        if i[2] == "X":    # lose
            total_points += (0+1)    # rock
        if i[2] == "Y":    # draw
            total_points += (3+2)    # paper
        if i[2] == "Z":    # win
            total_points += (6+3)    # scissors

    if i[0] == "C":    # scissors
        if i[2] == "X":    # lose
            total_points += (0+2)    # paper
        if i[2] == "Y":    # draw
            total_points += (3+3)    # scissors
        if i[2] == "Z":    # win
            total_points += (6+1)    # rock

# part 2 answer
print("Part 2 answer: ", str(total_points))
            
            
