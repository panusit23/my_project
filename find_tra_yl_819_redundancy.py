# Yellow 819 TRA in Area Under Test
# Redundancy Plan A and B

line1 = lambda: print("_"*54)
line3 = lambda: print("="*54)

#see routing doc
tra_under_test = {

9114, 9117, 9125, 9129, 9134, 9141

}

#------------------------------------------------------#

#see from analyze
tra_present = {

9114, 9117, 9125, 9129, 9134, 9141



}             

#------------------------------------------------------#

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

#=======================================================
# YL Depot TRA Down
#=======================================================
# Track B, C2, C3, Stabling Yard

plan_a_s = {1606, 9102, 9133, 9134, 9137, 9125, 9101, 9113, 9117}

plan_b_s = {9105, 9109, 9126, 9129, 9130, 9106, 9138, 9141, 9142, 9121, 9114, 1609}

#------------------------------------------------------#

# Track B, C2, C3, Mainworkshop

plan_a_m = {9101, 9113, 9117}

plan_b_m = {9118, 9122, 9110, 9121, 9114, 1609}

#------------------------------------------------------#

# Ramp A, Track B, C2, C3

plan_a_a = {9105, 9109, 9126, 9129, 9130}

plan_b_a = {9101, 9113, 9117, 9106, 9138, 9141, 9142}

#------------------------------------------------------#

# Ramp B, Track B, C2, C3

plan_a_b = {1606, 9102, 9133, 9134, 9137, 9125}

plan_b_b = {9101, 9113, 9117}

#------------------------------------------------------#

# Ramp C, Track B, C2, C3

plan_a_c = {9105, 9109, 9126, 9129, 9130}

plan_b_c = {9101, 9113, 9117, 9118, 9122, 9110}

#------------------------------------------------------#

# Mainline YL01 - YL23

plan_a_ml = {
             102, 114, 210, 309, 402, 505, 602, 705, 802, 814, 910, 1009, 
             106, 202, 301, 313, 406, 509, 606, 709, 806, 902, 1001, 1013, 
             110, 206, 305, 317, 501, 513, 701, 713, 810, 906, 1005, 1017,
             1101, 1109, 1201, 1209, 1217, 
             1105, 1113, 1205, 1213,
             1302, 1306, 1310, 1402, 1406, 1410, 1502, 1506, 1510, 1514, 1601, 1605,
             1609, 
             1702, 1714, 1809, 1905, 2002, 2014, 2110, 2205, 2217,
             1706, 1801, 1813, 1909, 2006, 2102, 2114, 2209,
             1710, 1805, 1901, 1913, 2010, 2106, 2201, 2213           

}

plan_b_ml = {
              101, 113, 209, 306, 401, 502, 601, 702, 801, 813, 909, 1006, 1018,
              105, 201, 213, 310, 405, 506, 605, 706, 805, 901, 913, 1010,
              109, 205, 302, 314, 409, 510, 609, 710, 809, 905, 1002, 1014,
              1102, 1110, 1202, 1210,
              1106, 1114, 1206, 1214,
              1606,
              1301, 1305, 1309, 1401, 1405, 1409, 1501, 1505, 1509, 1513, 1517, 1602,
              1701, 1713, 1806, 1902, 2001, 2013, 2109, 2202, 2214,
              1705, 1717, 1810, 1906, 2005, 2101, 2113, 2206, 2301,
              1709, 1802, 1814, 1910, 2009, 2105, 2117, 2210
    
}

#=======================================================

print("For 819 YL")
line3()
print("**************************************************")
print("Depot Area")
print("Type: \"M\" ==> Track B, Track C2, Track C3 to Main Workshop M1, M2, M3, M4, M5, and M6.")
print("Type: \"S\" ==> Track B, Track C2, Track C3 to Stabling S1, S2, S3, S4, S5, S6, S7, S8, S9, and TT.")
print("Type: \"A\" ==> Ramp A to Track B, Track C2, Track C3.")
print("Type: \"B\" ==> Ramp B to Track B, Track C2, Track C3.")
print("Type: \"C\" ==> Ramp C to Track B, Track C2, Track C3.")
print("\n")
print("Main Line Area")
print("Type: \"ML\" ==> Main Line YL01 - YL23")
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
    print("Track B, Track C2, Track C3 to Main Workshop M1, M2, M3, M4, M5, and M6.")
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
        line1()
    
    else: print("!!!!!!!!!!!!!!!  Wrong  !!!!!!!!!!!!!!!!")

#------------------------------------------------------#    

elif select_area == "S":  
    print("Track B, Track C2, Track C3 to Stabling S1, S2, S3, S4, S5, S6, S7, S8, S9, and TT.")
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
                
    else: print("!!!!!!!!!!!!!!!  Wrong  !!!!!!!!!!!!!!!!")

#------------------------------------------------------#    

elif select_area == "A":  
    print("Ramp A to Track B, Track C2, Track C3.")
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
                
    else: print("!!!!!!!!!!!!!!!  Wrong  !!!!!!!!!!!!!!!!")

#------------------------------------------------------#    

