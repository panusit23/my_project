#Check Duplicate Number

from collections import Counter

'''
def find_duplicate(tra):
    counter = Counter(tra)
    duplicate = []
    
    for item, count in counter.items():
        if count > 1:
            duplicate.append(item)
    
    return duplicate
'''

def find_duplicate(tra):
    counter = Counter(tra)
    return [item for item, count in counter.items() if count > 1]

tra_list = [
    
1201, 1309, 1509, 1613, 1713, 1901, 2013, 2206, 2401, 2505, 2610, 2709, 2901,
1205, 1402, 1513, 1617, 1717, 1905, 2102, 2210, 2405, 2509, 2614, 2801, 2905,
1209, 1406, 1601, 1701, 1801, 2001, 2106, 2302, 2409, 2513, 2618, 2805, 2909,
1301, 1501, 1605, 1705, 1805, 2005, 2110, 2306, 2413, 2602, 2701, 2809, 3002,
1305, 1505, 1609, 1709, 1809, 2009, 2202, 2310, 2501, 2606, 2705, 2813,
    
1202, 1401, 1510, 1614, 1714, 1902, 2101, 2209, 2402, 2506, 2613, 2710, 2902,
1206, 1405, 1514, 1618, 1718, 1906, 2105, 2301, 2406, 2510, 2617, 2802, 2906,
1210, 1409, 1602, 1702, 1802, 2002, 2109, 2305, 2410, 2601, 2621, 2806, 3001,
1302, 1502, 1606, 1706, 1806, 2006, 2201, 2309, 2414, 2605, 2702, 2810,
1306, 1506, 1610, 1710, 1810, 2010, 2205, 2313, 2502, 2609, 2706, 2814, 2814

]

print(f'All TRA = {len(tra_list)}')
print('------------------------------')
duplicate = find_duplicate(tra_list)
print(f'All TRA Duplicate = {len(duplicate)}')
print("Duplicate Values:", duplicate)

#End