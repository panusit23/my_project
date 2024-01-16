# Split CSV Into Multiple Files

selected_row = []

output_file = int(input('How many CSV files do you want?: ' ))
print('='*42)

for i in range(1, output_file+1):
    print(f'Output Files = {i}')

    row_fr = 0
    row_to = 0
    selected_row.clear()

    row_fr = int(input("Split Rows From: "))
    row_to = int(input("Split Rows To: "))
    print(f'From {row_fr} To {row_to}')
    
    #with open('VSCode\syslog_combine.csv', 'r') as file:
    with open('syslog_combine.csv', 'r') as file:
            read_file = file.readlines()
    print(f'=>Read all rows from "syslog_combine" = {len(read_file)}')

    for j in range(row_fr, row_to):
        selected_row.append(read_file[j])

    #write_file = f'VSCode\syslog_combine_round_{i} +.csv'
    write_file = f'syslog_combine_round_{i} +.csv'
    with open(write_file, 'w') as file_1:
            for row in selected_row:
                file_1.write(row)
    print(f'=>Selected row = {len(selected_row)}')

    print('---------------------')
print("!!!!!!!!!!!!!Done!!!!!!!!!!!!!")

#End