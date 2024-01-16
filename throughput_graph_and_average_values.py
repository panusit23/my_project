# Plot Graph of Throughput Performance
# Find Average Values

import matplotlib.pyplot as plt

line1 = lambda: print("="*50)
line2 = lambda: print("-"*50)
line3 = lambda: print()
line4 = lambda: print("*"*100)
line5 = lambda: print("*"*254)

print("***********Plot Graph************")

#------------------------------------------------

# MIN Input

bw_min_b = "TRA1109:0.0M, TRA1201:1.705M, TRA1202:7.732M, TRA1205:10.107M, TRA1206:3.163M, TRA1209:4.39M, TRA1210:7.125M, TRA1301:3.595M, TRA1302:1.431M, TRA1305:5.88M, TRA1306:3.56M, TRA1309:3.022M, TRA1401:4.685M, TRA1402:3.743M, TRA1405:8.075M, TRA1406:3.9M, TRA1409:2.789M, TRA1501:1.44M, TRA1502:2.37M, TRA1505:7.3M, TRA1506:0.0M, TRA1509:0.128M, TRA1510:3.31M, TRA1514:1.68M, TRA1601:0.871M, TRA1602:9.29M, TRA1605:9.86M, TRA1606:3.1M, TRA1609:3.74M, TRA1610:0.0M, TRA1614:5.795M, TRA1617:6.065M, TRA1618:8.31M, TRA1701:3.27M, TRA1702:4.725M, TRA1705:3.395M, TRA1706:9.605M, TRA1709:2.23M, TRA1710:2.861M, TRA1713:3.12M, TRA1714:0.0M, TRA1717:3.257M, TRA1718:3.895M, TRA1801:2.87M, TRA1802:3.15M, TRA1805:1.286M, TRA1809:1.099M, TRA1810:2.555M, TRA1901:1.942M, TRA1902:1.669M, TRA1905:2.83M, TRA1906:3.58M, TRA2001:0.981M, TRA2002:3.075M, TRA2005:2.209M, TRA2006:2.755M, TRA2009:3.505M, TRA2010:2.158M, TRA2013:12.95M, TRA2101:5.94M, TRA2102:10.52M, TRA2105:2.068M, TRA2109:2.215M, TRA2110:8.537M, TRA2201:5.577M, TRA2202:2.989M, TRA2205:1.245M, TRA2206:4.09M, TRA2209:6.622M, TRA2210:4.175M, TRA2301:0.689M, TRA2302:9.725M, TRA2305:1.721M, TRA2306:6.065M, TRA2309:1.192M, TRA2310:2.604M, TRA2313:6.99M, TRA2401:1.645M, TRA2402:4.316M, TRA2405:8.317M, TRA2406:6.621M, TRA2409:2.673M, TRA2410:12.39M, TRA2413:4.078M, TRA2414:1.413M, TRA2501:1.942M, TRA2502:6.86M, TRA2505:3.87M, TRA2506:3.93M, TRA2509:2.216M, TRA2510:2.183M, TRA2513:4.495M, TRA2601:3.085M, TRA2602:6.229M, TRA2605:12.28M, TRA2606:5.321M, TRA2609:7.74M, TRA2610:8.49M, TRA2613:11.1M, TRA2614:4.845M, TRA2617:8.2M, TRA2618:5.555M, TRA2621:1.151M, TRA2701:6.795M, TRA2702:5.456M, TRA2705:3.814M, TRA2706:4.265M, TRA2709:7.283M, TRA2710:6.75M, TRA2801:2.22M, TRA2802:4.56M, TRA2805:4.95M, TRA2806:1.36M, TRA2809:3.38M, TRA2810:4.01M, TRA2813:1.37M, TRA2814:13.5M, TRA2901:1.14M, TRA2902:8.48M, TRA2905:3.899M, TRA2906:13.55M"


bw_min_a = "TRA1109:10.275M, TRA1201:5.825M, TRA1202:9.675M, TRA1205:8.507M, TRA1206:3.682M, TRA1209:4.18M, TRA1210:5.862M, TRA1301:3.835M, TRA1302:7.092M, TRA1305:4.034M, TRA1306:2.551M, TRA1309:4.945M, TRA1401:7.725M, TRA1402:0.66M, TRA1405:7.6M, TRA1406:7.411M, TRA1409:2.282M, TRA1501:2.362M, TRA1502:1.721M, TRA1505:6.647M, TRA1506:0.189M, TRA1509:0.726M, TRA1510:0.485M, TRA1514:7.69M, TRA1601:2.94M, TRA1602:1.51M, TRA1605:10.795M, TRA1606:0.854M, TRA1609:2.05M, TRA1610:11.3M, TRA1614:4.683M, TRA1617:8.057M, TRA1618:8.905M, TRA1701:7.41M, TRA1702:1.749M, TRA1705:8.09M, TRA1706:4.78M, TRA1709:6.88M, TRA1710:2.395M, TRA1713:7.775M, TRA1714:5.9M, TRA1717:2.889M, TRA1718:2.1M, TRA1801:0.366M, TRA1802:2.664M, TRA1805:2.265M, TRA1809:1.45M, TRA1810:6.905M, TRA1901:2.19M, TRA1902:5.348M, TRA1905:2.385M, TRA1906:2.89M, TRA2001:0.97M, TRA2002:1.222M, TRA2005:6.353M, TRA2006:3.021M, TRA2009:2.9M, TRA2010:1.851M, TRA2013:6.01M, TRA2101:5.81M, TRA2102:3.31M, TRA2105:2.65M, TRA2109:1.045M, TRA2110:3.35M, TRA2201:6.01M, TRA2202:2.41M, TRA2205:2.38M, TRA2206:5.274M, TRA2209:6.27M, TRA2210:4.396M, TRA2301:1.794M, TRA2302:0.0M, TRA2305:1.415M, TRA2306:5.6M, TRA2309:1.837M, TRA2310:2.223M, TRA2313:14.84M, TRA2401:2.089M, TRA2402:5.66M, TRA2405:2.025M, TRA2406:2.675M, TRA2409:5.235M, TRA2410:10.24M, TRA2413:1.534M, TRA2414:3.811M, TRA2501:7.105M, TRA2502:5.27M, TRA2505:5.595M, TRA2506:5.235M, TRA2509:3.157M, TRA2510:4.657M, TRA2513:6.29M, TRA2601:16.3M, TRA2602:5.44M, TRA2605:2.645M, TRA2606:2.835M, TRA2609:1.275M, TRA2610:1.975M, TRA2613:5.25M, TRA2614:1.495M, TRA2617:9.77M, TRA2618:8.81M, TRA2621:3.635M, TRA2701:6.215M, TRA2702:5.546M, TRA2705:2.431M, TRA2706:4.523M, TRA2709:4.18M, TRA2710:0.094M, TRA2801:1.36M, TRA2802:4.06M, TRA2805:0.141M, TRA2806:0.0M, TRA2809:0.257M, TRA2810:0.012M, TRA2813:10.615M, TRA2814:6.265M, TRA2901:0.939M, TRA2902:1.35M, TRA2905:9.55M, TRA2906:12.15M"


