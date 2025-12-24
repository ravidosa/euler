import time
from utils.probability import compare_hand

hands = open("poker.txt", "r").read()
N = len(hands)

t0 = time.time()
hands = hands.split("\n")
ans = sum(map(lambda h: compare_hand(h[:14], h[15:]) == 1, hands))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")