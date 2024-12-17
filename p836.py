import time

words = "affine plane redically integral local field open oriented line section jacobian orthogonal kernel embedding"

t0 = time.time()
ans = "".join([word[0] for word in words.split(" ")])
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")