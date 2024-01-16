# Pink 819 TRA in Area Under Test
# Redundancy Plan A and B

line1 = lambda: print("_" * 54)
line3 = lambda: print("=" * 54)

# see routing doc
tra_under_test = {
    
 
    
}

# ------------------------------------------------------#

# see from analyze
tra_present = {
    
   
    
}


# ------------------------------------------------------#

def area():
    global tra_under_test, tra_present

    tra_absent = tra_under_test - tra_present

    print(f"TRA in Area Under Test = {sorted(tra_under_test)}")
    print(f"Number of TRA Area Under Test = {len(tra_under_test)}")
    line1()
    print(f"TRA_present={sorted(tra_present)}")
    print(f"Number of TRA Present = {len(tra_present)}")
    line1()
    print(f"TRA_absent={sorted(tra_absent)}")
    print(f"Number of TRA Absent = {len(tra_absent)}")
    line1()

# =======================================================
# PK Depot TRA Down
# =======================================================
# PF11704, Stabling Yard, S0

plan_a_s = {9125, 9126, 9129, 9110, 9137, 9138, 9141, 9145}

plan_b_s = {9106, 9118, 9121, 9122, 9130, 9133, 9134, 9142}

# ------------------------------------------------------#

# PF11703, Mainworkshop

plan_a_m = {9125, 9126, 9129, 9110, 9137, 9138, 9141, 9145}

plan_b_m = {9106, 9118, 9121, 9122, 9130, 9133, 9134, 9142}

# ------------------------------------------------------#

# "Platform ID P11703 or P11704 to TT" and "Platform ID P11703 or P11704 to PK30"

plan_a_a = {9102, 9109, 9114}

plan_b_a = {9101, 9105, 9117, 9113}

# ------------------------------------------------------#

# Main Line PK30-PK12
plan_a_ml_2 = {

    1201, 1309, 1509, 1613, 1713, 1901, 2013, 2206, 2401, 2505, 2610, 2709, 2901,
    1205, 1402, 1513, 1617, 1717, 1905, 2102, 2210, 2405, 2509, 2614, 2801, 2905,
    1209, 1406, 1601, 1701, 1801, 2001, 2106, 2302, 2409, 2513, 2618, 2805, 2909,
    1301, 1501, 1605, 1705, 1805, 2005, 2110, 2306, 2413, 2602, 2701, 2809, 3002,
    1305, 1505, 1609, 1709, 1809, 2009, 2202, 2310, 2501, 2606, 2705, 2813

}
plan_b_ml_2 = {

    1202, 1401, 1510, 1614, 1714, 1902, 2101, 2209, 2402, 2506, 2613, 2710, 2902,
    1206, 1405, 1514, 1618, 1718, 1906, 2105, 2301, 2406, 2510, 2617, 2802, 2906,
    1210, 1409, 1602, 1702, 1802, 2002, 2109, 2305, 2410, 2601, 2621, 2806, 3001,
    1302, 1502, 1606, 1706, 1806, 2006, 2201, 2309, 2414, 2605, 2702, 2810,
    1306, 1506, 1610, 1710, 1810, 2010, 2205, 2313, 2502, 2609, 2706, 2814

}
# ------------------------------------------------------#

# Main Line PK11-PK05
plan_a_ml_3 = {

    509, 701, 801, 901, 917, 1014,
    602, 705, 805, 905, 1002, 1102,
    501, 606, 709, 809, 909, 1006, 1106,
    505, 610, 713, 813, 913, 1010

}
plan_b_ml_3 = {

    601, 702, 802, 902, 1001, 1101,
    605, 706, 806, 906, 1005, 1105,
    502, 609, 710, 810, 910, 1009, 1109,
    506, 613, 714, 814, 914, 1013

}

# ------------------------------------------------------#

# Main Line PK04-PK01
plan_a_ml_4 = {

    101, 113, 209, 306, 318,
    105, 201, 213, 310, 402,
    109, 205, 302, 314

}
plan_b_ml_4 = {

    102, 114, 210, 309, 401,
    106, 202, 301, 313, 405,
    110, 206, 305, 317

}

# =======================================================

