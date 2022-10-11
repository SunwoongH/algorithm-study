money = int(input())
machine_duck = list(map(int, input().split()))
 
bnp_cash, timing_cash = money, money
bnp_stock, timing_stock = 0, 0

# BNP 
for i in machine_duck:                    
    if bnp_cash >= i:
        bnp_stock += bnp_cash // i
        bnp_cash %= i

# TIMING
for i in range(len(machine_duck) - 3):
    if machine_duck[i] > machine_duck[i+1] > machine_duck[i+2]:    # 하락, 하락, 하락 => 매수
        timing_stock += timing_cash // machine_duck[i+3]
        timing_cash %= machine_duck[i+3]
 
    elif machine_duck[i] < machine_duck[i+1] < machine_duck[i+2]:    # 상승, 상승, 상승 => 매도
        timing_cash += timing_stock * machine_duck[i+3]
        timing_stock = 0
 

bnp_asset = [bnp_cash + (machine_duck[-1] * bnp_stock)]
timing_asset = [timing_cash + (machine_duck[-1] * timing_stock)]
 
if bnp_asset > timing_asset:
    print('BNP')
elif bnp_asset < timing_asset:
    print('TIMING')
else:
    print('SAMESAME')