bw_min_b_a = "TRA1109:10.275M, TRA1201:7.53M, TRA1202:17.407M, TRA1205:18.613M, TRA1206:6.845M, TRA1209:8.57M, TRA1210:12.988M, TRA1301:7.43M, TRA1302:8.524M, TRA1305:9.914M, TRA1306:6.111M, TRA1309:7.967M, TRA1401:12.41M, TRA1402:4.402M, TRA1405:15.675M, TRA1406:11.311M, TRA1409:5.071M, TRA1501:3.803M, TRA1502:4.091M, TRA1505:13.947M, TRA1506:0.189M, TRA1509:0.854M, TRA1510:3.795M, TRA1514:9.37M, TRA1601:3.811M, TRA1602:10.8M, TRA1605:20.655M, TRA1606:3.954M, TRA1609:5.79M, TRA1610:11.3M, TRA1614:10.477M, TRA1617:14.122M, TRA1618:17.215M, TRA1701:10.68M, TRA1702:6.474M, TRA1705:11.485M, TRA1706:14.385M, TRA1709:9.11M, TRA1710:5.256M, TRA1713:10.895M, TRA1714:5.9M, TRA1717:6.147M, TRA1718:5.995M, TRA1801:3.236M, TRA1802:5.814M, TRA1805:3.551M, TRA1809:2.549M, TRA1810:9.46M, TRA1901:4.132M, TRA1902:7.016M, TRA1905:5.215M, TRA1906:6.47M, TRA2001:1.95M, TRA2002:4.298M, TRA2005:8.562M, TRA2006:5.776M, TRA2009:6.405M, TRA2010:4.01M, TRA2013:18.96M, TRA2101:11.75M, TRA2102:13.83M, TRA2105:4.718M, TRA2109:3.26M, TRA2110:11.886M, TRA2201:11.587M, TRA2202:5.399M, TRA2205:3.625M, TRA2206:9.364M, TRA2209:12.893M, TRA2210:8.571M, TRA2301:2.483M, TRA2302:9.725M, TRA2305:3.136M, TRA2306:11.665M, TRA2309:3.029M, TRA2310:4.827M, TRA2313:21.83M, TRA2401:3.734M, TRA2402:9.976M, TRA2405:10.342M, TRA2406:9.296M, TRA2409:7.908M, TRA2410:22.63M, TRA2413:5.612M, TRA2414:5.224M, TRA2501:9.047M, TRA2502:12.13M, TRA2505:9.465M, TRA2506:9.165M, TRA2509:5.373M, TRA2510:6.84M, TRA2513:10.785M, TRA2601:19.385M, TRA2602:11.668M, TRA2605:14.925M, TRA2606:8.156M, TRA2609:9.015M, TRA2610:10.465M, TRA2613:16.35M, TRA2614:6.34M, TRA2617:17.97M, TRA2618:14.365M, TRA2621:4.786M, TRA2701:13.01M, TRA2702:11.002M, TRA2705:6.245M, TRA2706:8.788M, TRA2709:11.463M, TRA2710:6.844M, TRA2801:3.58M, TRA2802:8.62M, TRA2805:5.091M, TRA2806:1.36M, TRA2809:3.637M, TRA2810:4.022M, TRA2813:11.985M, TRA2814:19.765M, TRA2901:2.079M, TRA2902:9.83M, TRA2905:13.449M, TRA2906:25.7M" 


#------------------------------------------------

# AVG Input

