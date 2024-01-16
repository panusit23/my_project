# Sum Bandwidth Value in Seperate Files
# Cab B Average the Same TRA, 
# Cab A Average the Same TRA 
# Then Combine

import warnings
import pandas as pd

warnings.filterwarnings("ignore")
#------------------------------------------------------#  
def line1():
    print("_"*54)
#------------------------------------------------------#    

def read_csv_a():
    df_bw_a = pd.read_csv('bw_a.txt', names = name_a, usecols=cols_bw, skiprows=[0, 1, 2])
    df_bw_a["Min Cab A"] = df_bw_a["Min Cab A"].fillna(0)
    df_bw_a["Average Cab A"] = df_bw_a["Average Cab A"].fillna(0)
    print(f"Bandwidth Cab A = {len(df_bw_a)}")
    return df_bw_a

def read_csv_b():
    df_bw_b = pd.read_csv('bw_b.txt', names = name_b, usecols=cols_bw, skiprows=[0, 1, 2])
    df_bw_b["Min Cab B"] = df_bw_b["Min Cab B"].fillna(0)
    df_bw_b["Average Cab B"] = df_bw_b["Average Cab B"].fillna(0)
    print(f"Bandwidth Cab B = {len(df_bw_b)}")
    return df_bw_b

def read_csv_a2():
    df_bw_a2 = pd.read_csv('bw_a2.txt', names = name_a, usecols=cols_bw, skiprows=[0, 1, 2])
    df_bw_a2["Min Cab A"] = df_bw_a2["Min Cab A"].fillna(0)
    df_bw_a2["Average Cab A"] = df_bw_a2["Average Cab A"].fillna(0) 
    print(f"Bandwidth Cab A2 = {len(df_bw_a2)}")  
    return df_bw_a2

def read_csv_a3():
    df_bw_a3 = pd.read_csv('bw_a3.txt', names = name_a, usecols=cols_bw, skiprows=[0, 1, 2])
    df_bw_a3["Min Cab A"] = df_bw_a3["Min Cab A"].fillna(0)
    df_bw_a3["Average Cab A"] = df_bw_a3["Average Cab A"].fillna(0)  
    print(f"Bandwidth Cab A3 = {len(df_bw_a3)}")  
    return df_bw_a3

def read_csv_b2(): 
    df_bw_b2 = pd.read_csv('bw_b2.txt', names = name_b, usecols=cols_bw, skiprows=[0, 1, 2])
    df_bw_b2["Min Cab B"] = df_bw_b2["Min Cab B"].fillna(0)
    df_bw_b2["Average Cab B"] = df_bw_b2["Average Cab B"].fillna(0)  
    print(f"Bandwidth Cab B2 = {len(df_bw_b2)}")
    return df_bw_b2

def read_csv_b3():
    df_bw_b3 = pd.read_csv('bw_b3.txt', names = name_b, usecols=cols_bw, skiprows=[0, 1, 2])
    df_bw_b3["Min Cab B"] = df_bw_b3["Min Cab B"].fillna(0)
    df_bw_b3["Average Cab B"] = df_bw_b3["Average Cab B"].fillna(0)   
    print(f"Bandwidth Cab B3 = {len(df_bw_b3)}")
    return df_bw_b3

#------------------------------------------------------#

def err():
    print("!!!!! File Not Found !!!!!")    
    
#------------------------------------------------------#
#Merge Same TRA of Cab A, B.
def merge_tra_a_a2():
    df_bw_concat_tra_a_a2 = pd.concat([df_bw_a, df_bw_a2], axis=0, ignore_index=False, sort=False)
    print(f"Merge Min and Average Cab A+A2 = {len(df_bw_concat_tra_a_a2)}")
    return df_bw_concat_tra_a_a2

