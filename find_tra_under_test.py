# 819 TRA in Area Under Test

line1 = lambda: print("_"*54)

#see routing doc
tra_under_test = [

9114, 9117, 9125, 9129, 9134, 9141 
    
]

#------------------------------------------------------#

#see from analyze
tra_present = [

9117, 9125, 9129, 9141

]              

print("For 818")
line1()

print(f"TRA in Area Under Test={sorted(tra_under_test)}")
print(f"Number of TRA Area Under Test = {len(tra_under_test)}")
line1()

print(f"TRA_present={sorted(tra_present)}")
print(f"Number of TRA Present = {len(tra_present)}")
line1()

tra_under_test = set(list(tra_under_test))
tra_present = set(list(tra_present))
tra_not_present = tra_under_test.difference(tra_present)

print(f"TRA_absent={sorted(tra_not_present)}")
print(f"Number of TRA Absent = {len(tra_not_present)}")

#End