bw_avg_b = "{TRA1109:0.0M, TRA1201:11.317M, TRA1202:18.531M, TRA1205:19.925M, TRA1206:15.668M, TRA1209:15.411M, TRA1210:15.309M, TRA1301:13.188M, TRA1302:15.313M, TRA1305:15.229M, TRA1306:12.666M, TRA1309:16.808M, TRA1401:19.652M, TRA1402:11.435M, TRA1405:17.422M, TRA1406:14.769M, TRA1409:10.326M, TRA1501:11.825M, TRA1502:11.575M, TRA1505:11.875M, TRA1506:0.0M, TRA1509:8.527M, TRA1510:14.822M, TRA1514:11.038M, TRA1601:13.683M, TRA1602:21.053M, TRA1605:15.982M, TRA1606:17.039M, TRA1609:8.709M, TRA1610:0.0M, TRA1614:10.324M, TRA1617:20.099M, TRA1618:15.996M, TRA1701:16.406M, TRA1702:16.317M, TRA1705:14.104M, TRA1706:18.799M, TRA1709:16.724M, TRA1710:12.319M, TRA1713:14.809M, TRA1714:13.147M, TRA1717:13.118M, TRA1718:13.965M, TRA1801:19.194M, TRA1802:15.264M, TRA1805:16.31M, TRA1809:11.002M, TRA1810:13.372M, TRA1901:14.772M, TRA1902:13.284M, TRA1905:12.957M, TRA1906:14.894M, TRA2001:7.041M, TRA2002:13.25M, TRA2005:14.862M, TRA2006:11.192M, TRA2009:15.14M, TRA2010:15.205M, TRA2013:22.287M, TRA2101:19.159M, TRA2102:16.681M, TRA2105:14.706M, TRA2109:14.825M, TRA2110:15.832M, TRA2201:11.689M, TRA2202:12.999M, TRA2205:8.17M, TRA2206:12.337M, TRA2209:16.402M, TRA2210:14.017M, TRA2301:14.335M, TRA2302:13.411M, TRA2305:9.451M, TRA2306:15.844M, TRA2309:9.784M, TRA2310:10.07M, TRA2313:15.468M, TRA2401:12.4M, TRA2402:16.152M, TRA2405:12.994M, TRA2406:15.845M, TRA2409:12.187M, TRA2410:19.684M, TRA2413:17.078M, TRA2414:15.538M, TRA2501:17.352M, TRA2502:15.774M, TRA2505:13.76M, TRA2506:17.383M, TRA2509:12.544M, TRA2510:12.928M, TRA2513:15.667M, TRA2601:19.284M, TRA2602:19.112M, TRA2605:22.077M, TRA2606:15.563M, TRA2609:17.872M, TRA2610:19.13M, TRA2613:19.572M, TRA2614:16.682M, TRA2617:17.086M, TRA2618:17.513M, TRA2621:14.887M, TRA2701:21.573M, TRA2702:16.613M, TRA2705:9.109M, TRA2706:13.644M, TRA2709:12.97M, TRA2710:14.805M, TRA2801:19.143M, TRA2802:17.376M, TRA2805:12.735M, TRA2806:6.924M, TRA2809:15.271M, TRA2810:8.188M, TRA2813:17.453M, TRA2814:17.92M, TRA2901:13.052M, TRA2902:13.476M, TRA2905:10.774M, TRA2906:17.629M"


bw_avg_a = "TRA1109:19.71M, TRA1201:16.546M, TRA1202:20.393M, TRA1205:17.015M, TRA1206:10.016M, TRA1209:15.524M, TRA1210:13.182M, TRA1301:14.122M, TRA1302:13.205M, TRA1305:11.454M, TRA1306:14.326M, TRA1309:20.65M, TRA1401:16.355M, TRA1402:11.84M, TRA1405:17.793M, TRA1406:13.166M, TRA1409:11.151M, TRA1501:13.977M, TRA1502:8.736M, TRA1505:7.934M, TRA1506:0.189M, TRA1509:6.346M, TRA1510:13.449M, TRA1514:14.015M, TRA1601:12.619M, TRA1602:25.353M, TRA1605:17.469M, TRA1606:10.349M, TRA1609:13.362M, TRA1610:17.65M, TRA1614:14.901M, TRA1617:21.347M, TRA1618:14.759M, TRA1701:16.205M, TRA1702:12.934M, TRA1705:15.188M, TRA1706:14.932M, TRA1709:16.689M, TRA1710:10.542M, TRA1713:18.856M, TRA1714:14.455M, TRA1717:14.957M, TRA1718:18.993M, TRA1801:14.17M, TRA1802:13.371M, TRA1805:13.629M, TRA1809:12.801M, TRA1810:19.31M, TRA1901:14.4M, TRA1902:13.954M, TRA1905:12.336M, TRA1906:15.268M, TRA2001:8.45M, TRA2002:12.262M, TRA2005:15.463M, TRA2006:9.193M, TRA2009:14.449M, TRA2010:15.526M, TRA2013:17.111M, TRA2101:15.786M, TRA2102:13.404M, TRA2105:15.611M, TRA2109:16.239M, TRA2110:16.025M, TRA2201:14.901M, TRA2202:9.311M, TRA2205:6.722M, TRA2206:14.645M, TRA2209:12.676M, TRA2210:12.116M, TRA2301:8.455M, TRA2302:0.0M, TRA2305:11.266M, TRA2306:13.387M, TRA2309:9.515M, TRA2310:13.182M, TRA2313:22.848M, TRA2401:11.131M, TRA2402:14.175M, TRA2405:14.409M, TRA2406:15.361M, TRA2409:15.602M, TRA2410:20.521M, TRA2413:18.834M, TRA2414:12.492M, TRA2501:16.507M, TRA2502:13.997M, TRA2505:14.319M, TRA2506:19.264M, TRA2509:9.374M, TRA2510:12.826M, TRA2513:22.892M, TRA2601:19.667M, TRA2602:15.441M, TRA2605:7.912M, TRA2606:6.282M, TRA2609:7.626M, TRA2610:8.123M, TRA2613:8.592M, TRA2614:13.583M, TRA2617:15.964M, TRA2618:17.677M, TRA2621:18.527M, TRA2701:16.199M, TRA2702:13.827M, TRA2705:11.37M, TRA2706:13.055M, TRA2709:12.148M, TRA2710:13.386M, TRA2801:14.438M, TRA2802:13.64M, TRA2805:9.767M, TRA2806:6.901M, TRA2809:10.103M, TRA2810:8.839M, TRA2813:15.474M, TRA2814:15.02M, TRA2901:10.667M, TRA2902:13.534M, TRA2905:17.503M, TRA2906:17.556M"