def merge_tra_a_a2_a3():
    df_bw_concat_tra_a_a2_a3 = pd.concat([df_bw_a, df_bw_a2, df_bw_a3], axis=0, ignore_index=False, sort=False)
    print(f"Merge Min and Average Cab A+A2+A3 = {len(df_bw_concat_tra_a_a2_a3)}")
    return df_bw_concat_tra_a_a2_a3

def merge_tra_b_b2():
    df_bw_concat_tra_b_b2 = pd.concat([df_bw_b, df_bw_b2], axis=0, ignore_index=False, sort=False)
    print(f"Merge Min and Average Cab B+B2 = {len(df_bw_concat_tra_b_b2)}")
    return df_bw_concat_tra_b_b2

def merge_tra_b_b2_b3():
    df_bw_concat_tra_b_b2_b3 = pd.concat([df_bw_b, df_bw_b2, df_bw_b3], axis=0, ignore_index=False, sort=False)
    print(f"Merge Min and Average Cab B+B2+B3 = {len(df_bw_concat_tra_b_b2_b3)}") 
    return df_bw_concat_tra_b_b2_b3

#------------------------------------------------------#

# Average The Same TRA of Cab A and B
def mean_a():    
    df_bw_tra_avg_a = df_bw_a.groupby("TRA").mean()
    print(f"Average of Min and Average Cab A = {len(df_bw_tra_avg_a)}")
    return df_bw_tra_avg_a

def mean_b():    
    df_bw_tra_avg_b = df_bw_b.groupby("TRA").mean()
    print(f"Average of Min and Average Cab B = {len(df_bw_tra_avg_b)}")
    return df_bw_tra_avg_b

def mean_a_a2():
    df_bw_tra_avg_a = df_bw_concat_tra_a_a2.groupby("TRA").mean()
    print(f"Average of Min and Average Cab A = {len(df_bw_tra_avg_a)}")
    return df_bw_tra_avg_a
    
def mean_a_a2_a3(): 
    df_bw_tra_avg_a = df_bw_concat_tra_a_a2_a3.groupby("TRA").mean()
    print(f"Average of Min and Average Cab A = {len(df_bw_tra_avg_a)}")
    return df_bw_tra_avg_a
    
def mean_b_b2():
    df_bw_tra_avg_b = df_bw_concat_tra_b_b2.groupby("TRA").mean()
    print(f"Average of Min and Average Cab B = {len(df_bw_tra_avg_b)}")
    return df_bw_tra_avg_b
    
def mean_b_b2_b3():   
    df_bw_tra_avg_b = df_bw_concat_tra_b_b2_b3.groupby("TRA").mean()
    print(f"Average of Min and Average Cab B = {len(df_bw_tra_avg_b)}")  
    return df_bw_tra_avg_b

#------------------------------------------------------#

