# For discontinued data packets combination
# Find total bandwidth
# Export to .txt

import random

line1 = lambda: print("-"*30)
line2 = lambda: print("="*30)

collected_data = []
threshold_rate_lower = 8.6  # Kbits/sec
threshold_rate_higher = 11.4  # Kbits/sec

time_random = ['00', '01', '00', '01', '00', '01', '00', '01', '00', '01', '00', '01', '00', '01', '00', '01', '02']

bytes_value_gen= [

    '1.12', '1.22', '1.17', '1.22', '1.22', '1.27', '1.17', '1.22', '1.22', '1.22', '1.22', '1.27', '1.17', '1.22',
    '1.22', '1.22', '1.27', '1.22', '1.17', '1.22', '1.22', '1.27', '1.17', '1.27', '1.22', '1.17', '1.27', '1.22',
    '1.17', '1.22', '1.27', '1.22', '1.17', '1.27', '1.22', '1.22', '1.17', '1.27', '1.22', '1.17', '1.27', '1.22',
    '1.22', '1.17', '1.27', '1.22', '1.17', '1.22', '1.27', '1.17', '1.22', '1.22', '1.22', '1.22', '1.27', '1.22',
    '1.17', '1.22', '1.27', '1.17', '1.22', '1.22', '1.27', '1.17', '1.27', '1.17', '1.22', '1.22', '1.22', '1.22',
    '1.22', '1.22', '1.22', '1.22', '1.22', '1.22', '1.22', '1.27', '1.17', '1.22', '1.27', '1.22', '1.22', '1.22',
    '1.17', '1.22', '1.22', '1.22', '1.22', '1.22', '1.22', '1.27', '1.17', '1.22', '1.22', '1.22', '1.22', '1.22',
    '1.27', '1.17', '1.22', '1.27', '1.17', '1.27', '1.17', '1.22', '1.22', '1.22', '1.27', '1.17', '1.27', '1.22',
    '1.22', '1.22', '1.22', '1.22', '1.22', '1.12', '1.32', '1.17', '1.27', '1.22', '1.22', '1.22', '1.22', '1.22',
    '1.22', '1.22', '1.22', '1.17', '1.27', '1.17', '1.22', '1.27', '1.22', '1.17', '1.22', '1.22', '1.22', '1.22',
    '1.22', '1.27', '1.22', '1.22', '1.22', '1.17', '1.27', '1.22', '1.22', '1.22', '1.22', '1.22', '1.17', '1.22',
    '1.22', '1.22', '1.22', '1.32', '1.17', '1.17', '1.22', '1.27', '1.22', '1.17', '1.22', '1.17', '1.27', '1.22',
    '1.22', '1.27', '1.22', '1.12', '1.32', '1.22', '1.17', '1.22', '1.27', '1.17', '1.27', '1.22', '1.22'

]

bits_value_gen = [

    '9.10', '10.0', '9.58', '9.96', '10.1', '10.3', '9.64', '9.99', '9.97', '9.98', '9.96', '10.5', '9.57', '10.0',
    '9.93', '10.1', '10.4', '9.92', '9.58', '10.1', '9.93', '10.4', '9.52', '10.5', '9.99', '9.58', '10.3', '10.0',
    '9.65', '9.99', '10.3', '9.97', '9.70', '10.3', '10.0', '9.96', '9.64', '10.3', '10.0', '9.64', '10.4', '9.89',
    '10.0', '9.70', '10.3', '10.0', '9.67', '9.92', '10.4', '9.69', '9.97', '9.96', '10.1', '9.90', '10.5', '9.97',
    '9.54', '9.96', '10.4', '9.70', '9.96', '10.1', '10.3', '9.54', '10.5', '9.59', '9.95', '10.1', '9.94', '9.96',
    '10.0', '9.93', '10.1', '9.92', '10.1', '9.92', '10.1', '10.4', '9.59', '9.93', '10.4', '10.1', '9.93', '10.1',
    '9.59', '9.96', '9.97', '10.1', '9.93', '9.94', '10.1', '10.3', '9.65', '10.0', '9.94', '10.1', '9.93', '10.1',
    '10.3', '9.67', '9.93', '10.4', '9.71', '10.3', '9.68', '9.94', '10.1', '9.93', '10.3', '9.68', '10.4', '10.1',
    '9.98', '9.94', '10.1', '9.95', '10.0', '9.21', '10.8', '9.55', '10.5', '9.93', '10.1', '9.97', '10.1', '9.96',
    '9.94', '10.1', '9.95', '9.53', '10.5', '9.56', '9.93', '10.5', '10.1', '9.51', '10.1', '9.96', '9.95', '10.1',
    '9.94', '10.3', '10.1', '10.0', '9.98', '9.55', '10.5', '9.97', '9.97', '10.1', '10.0', '9.95', '9.56', '10.1',
    '9.94', '10.1', '9.96', '10.7', '9.71', '9.51', '10.1', '10.4', '9.94', '9.57', '10.0', '9.68', '10.4', '9.96',
    '10.1', '10.3', '10.0', '9.19', '10.7', '10.1', '9.58', '9.97', '10.5', '9.56', '10.3', '10.1', '10.1'

]

pair_value = list(zip(bytes_value_gen, bits_value_gen))
space_word = '                 '  # space = 17

#------------------------------------------#

file_name = input('File Name = \n')
#file_name = "test"
#lot_num = str(input('lot [ ?] =  \n'))
lot_num = "5"
stop_time = int(input("stop_time = \n"))
stop_time = stop_time+1
line1()
#------------------------------------------#