bw_avg_b_a = "TRA1109:19.71M, TRA1201:27.863M, TRA1202:38.925M, TRA1205:36.94M, TRA1206:25.684M, TRA1209:30.934M, TRA1210:28.491M, TRA1301:27.31M, TRA1302:28.518M, TRA1305:26.683M, TRA1306:26.991M, TRA1309:37.458M, TRA1401:36.007M, TRA1402:23.275M, TRA1405:35.215M, TRA1406:27.935M, TRA1409:21.477M, TRA1501:25.802M, TRA1502:20.311M, TRA1505:19.809M, TRA1506:0.189M, TRA1509:14.873M, TRA1510:28.271M, TRA1514:25.053M, TRA1601:26.302M, TRA1602:46.406M, TRA1605:33.452M, TRA1606:27.388M, TRA1609:22.071M, TRA1610:17.65M, TRA1614:25.225M, TRA1617:41.447M, TRA1618:30.755M, TRA1701:32.611M, TRA1702:29.251M, TRA1705:29.292M, TRA1706:33.731M, TRA1709:33.413M, TRA1710:22.861M, TRA1713:33.665M, TRA1714:27.602M, TRA1717:28.075M, TRA1718:32.957M, TRA1801:33.364M, TRA1802:28.635M, TRA1805:29.939M, TRA1809:23.803M, TRA1810:32.682M, TRA1901:29.172M, TRA1902:27.238M, TRA1905:25.293M, TRA1906:30.162M, TRA2001:15.491M, TRA2002:25.512M, TRA2005:30.325M, TRA2006:20.384M, TRA2009:29.589M, TRA2010:30.731M, TRA2013:39.397M, TRA2101:34.946M, TRA2102:30.085M, TRA2105:30.317M, TRA2109:31.064M, TRA2110:31.857M, TRA2201:26.59M, TRA2202:22.31M, TRA2205:14.892M, TRA2206:26.982M, TRA2209:29.078M, TRA2210:26.133M, TRA2301:22.79M, TRA2302:13.411M, TRA2305:20.717M, TRA2306:29.231M, TRA2309:19.299M, TRA2310:23.251M, TRA2313:38.316M, TRA2401:23.532M, TRA2402:30.327M, TRA2405:27.403M, TRA2406:31.205M, TRA2409:27.789M, TRA2410:40.205M, TRA2413:35.912M, TRA2414:28.03M, TRA2501:33.859M, TRA2502:29.771M, TRA2505:28.079M, TRA2506:36.647M, TRA2509:21.918M, TRA2510:25.754M, TRA2513:38.559M, TRA2601:38.95M, TRA2602:34.553M, TRA2605:29.99M, TRA2606:21.845M, TRA2609:25.498M, TRA2610:27.253M, TRA2613:28.164M, TRA2614:30.265M, TRA2617:33.05M, TRA2618:35.19M, TRA2621:33.414M, TRA2701:37.772M, TRA2702:30.441M, TRA2705:20.479M, TRA2706:26.699M, TRA2709:25.119M, TRA2710:28.191M, TRA2801:33.581M, TRA2802:31.016M, TRA2805:22.502M, TRA2806:13.825M, TRA2809:25.374M, TRA2810:17.027M, TRA2813:32.926M, TRA2814:32.94M, TRA2901:23.718M, TRA2902:27.01M, TRA2905:28.277M, TRA2906:35.185M"


#------------------------------------------------

# All TRA Under Test

all_tra = "1201, 1202, 1205, 1206, 1209, 1210, 1301, 1302, 1305, 1306, 1309, 1401, 1402, 1405, 1406, 1409, 1501, 1502, 1505, 1506, 1509, 1510, 1513, 1514, 1601, 1602, 1605, 1606, 1609, 1610, 1613, 1614, 1617, 1618, 1701, 1702, 1705, 1706, 1709, 1710, 1713, 1714, 1717, 1718, 1801, 1802, 1805, 1806, 1809, 1810, 1901, 1902, 1905, 1906, 2001, 2002, 2005, 2006, 2009, 2010, 2013, 2101, 2102, 2105, 2106, 2109, 2110, 2201, 2202, 2205, 2206, 2209, 2210, 2301, 2302, 2305, 2306, 2309, 2310, 2313, 2401, 2402, 2405, 2406, 2409, 2410, 2413, 2414, 2501, 2502, 2505, 2506, 2509, 2510, 2513, 2601, 2602, 2605, 2606, 2609, 2610, 2613, 2614, 2617, 2618, 2621, 2701, 2702, 2705, 2706, 2709, 2710, 2801, 2802, 2805, 2806, 2809, 2810, 2813, 2814, 2901, 2902, 2905, 2906, 2909, 3001, 3002"
    
    
#------------------------------------------------
# str to list
tra = all_tra.strip()
all_tra_split = tra.split(", ")