print("For 819 PK")
line3()
print("**************************************************************************************************************")
print("Depot Area")
print("Type: \"M\" ==> Platform ID P11703 to M1, M2, M3, M4, M5, M6, and M7.")
print("Type: \"S\" ==> Platform ID P11704 to S1+S0, S2, S3+S0, S4, S5+S0, S6, S7+S0, S8, S9, and S10.")
print("Type: \"A\" ==> [Platform ID P11703 or P11704 to TT] and [Platform ID P11703 or P11704 to PK30]")
print("\n")
print("Main Line Area")
print("Type: \"ML2\" ==> Main Line PK30-PK12")
print("Type: \"ML3\" ==> Main Line PK11-PK05")
print("Type: \"ML4\" ==> Main Line PK04-PK01")
line1()
select_area = str(input("Select Area Under Test = "))
print("\n")
print("**************************************************")
print("**************************************************")
print("Type: \"A\" ==> Redundancy Plan A")
print("Type: \"B\" ==> Redundancy Plan B")
line1()
select_plan = str(input("Select Redundancy Plan to down TRA = "))
print("\n")
print("**************************************************")
line3()
print("\n")
line3()

if select_area == "M":
    print("Platform ID P11703 to M1, M2, M3, M4, M5, M6, and M7.")
    line1()

    area()

    if select_plan == "A":
        tra_under_test_plan_a = tra_under_test - plan_a_m
        tra_absent_plan_a = tra_under_test_plan_a - tra_present

        print(f"====>\"OFF TRA\" Redundancy_plan_a={sorted(plan_a_m)}")
        print(f"====>Number of \"OFF TRA\" Redundancy Plan A = {len(plan_a_m)}")
        line1()
        print(f"====>\"ON TRA\" Redundancy Under Test_plan_a={sorted(tra_under_test_plan_a)}")
        print(f"====>Number of \"ON TRA\" Redundancy Under Test Plan A = {len(tra_under_test_plan_a)}")
        line1()
        print(f"====>TRA absent_plan_a={sorted(tra_absent_plan_a)}")
        print(f"====>Number of TRA Absent Plan A = {len(tra_absent_plan_a)}")
        line1()

    elif select_plan == "B":
        tra_under_test_plan_b = tra_under_test - plan_b_m
        tra_absent_plan_b = tra_under_test_plan_b - tra_present

        print(f"====>\"OFF TRA\" Redundancy_plan_b={sorted(plan_b_m)}")
        print(f"====>Number of \"OFF TRA\" Redundancy Plan B = {len(plan_b_m)}")
        line1()
        print(f"====>\"ON TRA\" Redundancy Under Test_plan_b={sorted(tra_under_test_plan_b)}")
        print(f"====>Number of \"ON TRA\" Redundancy Under Test Plan B = {len(tra_under_test_plan_b)}")
        line1()
        print(f"====>TRA absent_plan_b={sorted(tra_absent_plan_b)}")
        print(f"====>Number of TRA Absent Plan B = {len(tra_absent_plan_b)}")

    else:
        print("!!!!!!!!!!!!!!!  Wrong  !!!!!!!!!!!!!!!!")

# ------------------------------------------------------#

elif select_area == "S":
    print("Platform ID P11704 to S1+S0, S2, S3+S0, S4, S5+S0, S6, S7+S0, S8, S9, and S10.")
    line1()

    area()

    if select_plan == "A":
        tra_under_test_plan_a = tra_under_test - plan_a_s
        tra_absent_plan_a = tra_under_test_plan_a - tra_present

        print(f"====>\"OFF TRA\" Redundancy_plan_a={sorted(plan_a_s)}")
        print(f"====>Number of \"OFF TRA\" Redundancy Plan A = {len(plan_a_s)}")
        line1()
        print(f"====>\"ON TRA\" Redundancy Under Test_plan_a={sorted(tra_under_test_plan_a)}")
        print(f"====>Number of \"ON TRA\" Redundancy Under Test Plan A = {len(tra_under_test_plan_a)}")
        line1()
        print(f"====>TRA absent_plan_a={sorted(tra_absent_plan_a)}")
        print(f"====>Number of TRA Absent Plan A = {len(tra_absent_plan_a)}")
        line1()

    elif select_plan == "B":
        tra_under_test_plan_b = tra_under_test - plan_b_s
        tra_absent_plan_b = tra_under_test_plan_b - tra_present

        print(f"====>\"OFF TRA\" Redundancy_plan_b={sorted(plan_b_s)}")
        print(f"====>Number of \"OFF TRA\" Redundancy Plan B = {len(plan_b_s)}")
        line1()
        print(f"====>\"ON TRA\" Redundancy Under Test_plan_b={sorted(tra_under_test_plan_b)}")
        print(f"====>Number of \"ON TRA\" Redundancy Under Test Plan B = {len(tra_under_test_plan_b)}")
        line1()
        print(f"====>TRA absent_plan_b={sorted(tra_absent_plan_b)}")
        print(f"====>Number of TRA Absent Plan B = {len(tra_absent_plan_b)}")

    else:
        print("!!!!!!!!!!!!!!!  Wrong  !!!!!!!!!!!!!!!!")

