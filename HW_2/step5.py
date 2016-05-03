from math import factorial as f
ans = 0
for k in range(26, 51):
    ans += f(50)/f(k)/f(50-k)*(0.55**k)*(0.45**(50-k))
ans += f(50)/f(25)/f(25)*(0.55**25)*(0.45**25)/2
print(ans)