# Remove TRA wording
tra_bw = bw_min_b
tra_bw_split = tra_bw.split(",")
#print(tra_bw_split)

tra_bw_present = []
for tra_i in range(len(tra_bw_split)):
    remove_tra_word = tra_bw_split[tra_i].replace("TRA", "").replace("M", "")
    remove_tra_word = remove_tra_word.strip()
    remove_tra_word = remove_tra_word[:4]
    tra_bw_present.append(remove_tra_word)


print(f"All TRA Under Test = {len(all_tra_split)}")
#print(f"All TRA Under Test = {all_tra_split}")
line2()
print(f"TRA with Bandwidth Data = {len(tra_bw_present)}")
#print(f"TRA with Bandwidth Data = {tra_bw_present}")
line2()
   
all_tra_split = set(list(all_tra_split))
tra_bw_present = set(list(tra_bw_present))

tra_no_bw_data = all_tra_split.difference(tra_bw_present)
    
print(f"TRA with No Bandwidth Data = {len(tra_no_bw_data)}")
print(f"TRA with No Bandwidth Data = {sorted(tra_no_bw_data)}")
line3()


#------------------------------------------------    

def plot_bw(get_input, get_value, get_cab):
    
    # split TRA
    bw = get_input.split(",")
    
    # clean data
    bw_list = []
    for i in range(len(bw)):
        bw_word = bw[i].replace("M", "")
        bw_list.append(bw_word)
        
    # str to dict     
    bw_dict = {}
    for j in bw_list:
        key, value = j.split(":")
        bw_dict[key.strip()] = float(value.strip())
    #print(bw_dict)
    
    # dict to list to plot graph   
    keys = list(bw_dict.keys())
    values = list(bw_dict.values())
    
   
    values_sum = sum(values)
    values_len = len(values)
    average_values = values_sum/values_len
    #print(average_values)
        
    
    line1()
    print("--Output--")
    line1()
    
    
    #--------------------------------------------

    # find value and retune x&y for plot
    if get_value == "min":
        if get_cab =="b":
            print("Minimum Bandwidth - Cab B")
            line3()
            print(f"TRA with Bandwidth Data = {len(keys)}")
            line2()
            print("1)Min (Bandwidth < 5Mbps) = ", end = "")
            count_min= 0
            for i_min in bw_dict:
                if bw_dict[i_min] < 5:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1
            line3()
            print(f"=>The Number of Min Bandwidth Cab B (Bandwidth < 5Mbps) = {count_min}")
            line3()

            print("2)Min (5Mbps < Bandwidth < 10Mbps) = ", end = "") 
            count_min = 0
            for i_min in bw_dict:
                if 5 < bw_dict[i_min] < 10:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            print()
            print(f"=>The Number of Min Bandwidth Cab B (5Mbps < Bandwidth < 10Mbps) = {count_min}")
            line3()

            print("3)Min (10Mbps < Bandwidth < 15Mbps) = ", end = "") 
            count_min = 0
            for i_min in bw_dict:
                if 10 < bw_dict[i_min] < 15:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            print()
            print(f"=>The Number of Min Bandwidth Cab B (10Mbps < Bandwidth < 15Mbps) = {count_min}")
            line3()

            print("4)Min (Bandwidth > 15Mbps) = ", end = "") 
            count_min = 0
            for i_min in bw_dict:
                if bw_dict[i_min] > 15:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            print()
            print(f"=>The Number of Min Bandwidth Cab B (Bandwidth > 15Mbps) = {count_min}")
            count_min = 0
            line3()
            
            print(f"5)Average Value of All TRAs (Minimum Bandwidth - Cab B) = {average_values:.2f} Mbps")
            line3()

        elif get_cab =="a": 
            print("Minimum Bandwidth - Cab A")
            line3()
            print(f"TRA with Bandwidth Data = {len(keys)}")
            line2()

            print("1)Min (Bandwidth < 5Mbps) = ", end = "")
            count_min= 0
            for i_min in bw_dict:
                if bw_dict[i_min] < 5:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            line3()
            print(f"=>The Number of Min Bandwidth Cab A (Bandwidth < 5Mbps) = {count_min}")
            line3()

            print("2)Min (5Mbps < Bandwidth < 10Mbps) = ", end = "") 
            count_min = 0
            for i_min in bw_dict:
                if 5 < bw_dict[i_min] < 10:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            print()
            print(f"=>The Number of Min Bandwidth Cab A (5Mbps < Bandwidth < 10Mbps) = {count_min}")
            line3()

            print("3)Min (10Mbps < Bandwidth < 15Mbps) = ", end = "") 
            count_min = 0
            for i_min in bw_dict:
                if 10 < bw_dict[i_min] < 15:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            print()
            print(f"=>The Number of Min Bandwidth Cab A (10Mbps < Bandwidth < 15Mbps) = {count_min}")
            line3()

            print("4)Min (Bandwidth > 15Mbps) = ", end = "") 
            count_min = 0
            for i_min in bw_dict:
                if bw_dict[i_min] > 15:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            print()
            print(f"=>The Number of Min Bandwidth Cab A (Bandwidth > 15Mbps) = {count_min}")
            count_min = 0
            line3()
            
            print(f"5)Average Value of All TRAs (Minimum Bandwidth - Cab A) = {average_values:.2f} Mbps")
            line3()
            
            #------------------------------------------------ 
            
        else:
            print("Sum of Minimum Bandwidth (Cab B+A)")
            line3()
            print(f"TRA with Bandwidth Data = {len(keys)}")
            line2()

            print("1)Min (Bandwidth < 10Mbps) = ", end = "")
            count_min= 0
            for i_min in bw_dict:
                if bw_dict[i_min] < 10:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            line3()
            print(f"=>The Number of Min Bandwidth Cab B+A (Bandwidth < 10Mbps) = {count_min}")
            line3()

            print("2)Min (10Mbps < Bandwidth < 20Mbps) = ", end = "") 
            count_min = 0
            for i_min in bw_dict:
                if 10 < bw_dict[i_min] < 20:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            print()
            print(f"=>The Number of Min Bandwidth Cab B+A (10Mbps < Bandwidth < 20Mbps) = {count_min}")
            line3()

            print("3)Min (20Mbps < Bandwidth < 30Mbps) = ", end = "") 
            count_min = 0
            for i_min in bw_dict:
                if 20 < bw_dict[i_min] < 30:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            print()
            print(f"=>The Number of Min Bandwidth Cab B+A (20Mbps < Bandwidth < 30Mbps) = {count_min}")
            line3()

            print("4)Min (Bandwidth > 30Mbps) = ", end = "") 
            count_min = 0
            for i_min in bw_dict:
                if bw_dict[i_min] > 30:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            print()
            print(f"=>The Number of Min Bandwidth Cab B+A (Bandwidth > 30Mbps) = {count_min}")
            count_min = 0
            line3()
            
            print(f"5)Average Value of All TRAs (Sum of Minimum Bandwidth Cab B+A) = {average_values:.2f} Mbps")
            line3()

