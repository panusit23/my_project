#Split text (TRA) from concat data in excel

line1 = lambda: print("_"*54)

tra_input = input(f"TRA Input =")
line1()

tra_input_split = tra_input.split("TRA")

print(f"Number of TRAs in Under Test = {len(tra_input_split)-1}")
line1()

for tra_1 in tra_input_split:
    print(f"{tra_1},", end = "")

#End