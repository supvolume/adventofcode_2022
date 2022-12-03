txt = open("input_day01.txt", 'r').read()
txt_list = list(txt.split("\n\n"))
int_nest = [[int(j) for j in i.split("\n")] for i in txt_list]


max_num = 0
sum_list = []
for i in int_nest:
    if sum(i) > max_num:
        max_num = sum(i)
    sum_list.append(sum(i))

top3 = sorted(sum_list, reverse=True)[:3]

#Part 1 answer
print("part1: ", str(max_num))

print(sum(top3))