#------------------------------------------------  

    # find value and plot (AVG)
    else: 
        if get_cab =="b":       
            print("Average Bandwidth - Cab B")
            line3()
            print(f"TRA with Bandwidth Data = {len(keys)}")
            line2()
            
            print("1)Avg (Bandwidth < 5Mbps) = ", end = "")
            count_min= 0
            for i_min in bw_dict:
                if bw_dict[i_min] < 5:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            line3()
            print(f"=>The Number of Avg Bandwidth Cab B (Bandwidth < 5Mbps) = {count_min}")
            line3()
            
            print("2)Avg (5Mbps < Bandwidth < 10Mbps) = ", end = "") 
            count_min = 0
            for i_min in bw_dict:
                if 5 < bw_dict[i_min] < 10:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            print()
            print(f"=>The Number of Avg Bandwidth Cab B (5Mbps < Bandwidth < 10Mbps) = {count_min}")
            line3()
            
            print("3)Avg (10Mbps < Bandwidth < 15Mbps) = ", end = "") 
            count_min = 0
            for i_min in bw_dict:
                if 10 < bw_dict[i_min] < 15:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            print()
            print(f"=>The Number of Avg Bandwidth Cab B (10Mbps < Bandwidth < 15Mbps) = {count_min}")
            line3()
            
            print("4)Avg (Bandwidth > 15Mbps) = ", end = "") 
            count_min = 0
            for i_min in bw_dict:
                if bw_dict[i_min] > 15:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            print()
            print(f"=>The Number of Avg Bandwidth Cab B (Bandwidth > 15Mbps) = {count_min}")
            count_min = 0
            line3()
            
            print(f"5)Average Value of All TRAs (Average Bandwidth - Cab B) = {average_values:.2f} Mbps")
            line3()
            
            #------------------------------------------------  
            
        elif get_cab =="a": 
            print("Average Bandwidth - Cab A ")
            line3()
            print(f"TRA with Bandwidth Data = {len(keys)}")
            line2()

            print("1)Avg (Bandwidth < 5Mbps) = ", end = "")
            count_min= 0
            for i_min in bw_dict:
                if bw_dict[i_min] < 5:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            line3()
            print(f"=>The Number of Avg Bandwidth Cab A (Bandwidth < 5Mbps) = {count_min}")
            line3()

            print("2)Avg (5Mbps < Bandwidth < 10Mbps) = ", end = "") 
            count_min = 0
            for i_min in bw_dict:
                if 5 < bw_dict[i_min] < 10:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            print()
            print(f"=>The Number of Avg Bandwidth Cab A (5Mbps < Bandwidth < 10Mbps) = {count_min}")
            line3()

            print("3)Avg (10Mbps < Bandwidth < 15Mbps) = ", end = "") 
            count_min = 0
            for i_min in bw_dict:
                if 10 < bw_dict[i_min] < 15:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            print()
            print(f"=>The Number of Avg Bandwidth Cab A (10Mbps < Bandwidth < 15Mbps) = {count_min}")
            line3()

            print("4)Avg (Bandwidth > 15Mbps) = ", end = "") 
            count_min = 0
            for i_min in bw_dict:
                if bw_dict[i_min] > 15:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            print()
            print(f"=>The Number of Avg Bandwidth Cab A (Bandwidth > 15Mbps) = {count_min}")
            count_min = 0
            line3()
            
            print(f"5)Average Value of All TRAs (Average Bandwidth - Cab A) = {average_values:.2f} Mbps")
            line3()
            
            #------------------------------------------------  
            
        else:
            print("Sum of Average Bandwidth (Cab B+A)")
            line3()
            print(f"TRA with Bandwidth Data = {len(keys)}")
            line2()

            print("1)Avg (Bandwidth < 10Mbps) = ", end = "")
            count_min= 0
            for i_min in bw_dict:
                if bw_dict[i_min] < 10:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            line3()
            print(f"=>The Number of Avg Bandwidth Cab B+A (Bandwidth < 10Mbps) = {count_min}")
            line3()

            print("2)Avg (10Mbps < Bandwidth < 20Mbps) = ", end = "") 
            count_min = 0
            for i_min in bw_dict:
                if 10 < bw_dict[i_min] < 20:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            print()
            print(f"=>The Number of Avg Bandwidth Cab B+A (10Mbps < Bandwidth < 20Mbps) = {count_min}")
            line3()

            print("3)Avg (20Mbps < Bandwidth < 30Mbps) = ", end = "") 
            count_min = 0
            for i_min in bw_dict:
                if 20 < bw_dict[i_min] < 30:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            print()
            print(f"=>The Number of Avg Bandwidth Cab B+A (20Mbps < Bandwidth < 30Mbps) = {count_min}")
            line3()

            print("4)Avg (Bandwidth > 30Mbps) = ", end = "") 
            count_min = 0
            for i_min in bw_dict:
                if bw_dict[i_min] > 30:  
                    print(f"{i_min}:{bw_dict[i_min]}M,", end = " ")
                    count_min += 1  
            print()
            print(f"=>The Number of Avg Bandwidth Cab B+A (Bandwidth > 30Mbps) = {count_min}")
            count_min = 0
            line3()
            
            print(f"5)Average Value of All TRAs (Sum of Average Bandwidth Cab B+A) = {average_values:.2f} Mbps")
            line3()

    return keys, values