def merge_export(): 
    #Merge Same TRA of Cab A and B.
    df_bw_concat_tra_avg_a_b = pd.concat([df_bw_tra_avg_b, df_bw_tra_avg_a], axis=1, ignore_index=False, sort=False)
    print(f"Merge Min and Average Cab A, B = {len(df_bw_concat_tra_avg_a_b)}")
    line1()

    #Clean Data Both Cabs.
    df_bw_concat_tra_avg_a_b["Min Cab A"] = df_bw_concat_tra_avg_a_b["Min Cab A"].fillna(0)
    df_bw_concat_tra_avg_a_b["Average Cab A"] = df_bw_concat_tra_avg_a_b["Average Cab A"].fillna(0)
    df_bw_concat_tra_avg_a_b["Min Cab B"] = df_bw_concat_tra_avg_a_b["Min Cab B"].fillna(0)
    df_bw_concat_tra_avg_a_b["Average Cab B"] = df_bw_concat_tra_avg_a_b["Average Cab B"].fillna(0)

    #Sum Cab A and B and Create Column.
    df_bw_concat_tra_avg_a_b["Min Cab B + Cab A"] = df_bw_concat_tra_avg_a_b["Min Cab A"] + df_bw_concat_tra_avg_a_b["Min Cab B"]
    df_bw_concat_tra_avg_a_b["Average Cab B + Cab A"] = df_bw_concat_tra_avg_a_b["Average Cab A"] + df_bw_concat_tra_avg_a_b["Average Cab B"]
    print(f"Sum of Min Average Cab B+A = {len(df_bw_concat_tra_avg_a_b)}")
    line1()

    #Remove Column.
    df_bw_concat_tra_avg_a_b_rm_cols = df_bw_concat_tra_avg_a_b.drop(cols_bw_drop, axis=1)

    #Order TRA Number.
    df_bw_concat_tra_avg_a_b_record = df_bw_concat_tra_avg_a_b.sort_values("TRA")
    df_bw_concat_tra_avg_a_b_only = df_bw_concat_tra_avg_a_b_rm_cols.sort_values("TRA")

    bandwidth_file = pd.ExcelWriter('Bandwidth Avg Same TRA for Each Cab.xlsx')
    df_bw_concat_tra_avg_a_b_record.to_excel(bandwidth_file, sheet_name = 'BW for Record')
    df_bw_concat_tra_avg_a_b_only.to_excel(bandwidth_file, sheet_name = 'BW Only A+B')
    bandwidth_file.save()

    print("Done!! Created Files Complete!!") 
    
#------------------------------------------------------#

cols_bw = [0, 13, 15]
name_a = ["TRA", "Min Cab A","Average Cab A"]
name_b = ["TRA", "Min Cab B","Average Cab B"]
cols_bw_drop = ["Min Cab A","Average Cab A","Min Cab B","Average Cab B"]

print("How many bandwidth files do you have?\nExample:")
print("=>bw_a = 1\n=>bw_b, bw_b2, bw_b3 = 3")
print("------------------------------------------------------")
multiple_files_a = str(input("Banwidth Cab A File = "))
multiple_files_b = str(input("Banwidth Cab B File = "))
line1()        

#------------------------------------------------------#

if multiple_files_a == "1" and multiple_files_b == "1":
    try:                
        df_bw_a = read_csv_a()
        df_bw_b = read_csv_b()
        line1()
    except FileNotFoundError:
        err()
    
    df_bw_tra_avg_a = mean_a()    
    df_bw_tra_avg_b = mean_b()
    line1()    
    
    merge_export()   
    
#------------------------------------------------------# 

elif multiple_files_a == "1" and multiple_files_b == "2":        
    try:
        df_bw_a = read_csv_a()
        df_bw_b = read_csv_b()
        df_bw_b2 = read_csv_b2()
        line1()
    except FileNotFoundError:
        err()
    
    df_bw_concat_tra_b_b2 = merge_tra_b_b2()
    line1()
    
    df_bw_tra_avg_a = mean_a()       
    df_bw_tra_avg_b = mean_b_b2()
    line1()
    
    merge_export()  
    
#------------------------------------------------------# 

elif multiple_files_a == "1" and multiple_files_b == "3":    
    try:
        df_bw_a = read_csv_a()
        df_bw_b = read_csv_b()
        df_bw_b2 = read_csv_b2()
        df_bw_b3 = read_csv_b3()
        line1()
    except FileNotFoundError:
        err()        
 
    df_bw_concat_tra_b_b2_b3 = merge_tra_b_b2_b3()
    line1()
    
    df_bw_tra_avg_a = mean_a()    
    df_bw_tra_avg_b = mean_b_b2_b3()
    line1()
    
    merge_export()    
    
#------------------------------------------------------#   

elif multiple_files_a == "2" and multiple_files_b == "1":   
    try:
        df_bw_a = read_csv_a()
        df_bw_b = read_csv_b()
        df_bw_a2 = read_csv_a2()
        line1()
    except FileNotFoundError:
        err()
    
    df_bw_concat_tra_a_a2 = merge_tra_a_a2()
    line1()
    
    df_bw_tra_avg_a = mean_a_a2()
    df_bw_tra_avg_b = mean_b()
    line1()
    
    merge_export()    
    
