txt = open("input_day03.txt", 'r').read()
txt_list = txt.split("\n")

# Get the alphabet using ASSCI value
items = [chr(value) for value in range(97, 123)] + [chr(value) for value in range(65, 91)]
priority = list(range(1,53))
items_prio = dict(zip(items, priority))

# PART 1
comp1 = []
comp2 = []
sum_prio = 0
for rucksack in txt_list:
    # Separate compartment 
    n = int(len(rucksack)/2)
    comp1 = list(rucksack)[:n]
    comp2 = list(rucksack)[n:]
    # Find item type that appears in both compartments
    share_item = set(comp1).intersection(set(comp2))

    sum_prio += items_prio[list(share_item)[0]]

print("Part1 answer: ", str(sum_prio))
    

# PART 2
count = 0
sum_prio2 = 0
for i in range(2,len(txt_list)+1,3):
    rucksack1 = list(txt_list[i-2])
    rucksack2 = list(txt_list[i-1])
    rucksack3 = list(txt_list[i])
    # Find item type that is common in the group of three
    share_item2 = set(rucksack1).intersection(set(rucksack2)).intersection(set(rucksack3))

    sum_prio2 += items_prio[list(share_item2)[0]]

print("Part2 answer: ", str(sum_prio2))
