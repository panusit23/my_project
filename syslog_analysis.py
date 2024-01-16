# Syslog Analysis.
# Find Max RSSI (Received Signal Strength Indicator),
# Find TRA Roaming,
# Find Ping-Pong Occurrence.
# Export to .xlsx

import warnings
import pandas as pd

warnings.filterwarnings("ignore")

line1 = lambda: print("_"*54)
    
#---------------------------------------------------#    

train_no = {
        
"ym10 ": {"a":"xx:xx:xx:xx:xx:xx", "b":"xx:xx:xx:xx:xx:xx"},

"ym11": {"a":"xx:xx:xx:xx:xx:xx", "b":"xx:xx:xx:xx:xx:xx"},

"ym15": {"a":"xx:xx:xx:xx:xx:xx", "b":"xx:xx:xx:xx:xx:xx0"},

#----------------------------------------------

"pm28": {"a":"xx:xx:xx:xx:xx:xx", "b":"xx:xx:xx:xx:xx:xx"},
    
"pm30": {"a":"xx:xx:xx:xx:xx:xx", "b":"xx:xx:xx:xx:xx:xx"},
    
"pm35": {"a":"xx:xx:xx:xx:xx:xx", "b":"xx:xx:xx:xx:xx:xx"}
    
}

print("Please Enter Train Number: [ex. ym01]")
train_key = str(input("Train Number = "))
mdr_mac_a = train_no[train_key]["a"]
mdr_mac_b = train_no[train_key]["b"]

print(f'MDR Cab A MAC = {mdr_mac_a}')
print(f'MDR Cab B MAC = {mdr_mac_b}')
line1()

print("Calculating...")
line1()

cols = ['Status','Order','MDR','TRA From','TRA To','RSSI Roam','Handoff Roam','Channel','Roaming Time']

try:
    df = pd.read_csv('syslog_combine.csv', names = cols)
    print(f"Read All Lines From CSV = {len(df)}")
    line1()

except FileNotFoundError:
    print(f"!!!!! File Not Found !!!!!")
    
    
#Cab A, B
df_mdr_a = df[df.MDR == mdr_mac_a]
print(f"Read Lines from CSV Only Cab A = {len(df_mdr_a)}")
df_mdr_b = df[df.MDR == mdr_mac_b]
print(f"Read Lines from CSV Only Cab B = {len(df_mdr_b)}")
line1()

#Filter Handoff Cab A, B
df_mdr_handoff_a = df_mdr_a[df_mdr_a.Status == 'Handoff']
print(f"MDR Handoff Cab A = {len(df_mdr_handoff_a)}")
df_mdr_handoff_b = df_mdr_b[df_mdr_b.Status == 'Handoff']
print(f"MDR Handoff Cab B = {len(df_mdr_handoff_b)}")
line1()

#str to int (Handoff)
df_mdr_handoff_a["Order"] = df_mdr_handoff_a["Order"].astype(int)
df_mdr_handoff_b["Order"] = df_mdr_handoff_b["Order"].astype(int)

#Filter RSSI Cab A, B
df_mdr_rssi_a = df_mdr_a[df_mdr_a.Status == 'RSSI']
print(f"MDR RSSI Cab A = {len(df_mdr_rssi_a)}")
df_mdr_rssi_b = df_mdr_b[df_mdr_b.Status == 'RSSI']
print(f"MDR RSSI Cab B = {len(df_mdr_rssi_b)}")
line1()

#str to int (RSSI)
df_mdr_rssi_a["TRA To"] = df_mdr_rssi_a["TRA To"].astype(int)
df_mdr_rssi_a["RSSI Roam"] = df_mdr_rssi_a["RSSI Roam"].astype(int)
df_mdr_rssi_b["TRA To"] = df_mdr_rssi_b["TRA To"].astype(int)
df_mdr_rssi_b["RSSI Roam"] = df_mdr_rssi_b["RSSI Roam"].astype(int)

#Sum RSSI Max Cab A, B
df_mdr_rssi_a['Max Strength'] = df_mdr_rssi_a['TRA To'] + df_mdr_rssi_a['RSSI Roam']
df_mdr_rssi_b['Max Strength'] = df_mdr_rssi_b['TRA To'] + df_mdr_rssi_b['RSSI Roam']

#Find TRA Max Strength Cab A, B
max_a = df_mdr_rssi_a.groupby(["TRA From"])["Max Strength"].transform(max)==df_mdr_rssi_a["Max Strength"]
print(f"RSSI Max Strength for Cab A = {len(df_mdr_rssi_a[max_a])}")
df_mdr_rssi_max_a = df_mdr_rssi_a[max_a]
max_b = df_mdr_rssi_b.groupby(["TRA From"])["Max Strength"].transform(max)==df_mdr_rssi_b["Max Strength"]
print(f"RSSI Max Strength for Cab B = {len(df_mdr_rssi_b[max_b])}")
df_mdr_rssi_max_b = df_mdr_rssi_b[max_b]
line1()

#Find TRA Roaming Cab A
roam_a = df_mdr_rssi_a.groupby(["TRA From"])["RSSI Roam"].transform(max)==df_mdr_rssi_a["RSSI Roam"]
print(f"RSSI Roam Strength for Cab A = {len(df_mdr_rssi_a[roam_a])}")
df_mdr_rssi_roam_a = df_mdr_rssi_a[roam_a]
#TRA Roaming Cab A (Remove Duplicate)
df_mdr_rssi_roam_rm_dup_a = df_mdr_rssi_roam_a.drop_duplicates("TRA From")
print(f"RSSI Roam Strength for Cab A (Remaining TRA After Removing Duplicate) = {len(df_mdr_rssi_roam_rm_dup_a)}")

