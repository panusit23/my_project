# Find RSSI Level 

line1 = lambda: print("_"*54)

#-------------------------------

max = {
 
9110:-78,
9118:-60,
9121:-61,
    
}
 
#------------------------------------------------------#

roam = {
 
9110:0,
9118:-72,
9121:-62, 
    
}

max_with_value = max
print(f"max={max_with_value}")
roam_with_value = roam
print(f"roam={roam_with_value}")
line1()

#------------------------------------------------------#

#if occurs, see on MRA graph 
f=0
for value in roam:
    if roam[value] >= max[value] and roam[value] != 0:
        print(f"{value} : {roam[value]}, ", end='')
        f+=1
        
print(f"Number of Roam >= Max = {f}")
line1()
#------------------------------------------------------#

#No Roaming TRA
g=0
print('Non Roaming With RSSI = {')
for value in roam:
    if roam[value] == 0:
        print(f"{value}:{max[value]}, ", end='')
        g+=1

print(f"\nNumber of Non Roaming TRA = {g}")
line1()
#------------------------------------------------------#

#TRA MAX < -55
a=0
for value in max:
    if max[value] < -55 and roam[value] != 0:  
        print(f"{value}:{max[value]}, ", end='')
        a+=1
        
print(f"Number of TRA <-55 = {a}")
line1()
#------------------------------------------------------#

#TRA MAX < -45
b=0
for value in max:
    if max[value] < -45 and roam[value] != 0:  
        print(f"{value}:{max[value]}, ", end='')
        b+=1
        
print(f"Number of TRA <-45 = {b}")
line1()
#------------------------------------------------------#

#TRA MAX > -35
c=0
print('{', end='')
for value in max:
    if max[value] > -35 and roam[value] != 0:  
        print(f"{value}:{max[value]}, ", end='')
        c+=1
        
print(f"\nNumber of TRA >-35 = {c}")
line1()
#------------------------------------------------------#

#TRA Roam < -70
d=0
for value in roam:
    if roam[value] <= -70:  
        print(f"{value}:{roam[value]}, ", end='')
        d+=1
        
print(f"Number of TRA < 70 = {d}")
line1()
#------------------------------------------------------#

#TRA Roam < -80
e=0
for value in roam:
    if roam[value] < -80:  
        print(f"{value}:{roam[value]}, ", end='')
        e+=1
        
print(f"Number of TRA < 80 = {e}")
line1()
#------------------------------------------------------#

#End