#------------------------------------------------------#

elif multiple_files_a == "2" and multiple_files_b == "2":    
    try:
        df_bw_a = read_csv_a()
        df_bw_a2 = read_csv_a2()
        df_bw_b = read_csv_b()     
        df_bw_b2 = read_csv_b2()
        line1()
    except FileNotFoundError:
        err()

    df_bw_concat_tra_a_a2 = merge_tra_a_a2()
    df_bw_concat_tra_b_b2 = merge_tra_b_b2()
    line1()
    
    df_bw_tra_avg_a = mean_a_a2()
    df_bw_tra_avg_b = mean_b_b2()
    line1()
    
    merge_export()
    
#------------------------------------------------------#

elif multiple_files_a == "2" and multiple_files_b == "3" :    
    try: 
        df_bw_a = read_csv_a()  
        df_bw_a2 = read_csv_a2()
        df_bw_b = read_csv_b()
        df_bw_b2 = read_csv_b2()
        df_bw_b3 = read_csv_b3()
        line1()
    except FileNotFoundError:
        err()
    
    df_bw_concat_tra_a_a2 = merge_tra_a_a2()
    df_bw_concat_tra_b_b2_b3 = merge_tra_b_b2_b3()
    line1()
    
    df_bw_tra_avg_a = mean_a_a2()
    df_bw_tra_avg_b = mean_b_b2_b3()
    line1() 
    
    merge_export()   
    
#------------------------------------------------------#

elif multiple_files_a == "3" and multiple_files_b == "1":    
    try:
        df_bw_a = read_csv_a()
        df_bw_a2 = read_csv_a2()
        df_bw_a3 = read_csv_a3()
        df_bw_b = read_csv_b()  
        line1()
    except FileNotFoundError:
        err()
        
    df_bw_concat_tra_a_a2_a3 = merge_tra_a_a2_a3()
    line1() 
    
    df_bw_tra_avg_a = mean_a_a2_a3()
    df_bw_tra_avg_b = mean_b()
    line1()   
    
    merge_export()           
    
#------------------------------------------------------#  

elif multiple_files_a == "3" and multiple_files_b == "2":  
    try:
        df_bw_a = read_csv_a()
        df_bw_a2 = read_csv_a2()
        df_bw_a3 = read_csv_a3()
        df_bw_b = read_csv_b()
        df_bw_b2 = read_csv_b2()
        line1()
    except FileNotFoundError:
        err()

    df_bw_concat_tra_a_a2_a3 = merge_tra_a_a2_a3()
    df_bw_concat_tra_b_b2 = merge_tra_b_b2()
    line1()
    
    df_bw_tra_avg_a = mean_a_a2_a3()
    df_bw_tra_avg_b = mean_b_b2()
    line1()  
    
    merge_export()  
    
#------------------------------------------------------#

elif multiple_files_a == "3" and multiple_files_b == "3":
    try:
        df_bw_a = read_csv_a()        
        df_bw_a2 = read_csv_a2()
        df_bw_a3 = read_csv_a3()
        df_bw_b = read_csv_b()
        df_bw_b2 = read_csv_b2()
        df_bw_b3 = read_csv_b3()
        line1()
    except FileNotFoundError:
        err()

    df_bw_concat_tra_a_a2_a3 = merge_tra_a_a2_a3()
    df_bw_concat_tra_b_b2_b3 = merge_tra_b_b2_b3()
    line1()
    
    df_bw_tra_avg_a = mean_a_a2_a3()
    df_bw_tra_avg_b = mean_b_b2_b3()
    line1()    
    
    merge_export()    
    
#------------------------------------------------------#

else: print("Too much files, This test should be failed")
    
#End