#Find TRA Roaming Cab B
roam_b = df_mdr_rssi_b.groupby(["TRA From"])["RSSI Roam"].transform(max)==df_mdr_rssi_b["RSSI Roam"]
print(f"RSSI Roam Strength for Cab B = {len(df_mdr_rssi_b[roam_b])}")
df_mdr_rssi_roam_b = df_mdr_rssi_b[roam_b]
#TRA Roaming Cab B (Remove Duplicate)
df_mdr_rssi_roam_rm_dup_b = df_mdr_rssi_roam_b.drop_duplicates("TRA From")
print(f"RSSI Roam Strength for Cab B (Remaining TRA After Removing Duplicate) = {len(df_mdr_rssi_roam_rm_dup_b)}")
line1()

#Merge TRA Max Strength Cab A, B (1)
df_concat_max_a_b = pd.concat([df_mdr_rssi_max_a, df_mdr_rssi_max_b], axis=0, ignore_index=False, sort=False)
print(f"TRA MAX Concat Cab A, B = {len(df_concat_max_a_b)}")
line1()

#Merge Handoff Cab A, B to get Handoff Roaming (2)
df_concat_handoff_roam_a_b = pd.concat([df_mdr_handoff_a, df_mdr_handoff_b], axis=0, ignore_index=False, sort=False)
print(f"TRA Handoff Roam Concat Cab A, B = {len(df_concat_handoff_roam_a_b)}")
line1()

#Merge RSSI Roam Remove Duplicate TRA Cab A, B to Get RSSI Roaming (3)
df_concat_rssi_roam_a_b = pd.concat([df_mdr_rssi_roam_rm_dup_a, df_mdr_rssi_roam_rm_dup_b], axis=0, ignore_index=False, sort=False)
print(f"TRA RSSI Roam Concat Cab A, B (Remaining TRA After Removing Duplicate) = {len(df_concat_rssi_roam_a_b)}")
line1()

#Merge (1)+(2)
df_concat_max_handoff_roam_a_b = pd.concat([df_concat_max_a_b, df_concat_handoff_roam_a_b], axis=0, ignore_index=False, sort=False)
print(f"TRA Concat RSSI and Handoff for Cab A, B = {len(df_concat_max_handoff_roam_a_b)}")
df_concat_max_handoff_roam_a_b["Order"] = df_concat_max_handoff_roam_a_b["Order"].astype(int)
df_concat_max_handoff_roam_a_b_sort = df_concat_max_handoff_roam_a_b.sort_values('Order')
handoff_roam_a_b_rm_cols = df_concat_max_handoff_roam_a_b_sort[['Status','Order','MDR','TRA From','TRA To','RSSI Roam','Handoff Roam','Roaming Time','Max Strength']]
line1()

#Pivot to Find Each Max Value
pvt_tra_from_max = df_concat_max_a_b.pivot_table(index=['TRA From'], values = ['Max Strength'], aggfunc = ['max'])
pvt_tra_to_handoff_roam = df_concat_handoff_roam_a_b.pivot_table(index=['TRA To'], values = ['Handoff Roam'], aggfunc = ['max'])
pvt_tra_to_rssi_roam = df_concat_rssi_roam_a_b.pivot_table(index=['TRA From'], values = ['RSSI Roam'], aggfunc = ['max'])

#Pivot to find each Max Value for seperate value.
pvt_tra_from_max_only_a = df_mdr_rssi_max_a.pivot_table(index=['TRA From'], values = ['Max Strength'], aggfunc = ['max'])
pvt_tra_from_max_only_b = df_mdr_rssi_max_b.pivot_table(index=['TRA From'], values = ['Max Strength'], aggfunc = ['max'])

#Final Pivot to merge all.
pvt_tra_concat_a_b_record = pd.concat([pvt_tra_from_max, pvt_tra_to_handoff_roam, pvt_tra_to_rssi_roam], axis=1, ignore_index=False, sort=False)

#For Pingpong
pingpong_a = df_mdr_handoff_a
pingpong_a_sort = pingpong_a.sort_values('Order')
pingpong_a_sort_rm_cols = pingpong_a_sort[['Order','MDR','TRA From','TRA To','Roaming Time']]
pingpong_b = df_mdr_handoff_b
pingpong_b_sort = pingpong_b.sort_values('Order')
pingpong_b_sort_rm_cols = pingpong_b_sort[['Order','MDR','TRA From','TRA To','Roaming Time']]

syslog_analyze = pd.ExcelWriter('Syslog Analyze.xlsx')

pvt_tra_concat_a_b_record.to_excel(syslog_analyze, sheet_name = 'For Pre-Analyze')
pingpong_b_sort_rm_cols.to_excel(syslog_analyze, sheet_name = 'Cab B Pingpong', index = False)
pingpong_a_sort_rm_cols.to_excel(syslog_analyze, sheet_name = 'Cab A Pingpong', index = False)

pvt_tra_from_max.to_excel(syslog_analyze, sheet_name = 'TRA From MAX')
pvt_tra_to_handoff_roam.to_excel(syslog_analyze, sheet_name = 'TRA To Handoff Roam')
pvt_tra_to_rssi_roam.to_excel(syslog_analyze, sheet_name = 'TRA To RSSI Roam')

pvt_tra_from_max_only_b.to_excel(syslog_analyze, sheet_name = 'TRA From MAX Cab B')
pvt_tra_from_max_only_a.to_excel(syslog_analyze, sheet_name = 'TRA From MAX Cab A')

handoff_roam_a_b_rm_cols.to_excel(syslog_analyze, sheet_name = 'Cab A+B')

syslog_analyze.save()
#syslog_analyze.close()

print("Done!! Created Files Complete!!")   
    
#End    
    