elif select_area == "B":  
    print("Ramp B to Track B, Track C2, Track C3.")
    line1()

    area()
    
    if select_plan == "A":       
        tra_under_test_plan_a = tra_under_test - plan_a_b           
        tra_absent_plan_a = tra_under_test_plan_a - tra_present
            
        print(f"====>\"OFF TRA\" Redundancy_plan_a={sorted(plan_a_b)}")
        print(f"====>Number of \"OFF TRA\" Redundancy Plan A = {len(plan_a_b)}")
        line1()                          
        print(f"====>\"ON TRA\" Redundancy Under Test_plan_a={sorted(tra_under_test_plan_a)}")
        print(f"====>Number of \"ON TRA\" Redundancy Under Test Plan A = {len(tra_under_test_plan_a)}")
        line1()            
        print(f"====>TRA absent_plan_a={sorted(tra_absent_plan_a)}")
        print(f"====>Number of TRA Absent Plan A = {len(tra_absent_plan_a)}")
        line1() 
                
    elif select_plan == "B":
        tra_under_test_plan_b = tra_under_test - plan_b_b          
        tra_absent_plan_b = tra_under_test_plan_b - tra_present
            
        print(f"====>\"OFF TRA\" Redundancy_plan_b={sorted(plan_b_b)}")
        print(f"====>Number of \"OFF TRA\" Redundancy Plan B = {len(plan_b_b)}")
        line1()                          
        print(f"====>\"ON TRA\" Redundancy Under Test_plan_b={sorted(tra_under_test_plan_b)}")
        print(f"====>Number of \"ON TRA\" Redundancy Under Test Plan B = {len(tra_under_test_plan_b)}")
        line1()            
        print(f"====>TRA absent_plan_b={sorted(tra_absent_plan_b)}")
        print(f"====>Number of TRA Absent Plan B = {len(tra_absent_plan_b)}")
                
    else: print("!!!!!!!!!!!!!!!  Wrong  !!!!!!!!!!!!!!!!")

#------------------------------------------------------#    

elif select_area == "C":  
    print("Ramp C to Track B, Track C2, Track C3.")
    line1()

    area()
    
    if select_plan == "A":
        tra_under_test_plan_a = tra_under_test - plan_a_c          
        tra_absent_plan_a = tra_under_test_plan_a - tra_present
            
        print(f"====>\"OFF TRA\" Redundancy_plan_a={sorted(plan_a_c)}")
        print(f"====>Number of \"OFF TRA\" Redundancy Plan A = {len(plan_a_c)}")
        line1()                          
        print(f"====>\"ON TRA\" Redundancy Under Test_plan_a={sorted(tra_under_test_plan_a)}")
        print(f"====>Number of \"ON TRA\" Redundancy Under Test Plan A = {len(tra_under_test_plan_a)}")
        line1()            
        print(f"====>TRA absent_plan_a={sorted(tra_absent_plan_a)}")
        print(f"====>Number of TRA Absent Plan A = {len(tra_absent_plan_a)}")
        line1()     
       
    elif select_plan == "B":
        tra_under_test_plan_b = tra_under_test - plan_b_c         
        tra_absent_plan_b = tra_under_test_plan_b - tra_present
            
        print(f"====>\"OFF TRA\" Redundancy_plan_b={sorted(plan_b_c)}")
        print(f"====>Number of \"OFF TRA\" Redundancy Plan B = {len(plan_b_c)}")
        line1()                          
        print(f"====>\"ON TRA\" Redundancy Under Test_plan_b={sorted(tra_under_test_plan_b)}")
        print(f"====>Number of \"ON TRA\" Redundancy Under Test Plan B = {len(tra_under_test_plan_b)}")
        line1()            
        print(f"====>TRA absent_plan_b={sorted(tra_absent_plan_b)}")
        print(f"====>Number of TRA Absent Plan B = {len(tra_absent_plan_b)}")
        
    else: print("!!!!!!!!!!!!!!!  Wrong  !!!!!!!!!!!!!!!!")

#------------------------------------------------------#  

elif select_area == "ML":  
    print("Main Line YL01 - YL23")
    line1()

    area()
    
    if select_plan == "A": 
        tra_under_test_plan_a = tra_under_test - plan_a_ml         
        tra_absent_plan_a = tra_under_test_plan_a - tra_present
            
        print(f"====>\"OFF TRA\" Redundancy_plan_a={sorted(plan_a_ml)}")
        print(f"====>Number of \"OFF TRA\" Redundancy Plan A = {len(plan_a_ml)}")
        line1()                          
        print(f"====>\"ON TRA\" Redundancy Under Test_plan_a={sorted(tra_under_test_plan_a)}")
        print(f"====>Number of \"ON TRA\" Redundancy Under Test Plan A = {len(tra_under_test_plan_a)}")
        line1()            
        print(f"====>TRA absent_plan_a={sorted(tra_absent_plan_a)}")
        print(f"====>Number of TRA Absent Plan A = {len(tra_absent_plan_a)}")
        line1() 
        
    elif select_plan == "B":      
        tra_under_test_plan_b = tra_under_test - plan_b_ml         
        tra_absent_plan_b = tra_under_test_plan_b - tra_present
            
        print(f"====>\"OFF TRA\" Redundancy_plan_b={sorted(plan_b_ml)}")
        print(f"====>Number of \"OFF TRA\" Redundancy Plan B = {len(plan_b_ml)}")
        line1()                          
        print(f"====>\"ON TRA\" Redundancy Under Test_plan_b={sorted(tra_under_test_plan_b)}")
        print(f"====>Number of \"ON TRA\" Redundancy Under Test Plan B = {len(tra_under_test_plan_b)}")
        line1()            
        print(f"====>TRA absent_plan_b={sorted(tra_absent_plan_b)}")
        print(f"====>Number of TRA Absent Plan B = {len(tra_absent_plan_b)}")
        
    else: print("!!!!!!!!!!!!!!!  Wrong  !!!!!!!!!!!!!!!!")

#------------------------------------------------------#
else: print("!!!!!!!!!!!!!!!  Wrong  !!!!!!!!!!!!!!!!")

#End