# ------------------------------------------------------#

elif select_area == "A":
    print("[Platform ID P11703 or P11704 to TT] and [Platform ID P11703 or P11704 to PK30]")
    line1()

    area()

    if select_plan == "A":
        tra_under_test_plan_a = tra_under_test - plan_a_a
        tra_absent_plan_a = tra_under_test_plan_a - tra_present

        print(f"====>\"OFF TRA\" Redundancy_plan_a={sorted(plan_a_a)}")
        print(f"====>Number of \"OFF TRA\" Redundancy Plan A = {len(plan_a_a)}")
        line1()
        print(f"====>\"ON TRA\" Redundancy Under Test_plan_a={sorted(tra_under_test_plan_a)}")
        print(f"====>Number of \"ON TRA\" Redundancy Under Test Plan A = {len(tra_under_test_plan_a)}")
        line1()
        print(f"====>TRA absent_plan_a={sorted(tra_absent_plan_a)}")
        print(f"====>Number of TRA Absent Plan A = {len(tra_absent_plan_a)}")
        line1()

    elif select_plan == "B":
        tra_under_test_plan_b = tra_under_test - plan_b_a
        tra_absent_plan_b = tra_under_test_plan_b - tra_present

        print(f"====>\"OFF TRA\" Redundancy_plan_b={sorted(plan_b_a)}")
        print(f"====>Number of \"OFF TRA\" Redundancy Plan B = {len(plan_b_a)}")
        line1()
        print(f"====>\"ON TRA\" Redundancy Under Test_plan_b={sorted(tra_under_test_plan_b)}")
        print(f"====>Number of \"ON TRA\" Redundancy Under Test Plan B = {len(tra_under_test_plan_b)}")
        line1()
        print(f"====>TRA absent_plan_b={sorted(tra_absent_plan_b)}")
        print(f"====>Number of TRA Absent Plan B = {len(tra_absent_plan_b)}")

    else:
        print("!!!!!!!!!!!!!!!  Wrong  !!!!!!!!!!!!!!!!")
# ------------------------------------------------------#

elif select_area == "ML2":
    print("Main Line PK30-PK12")
    line1()

    area()

    if select_plan == "A":
        tra_under_test_plan_a = tra_under_test - plan_a_ml_2
        tra_absent_plan_a = tra_under_test_plan_a - tra_present

        print(f"====>\"OFF TRA\" Redundancy Plan A = {sorted(plan_a_ml_2)}")
        print(f"====>Number of \"OFF TRA\" Redundancy Plan A = {len(plan_a_ml_2)}")
        line1()
        tra_under_test_plan_a = tra_under_test.difference(plan_a_ml_2)
        print(f"====>\"ON TRA\" Redundancy Under Test Plan A = {sorted(tra_under_test_plan_a)}")
        print(f"====>Number of \"ON TRA\" Redundancy Under Test Plan A = {len(tra_under_test_plan_a)}")
        line1()
        print(f"====>TRA absent_plan_a={sorted(tra_absent_plan_a)}")
        print(f"====>Number of TRA Absent Plan A = {len(tra_absent_plan_a)}")
        line1()

    elif select_plan == "B":
        tra_under_test_plan_b = tra_under_test - plan_b_ml_2
        tra_absent_plan_b = tra_under_test_plan_b - tra_present

        print(f"====>\"OFF TRA\" Redundancy Plan B = {sorted(plan_b_ml_2)}")
        print(f"====>Number of \"OFF TRA\" Redundancy Plan B = {len(plan_b_ml_2)}")
        line1()
        tra_under_test_plan_b = tra_under_test.difference(plan_b_ml_2)
        print(f"====>\"ON TRA\" Redundancy Under Test Plan B = {sorted(tra_under_test_plan_b)}")
        print(f"====>Number of \"ON TRA\" Redundancy Under Test Plan B = {len(tra_under_test_plan_b)}")
        line1()
        print(f"====>TRA absent_plan_b={sorted(tra_absent_plan_b)}")
        print(f"====>Number of TRA Absent Plan B = {len(tra_absent_plan_b)}")

    else:
        print("!!!!!!!!!!!!!!!  Wrong  !!!!!!!!!!!!!!!!")
