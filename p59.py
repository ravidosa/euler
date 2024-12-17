import time, itertools

cipher = open("cipher.txt").read()

t0 = time.time()
cipher = [int(ordd) for ordd in cipher.split(",")]
for key in itertools.product(range(97, 123), repeat=3):
    message = [chr(cipher[i] ^ key[i % 3]) for i in range(len(cipher))]
    if "euler" in "".join(message).lower() and "the" in "".join(message).lower():
        ans = sum([ord(char) for char in message])
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")