

rain = [0,1,0,2,1,0,1,3,2,1,2,1]

unit = 0

for i in range(1, len(rain) - 1):
    volumes = min(max(rain[:i]), max(rain[i:])) - rain[i]  
    if volumes > 0:
        unit += volumes

print(unit)