# Find total bandwidth
def find_total_bandwidth():
    file_name = 'Modified_Iperf.txt'

    with open(file_name, 'r') as file:
        data = file.readlines()
    sum_bytes = 0
    sum_kbits = 0

    count = 0
    for i in range(len(data)):
        # Split the line into parts
        line = data[i]
        parts = line.split()

        # find in KBytes
        transfer_rate_bytes = float(parts[-4])
        transfer_rate_bytes_unit = str(parts[-3])

        # check unit if bytes => Bytes/1000
        if transfer_rate_bytes_unit == "Bytes" and transfer_rate_bytes_unit != 0:
            transfer_rate_bytes = transfer_rate_bytes / 1000
        sum_bytes += transfer_rate_bytes

        # find in Kbits
        transfer_rate_kbits = float(parts[-2])
        transfer_rate_kbits_unit = str(parts[-1])
        # check unit if bits => bits/1000
        if transfer_rate_kbits_unit == "bits/sec" and transfer_rate_kbits_unit != 0:
            transfer_rate_kbits = transfer_rate_kbits / 1000
        sum_kbits += transfer_rate_kbits
        count += 1

    print(f'transfer_rate_Bytes(Kbps) = {round(sum_bytes, 3)}K')
    print(f'transfer_rate_Bytes(Mbps) = {round(sum_bytes / 1000, 3)}M')
    print(f'transfer_rate_bits(Kbps) = {round(sum_kbits, 3)}K')
    print(f'transfer_rate_bits(Mbps) = {round(sum_kbits / 1000, 3)}M')
    print(f'Read Rows = {count}')

line1()
#------------------------------------------#

def write_data_format(row):
    if row == 0:
        modified_parts = '[  {}]   {}.00-{}.{}   sec  '.format(lot_num, row, row + 1, random_time_2)
    elif 0 < row < 9:
        modified_parts = '\n[  {}]   {}.{}-{}.{}   sec  '.format(lot_num, row, random_time_1, row + 1, random_time_2)
    elif row == 9:
        modified_parts = '\n[  {}]   {}.{}-{}.{}  sec  '.format(lot_num, row, random_time_1, row + 1, random_time_2)
    elif 9 < row < 99:
        modified_parts = '\n[  {}]  {}.{}-{}.{}  sec  '.format(lot_num, row, random_time_1, row + 1, random_time_2)
    elif row == 99:
        modified_parts = '\n[  {}]  {}.{}-{}.{} sec  '.format(lot_num, row, random_time_1, row + 1, random_time_2)
    else:
        modified_parts = '\n[  {}] {}.{}-{}.{} sec  '.format(lot_num, row, random_time_1, row + 1, random_time_2)
    return modified_parts

#------------------------------------------#

with open(file_name+'.txt') as file:
    read_packet = file.readlines()
    print(f"Read Packet = {len(read_packet)}")
    row_add = stop_time - (len(read_packet)+1)
    print(f"Add Rows Packet = {row_add}")
    row_actual = len(read_packet) + row_add
    print(f"Total Rows Packet After Modified = {row_actual}")
    
    # Loop All Rows
    for row_i in range(0, row_actual):
        # random time
        random_time_1 = random.choice(time_random)
        random_time_2 = random.choice(time_random)

        # random replace data
        replace_data = random.choice(pair_value)
        replace_bytes_value = replace_data[0]
        replace_bits_value = replace_data[1]
        #print(f'{replace_bytes_value} and {replace_bits_value}')

        # use data in actual value
        if row_i < len(read_packet):
            data_packet = read_packet[row_i]
            data_packet_list = data_packet.split()

            bits_unit = data_packet_list[-1]
            bits_value = data_packet_list[-2]
            bytes_unit = data_packet_list[-3]
            bytes_value = data_packet_list[-4]

            # str to float
            transfer_rate = float(bits_value)

            # Check if the transfer rate is lower than the threshold
            if (transfer_rate < threshold_rate_lower) or (transfer_rate > threshold_rate_higher):
                # Replace the transfer rate
                data_packet_list[-2] = replace_bits_value
                data_packet_list[-4] = replace_bytes_value

                bits_unit = "Kbits/sec"
                bits_value = str(data_packet_list[-2])
                bytes_unit = "KBytes"
                bytes_value = str(data_packet_list[-4])

            if (bytes_value != "1000") and (bytes_unit == "Bytes"):
                # add 1 space
                packet_value = ' {} {}  {} {}'.format(bytes_value, bytes_unit, bits_value, bits_unit)
            else:
                # no space
                packet_value = '{} {}  {} {}'.format(bytes_value, bytes_unit, bits_value, bits_unit)

            modified_parts = write_data_format(row_i)

        # use data in gen value (rows are over actual packets)
        else:
            if (bytes_value != "1000") and (bytes_unit == "Bytes"):
                # add 1 space
                packet_value = '{} {}  {} {}'.format(replace_bytes_value, bytes_unit, replace_bits_value, bits_unit)
            else:
                # no space
                packet_value = '{} {}  {} {}'.format(replace_bytes_value, bytes_unit, replace_bits_value, bits_unit)

            modified_parts = write_data_format(row_i)

        modified_data = modified_parts + packet_value + space_word
        print(modified_data)
        collected_data.append(modified_data)
        
with open('Modified_Iperf.txt', 'w') as new_file:
    count_output = 0
    for row_write in collected_data:
        new_file.write(row_write)
        count_output += 1

line1()
print(f'Write Rows = {count_output}')
line1()
find_total_bandwidth()
line2()
print('!!!!!!Done!!!!!!')
line2()

# End