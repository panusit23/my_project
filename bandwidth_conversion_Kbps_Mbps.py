# Bandwidth Summary for record in the test report
# Kbps to Mbps Conversion

line1 = lambda: print("_"*54)

#-------------------------------#

bw_min_b = {
  
9113 : 0,
9117 : 11.75,
9125 : 3340,
   
}

#------------------------------------------------------#

bw_avg_b= {

9113 : 0,
9117 : 1559.695,
9125 : 8150,
   
}

#------------------------------------------------------#

bw_min_a = {
    
9113 : 3.86666666666667,
9117 : 132.2,
9125 : 209,
    
}

#------------------------------------------------------#

bw_avg_a = {
  
9113 : 777.763333333333,
9117 : 773.686666666667,
9125 : 977.13,
    
}

#------------------------------------------------------#

bw_min_b_a = {
  

9113 : 3.86666666666667,
9117 : 143.95,
9125 : 3549,
    
}

#------------------------------------------------------#

bw_avg_b_a = {
    

9113 : 777.763333333333,
9117 : 2333.38166666667,
9125 : 9127.13,
    
}

#------------------------------------------------------#

#BW Min Cab B

print("Mininum Bandwidth\n")

print("pc2_min={", end = "")
g=0
for value1 in bw_min_b:
    print(f"TRA{value1}:{round(bw_min_b[value1]/1000, 3)}M,", end = " ")
    g+=1
print("}")
print(f"//Number of All BW Min Cab B= {g}")
line1()

#------------------------------------------------------#

#BW Min Cab A

print("pc3_min={", end = "")
i=0
for value3 in bw_min_a:
    print(f"TRA{value3}:{round(bw_min_a[value3]/1000, 3)}M,", end = " ")
    i+=1
print("}")
print(f"//Number of All BW Average Cab A = {i}")
line1()

#------------------------------------------------------#

#BW Min Cab B+A

print("sum_min={", end = "")
k=0
for value5 in bw_min_b_a:
    print(f"TRA{value5}:{round(bw_min_b_a[value5]/1000, 3)}M,", end = " ")
    k+=1
print("}")
print(f"//Number of All BW Min Cab B+A = {k}")
line1()

#------------------------------------------------------#

#BW Min Cab B+A < 30Mbps

print("sum_min<30={", end = "")
m=0
for value7 in bw_min_b_a:
    if bw_min_b_a[value7] < 30000:  
        print(f"TRA{value7}:{round(bw_min_b_a[value7]/1000, 3)}M,", end = " ")
        m+=1
print("}")        
print(f"//Number of BW Min Cab B+A < 30Mbps = {m}")
line1()
line1()
line1()
#------------------------------------------------------#


#BW Avg Cab B

print("Average Bandwidth\n")

print("pc2_avg={", end = "")
h=0
for value2 in bw_avg_b:
    print(f"TRA{value2}:{round(bw_avg_b[value2]/1000, 3)}M,", end = " ")
    h+=1
print("}")
print(f"//Number of All BW Average Cab B = {h}")
line1()

#------------------------------------------------------#

#BW Avg Cab A

print("pc3_avg={", end = "")
j=0
for value4 in bw_avg_a:
    print(f"TRA{value4}:{round(bw_avg_a[value4]/1000, 3)}M,", end = " ")
    j+=1
print("}")
print(f"//Number of All BW Average Cab A = {j}")
line1()

#------------------------------------------------------#

#BW avg Cab B+A

print("sum_avg={", end = "")
l=0
for value6 in bw_avg_b_a: 
    print(f"TRA{value6}:{round(bw_avg_b_a[value6]/1000, 3)}M,", end = " ")
    l+=1
print("}")    
print(f"//Number of All BW Min Cab B+A = {l}")
line1()

#------------------------------------------------------#

#BW Min Cab B+A < 60Mbps

print("sum_avg<60={", end = "")
n=0
for value8 in bw_avg_b_a:
    if bw_avg_b_a[value8] < 60000:  
        print(f"TRA{value8}:{round(bw_avg_b_a[value8]/1000, 3)}M,", end = " ")
        n+=1
print("}")        
print(f"Number of BW Avg Cab B+A < 60Mbps = {n}")
line1()

#end