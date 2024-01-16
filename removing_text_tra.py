#Prepare data by removing "TRA" and "TRA0"

line1 = lambda: print("_"*54)

tra_input= input(f"TRA Input =")
#tra_input = tra_input.replace(" ", ",")
print(type(tra_input))
line1()

tra_input = tra_input.replace("TRA0", "")
tra_input = tra_input.replace("TRA", "")
tra_input = tra_input.split(" ")

print(f"Number of TRAs = {len(tra_input)}")
print(f'After Split = "class list" =>{tra_input}')
print(type(tra_input))
line1()

print(f"Number of TRAs = {len(tra_input)}")
for i in tra_input:
        print(f'{i}, ', end ="")
        
print()
line1()

#End