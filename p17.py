import time

N = 1000

t0 = time.time()
letters = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4,
           6: 3, 7: 5, 8: 5, 9: 4, 10: 3,
           11: 6, 12: 6, 13: 8, 14: 8, 15: 7,
           16: 7, 17: 9, 18: 8, 19: 8, 20: 6,
           30: 6, 40: 5, 50: 5, 60: 5, 70: 7,
           80: 6, 90: 6, 100: 7, 1000: 8, 1000000: 7,
           1000000000: 7}

ans = 0
for i in range(1, N + 1):
    for j in range((len(str(i)) + 2) // 3):
        temp = (i // (10 ** (3 * j))) % 1000
        if j > 0:
            ans += letters[10 ** (3 * j)]
        if temp // 100 > 0:
            ans += letters[temp // 100] + letters[100]
        if 1 <= temp % 100 <= 19:
            ans += (3 if temp > 100 else 0) + letters[temp % 100]
        elif 20 <= temp % 100:
            ans += (3 if temp > 100 else 0) + letters[(temp % 100) // 10 * 10]
            if 1 <= temp % 10:
                ans += letters[temp % 10]
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")