#------------------------------------------------

line4()
line3()
print("Part 1")

plot_min_bx, plot_min_by = plot_bw(bw_min_b, "min", "b")
plt.figure(figsize=(30, 6), dpi=500)
plt.plot(plot_min_bx, plot_min_by, marker="x", label="Min-Cab B")
plt.legend(loc="upper left")
plt.xlabel("TRA with Bandwidth Data")
plt.xticks(rotation=90)
plt.ylabel("Bandwidth (Mbps)")
plt.title("Minimum Bandwidth - Cab B")
plt.grid(True)
plt.savefig("z1-CabB-Min.png", bbox_inches="tight")
plt.show()

plt.hist(plot_min_by, label="Min-Cab B", alpha=0.7, bins=15)
plt.legend(loc="upper right")
plt.xlabel("Bandwidth (Mbps)")
plt.ylabel("The Number of TRAs")
plt.title("Histogram of Minimum Bandwidth - Cab B")
plt.grid(True)
plt.savefig("z1-CabB-Min-Hist.png", bbox_inches="tight")
plt.show()
#-----------------------

plot_min_ax, plot_min_ay = plot_bw(bw_min_a, "min", "a")
plt.figure(figsize=(30, 6), dpi=500)
plt.plot(plot_min_ax, plot_min_ay, color="red", marker="x", label="Min-Cab A")
plt.legend(loc="upper left")
plt.xlabel("TRA with Bandwidth Data")
plt.xticks(rotation=90)
plt.ylabel("Bandwidth (Mbps)")
plt.title("Minimum Bandwidth - Cab A")
plt.grid(True)
plt.savefig("z2-CabA-Min.png", bbox_inches="tight")
plt.show()

plt.hist(plot_min_ay, color="red", label="Min-Cab A", alpha=0.7, bins=15)
plt.legend(loc="upper right")
plt.xlabel("Bandwidth (Mbps)")
plt.ylabel("The Number of TRAs")
plt.title("Histogram of Minimum Bandwidth - Cab A")
plt.grid(True)
plt.savefig("z2-CabA-Min-Hist.png", bbox_inches="tight")
plt.show()
#-----------------------

plot_min_bax, plot_min_bay = plot_bw(bw_min_b_a, "min", "ba")
plt.figure(figsize=(30, 6), dpi=500)
plt.plot(plot_min_bax, plot_min_bay, color="green", marker="x", label="Min-Cab B+A")
plt.legend(loc="upper left")
plt.xlabel("TRA with Bandwidth Data")
plt.xticks(rotation=90)
plt.ylabel("Bandwidth (Mbps)")
plt.title("Sum of Minimum Bandwidth (Cab B+A)")
plt.grid(True)
plt.savefig("z3-Sum-Min.png", bbox_inches="tight")
plt.show()

plt.hist(plot_min_bay, color="green", label="Min-Cab B+A", alpha=0.7, bins=15)
plt.legend(loc="upper right")
plt.xlabel("Bandwidth (Mbps)")
plt.ylabel("The Number of TRAs")
plt.title("Histogram of Sum Minimum Bandwidth - Cab B+A")
plt.grid(True)
plt.savefig("z3-Sum-Min-Hist.png", bbox_inches="tight")
plt.show()
#-----------------------

#plot all min
print("\n#---------------Minimum Bandwidth Comparison---------------#")
plt.figure(figsize=(30, 6), dpi=500)
plt.plot(plot_min_bx, plot_min_by, marker="x", label="Min-Cab B")
plt.plot(plot_min_ax, plot_min_ay, color="red", marker="x", label="Min-Cab A")
plt.plot(plot_min_bax, plot_min_bay, color="green", marker="x", label="Min-Cab B+A")
plt.legend(loc="upper left")
plt.xlabel("TRA with Bandwidth Data")
plt.xticks(rotation=90)
plt.ylabel("Bandwidth (Mbps)")
plt.title("Minimum Bandwidth Comparison")
plt.grid(True)
plt.savefig("z4-Comparison-Min.png", bbox_inches="tight")
plt.show()