# ------------------------------------------------------#

elif select_area == "ML3":
    print("Main Line PK11-PK05")
    line1()

    area()

    if select_plan == "A":
        tra_under_test_plan_a = tra_under_test - plan_a_ml_3
        tra_absent_plan_a = tra_under_test_plan_a - tra_present

        print(f"====>\"OFF TRA\" Redundancy Plan A = {sorted(plan_a_ml_3)}")
        print(f"====>Number of \"OFF TRA\" Redundancy Plan A = {len(plan_a_ml_3)}")
        line1()
        tra_under_test_plan_a = tra_under_test.difference(plan_a_ml_3)
        print(f"====>\"ON TRA\" Redundancy Under Test Plan A = {sorted(tra_under_test_plan_a)}")
        print(f"====>Number of \"ON TRA\" Redundancy Under Test Plan A = {len(tra_under_test_plan_a)}")
        line1()
        print(f"====>TRA absent_plan_a={sorted(tra_absent_plan_a)}")
        print(f"====>Number of TRA Absent Plan A = {len(tra_absent_plan_a)}")
        line1()

    elif select_plan == "B":
        tra_under_test_plan_b = tra_under_test - plan_b_ml_3
        tra_absent_plan_b = tra_under_test_plan_b - tra_present

        print(f"====>\"OFF TRA\" Redundancy Plan B = {sorted(plan_b_ml_3)}")
        print(f"====>Number of \"OFF TRA\" Redundancy Plan B = {len(plan_b_ml_3)}")
        line1()
        tra_under_test_plan_b = tra_under_test.difference(plan_b_ml_3)
        print(f"====>\"ON TRA\" Redundancy Under Test Plan B = {sorted(tra_under_test_plan_b)}")
        print(f"====>Number of \"ON TRA\" Redundancy Under Test Plan B = {len(tra_under_test_plan_b)}")
        line1()
        print(f"====>TRA absent_plan_b={sorted(tra_absent_plan_b)}")
        print(f"====>Number of TRA Absent Plan B = {len(tra_absent_plan_b)}")

    else:
        print("!!!!!!!!!!!!!!!  Wrong  !!!!!!!!!!!!!!!!")
# ------------------------------------------------------#
elif select_area == "ML4":
    print("Main Line PK04-PK01")
    line1()

    area()

    if select_plan == "A":
        tra_under_test_plan_a = tra_under_test - plan_a_ml_4
        tra_absent_plan_a = tra_under_test_plan_a - tra_present

        print(f"====>\"OFF TRA\" Redundancy Plan A = {sorted(plan_a_ml_4)}")
        print(f"====>Number of \"OFF TRA\" Redundancy Plan A = {len(plan_a_ml_4)}")
        line1()
        tra_under_test_plan_a = tra_under_test.difference(plan_a_ml_4)
        print(f"====>\"ON TRA\" Redundancy Under Test Plan A = {sorted(tra_under_test_plan_a)}")
        print(f"====>Number of \"ON TRA\" Redundancy Under Test Plan A = {len(tra_under_test_plan_a)}")
        line1()
        print(f"====>TRA absent_plan_a={sorted(tra_absent_plan_a)}")
        print(f"====>Number of TRA Absent Plan A = {len(tra_absent_plan_a)}")
        line1()

    elif select_plan == "B":
        tra_under_test_plan_b = tra_under_test - plan_b_ml_4
        tra_absent_plan_b = tra_under_test_plan_b - tra_present

        print(f"====>\"OFF TRA\" Redundancy Plan B = {sorted(plan_b_ml_4)}")
        print(f"====>Number of \"OFF TRA\" Redundancy Plan B = {len(plan_b_ml_4)}")
        line1()
        tra_under_test_plan_b = tra_under_test.difference(plan_b_ml_4)
        print(f"====>\"ON TRA\" Redundancy Under Test Plan B = {sorted(tra_under_test_plan_b)}")
        print(f"====>Number of \"ON TRA\" Redundancy Under Test Plan B = {len(tra_under_test_plan_b)}")
        line1()
        print(f"====>TRA absent_plan_b={sorted(tra_absent_plan_b)}")
        print(f"====>Number of TRA Absent Plan B = {len(tra_absent_plan_b)}")

    else:
        print("!!!!!!!!!!!!!!!  Wrong  !!!!!!!!!!!!!!!!")
# ------------------------------------------------------#

else:
    print("!!!!!!!!!!!!!!!  Wrong  !!!!!!!!!!!!!!!!")

#End