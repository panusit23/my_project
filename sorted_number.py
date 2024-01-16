# Clean Data
# Sorted TRA Number 
# Output: Add and Not Add TRA Wording

line1 = lambda: print("_"*54)

tra_input= input(f"TRA Input =")
tra_input = tra_input.replace(" ", "")
tra_input = tra_input.replace(",", "")
print(type(tra_input))
line1()

tra_input = tra_input.split("TRA")
print(f"Number of TRAs in Under Test = {len(tra_input)-1}")
print(f'After Split = "class list" =>{tra_input}')
print(type(tra_input))
line1()

tra_list_add = []

for i in range(len(tra_input)):
    tra_list_add.append(tra_input[i])
tra_list_add = sorted(tra_list_add)

print(f"Number of TRAs in Under Test (with TRA) = {len(tra_list_add)-1}")

for j in tra_list_add:
    if j != "":
        print(f'TRA{j}, ', end ="")
line1()

print(f"Number of TRAs in Under Test (without TRA) = {len(tra_list_add)-1}")
for j in tra_list_add:
    if j != "":
        print(f'{j}, ', end ="")

#End