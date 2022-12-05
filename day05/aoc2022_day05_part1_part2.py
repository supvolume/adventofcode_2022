txt = open("input_day05.txt", 'r').read()
txt_list = txt.split("\n\n")

# Pivot cargo (row <> col)
cargo = txt_list[0].replace("[","").replace("]","").split("\n")
for n_row in range(len(cargo)):
    cargo[n_row] = cargo[n_row].rstrip().replace("    ","_ ")

p_cargo = list(cargo[-2].split(" "))

for n_row in range(len(cargo)-3,-1,-1):
    cargo_row = cargo[n_row].split(" ")
    for n_col in range(len(cargo_row)):
        if cargo_row[n_col] != " " and cargo_row[n_col] != "_" and len(cargo_row[n_col]) != 0:
            p_cargo[n_col] += cargo_row[n_col][0]

orders = txt_list[1].split("\n")

# Move cargo
for i in range(len(orders)):
    order = orders[i].split(" ")
    order_move = int(order[1])
    order_from = int(order[3])
    order_to = int(order[5])
    # move value
    # For part 1: place cargo one by one == reverse order >> uncomment [::-1]
    # For part 2: move all cargo at once == no reverse >> comment #[::-1]  
    p_cargo[order_to-1] += p_cargo[order_from-1][-order_move:]#[::-1]  
    # remove old value
    p_cargo[order_from-1] = p_cargo[order_from-1][:-order_move]
    #print(p_cargo)

top_stack = ""
for row in p_cargo:
        top_stack += row[-1]

# Answer
print("Part 1/2 answer: ", top_stack)
