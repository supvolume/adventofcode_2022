txt = open("input_day06.txt", 'r').read()

# PART 1

first_start = ""
starter = txt[:3]
starter_lo = 0

for i in range(3,len(txt)):
    start_check = txt[i-3:i+1]
    if len(set(start_check)) == len(start_check):
        first_start = start_check
        starter_lo = i
        break
   
#print(first_start)

# Part 1 answer
print("Part 1 answer: ", str(i+1))


# PART 2
first_start = ""
starter = txt[:13]
starter_lo = 0

for i in range(13,len(txt)):
    start_check = txt[i-13:i+1]
    if len(set(start_check)) == len(start_check):
        first_start = start_check
        starter_lo = i
        break
    
#print(first_start)
print("Part 2 answer: ", str(i+1))