plt.hist(plot_min_by, label="Min-Cab B", alpha=0.4, bins=15)
plt.hist(plot_min_ay, color="red", label="Min-Cab A", alpha=0.4, bins=15)
plt.hist(plot_min_bay, color="green", label="Min-Cab B+A", alpha=0.4, bins=15)
plt.legend(loc="upper right")
plt.xlabel("Bandwidth (Mbps)")
plt.ylabel("The Number of TRAs")
plt.title("Histogram of Minimum Bandwidth Comparison")
plt.grid(True)
plt.savefig("z4-Comparison-Min-Hist.png", bbox_inches="tight")
plt.show()
#-----------------------



line4()
line3()
print("Part 2")

plot_avg_bx, plot_avg_by = plot_bw(bw_avg_b, "avg", "b")
plt.figure(figsize=(30, 6), dpi=500)
plt.plot(plot_avg_bx, plot_avg_by, marker="x", label="Avg-Cab B")
plt.legend(loc="upper left")
plt.xlabel("TRA with Bandwidth Data")
plt.xticks(rotation=90)
plt.ylabel("Bandwidth (Mbps)")
plt.title("Average Bandwidth - Cab B")
plt.grid(True)
plt.savefig("z5-Cab-B-Avg.png", bbox_inches="tight")
plt.show()            

plt.hist(plot_avg_by, label="Avg-Cab B", alpha=0.7, bins=15)
plt.legend(loc="upper left")
plt.xlabel("Bandwidth (Mbps)")
plt.ylabel("The Number of TRAs")
plt.title("Histogram of Average Bandwidth - Cab B")
plt.grid(True)
plt.savefig("z5-Cab-B-Avg-Hist.png", bbox_inches="tight")
plt.show()
#-----------------------

plot_avg_ax, plot_avg_ay = plot_bw(bw_avg_a, "avg", "a")
plt.figure(figsize=(30, 6), dpi=500)
plt.plot(plot_avg_ax, plot_avg_ay, color="red", marker="x", label="Avg-Cab A")
plt.legend(loc="upper left")
plt.xlabel("TRA with Bandwidth Data")
plt.xticks(rotation=90)
plt.ylabel("Bandwidth (Mbps)")
plt.title("Average Bandwidth - Cab A")
plt.grid(True)
plt.savefig("z6-Cab-A-Avg.png", bbox_inches="tight")
plt.show()    


plt.hist(plot_avg_ay, color="red", label="Avg-Cab A", alpha=0.7, bins=15)
plt.legend(loc="upper left")
plt.xlabel("Bandwidth (Mbps)")
plt.ylabel("The Number of TRAs")
plt.title("Histogram of Average Bandwidth - Cab A")
plt.grid(True)
plt.savefig("z6-Cab-A-Avg-Hist.png", bbox_inches="tight")
plt.show()
#-----------------------


plot_avg_bax, plot_avg_bay = plot_bw(bw_avg_b_a, "avg", "ba")
plt.figure(figsize=(30, 6), dpi=500)
plt.plot(plot_avg_bax, plot_avg_bay, color="green", marker="x", label="Avg-Cab B+A")
plt.legend(loc="upper left")
plt.xlabel("TRA with Bandwidth Data")
plt.xticks(rotation=90)
plt.ylabel("Bandwidth (Mbps)")
plt.title("Sum of Avergae Bandwidth (Cab B+A)")
plt.grid(True)
plt.savefig("z7-Sum-Avg.png", bbox_inches="tight")
plt.show()

plt.hist(plot_avg_bay, color="green", label="Avg-Cab B+A", alpha=0.7, bins=15)
plt.legend(loc="upper left")
plt.xlabel("Bandwidth (Mbps)")
plt.ylabel("The Number of TRAs")
plt.title("Histogram of Sum Avergae Bandwidth - Cab B+A")
plt.grid(True)
plt.savefig("z7-Sum-Avg-Hist.png", bbox_inches="tight")
plt.show()
#-----------------------

#plot all Avg
print("\n#---------------Average Bandwidth Comparison---------------#")
plt.figure(figsize=(30, 6), dpi=500)
plt.plot(plot_avg_bx, plot_avg_by, marker="x", label="Avg-Cab B")
plt.plot(plot_avg_ax, plot_avg_ay, color="red", marker="x", label="Avg-Cab A")
plt.plot(plot_avg_bax, plot_avg_bay, color="green", marker="x", label="Avg-Cab B+A")
plt.legend(loc="upper left")
plt.xlabel("TRA with Bandwidth Data")
plt.xticks(rotation=90)
plt.ylabel("Bandwidth (Mbps)")
plt.title("Average Bandwidth Comparison")
plt.grid(True)
plt.savefig("z8-Comparison-Avg.png", bbox_inches="tight")
plt.show() 

plt.hist(plot_avg_by, label="Avg-Cab B", alpha=0.4, bins=15)
plt.hist(plot_avg_ay, color="red", label="Avg-Cab A", alpha=0.4, bins=15)
plt.hist(plot_avg_bay, color="green", label="Avg-Cab B+A", alpha=0.4, bins=15)
plt.legend(loc="upper left")
plt.xlabel("Bandwidth (Mbps)")
plt.ylabel("The Number of TRAs")
plt.title("Histogram of Average Bandwidth Comparison")
plt.grid(True)
plt.savefig("z8-Comparison-Avg-Hist.png", bbox_inches="tight")
plt.show()

line5()
line3()
print("!!!!!!!!!!!!!!!!!Done!!!!!!!!!!!!!!!!!!!")

#end

