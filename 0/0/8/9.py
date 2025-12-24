import time

numerals = open("roman.txt", "r").read()
N = len(numerals)

t0 = time.time()
ans = 0
numerals = numerals.split("\n")
order = "IVXLCDM"
replacements_add = [("IIIII", "V"), ("VV", "X"), ("XXXXX", "L"), ("LL", "C"), ("CCCCC", "D"), ("DD", "M")]
replacements_sub = [("VIIII", "IX"), ("IIII", "IV"), ("LXXXX", "XC"), ("XXXX", "XL"), ("DCCCC", "CM"), ("CCCC", "CD")]
for numeral in numerals:
    minimal = numeral
    for r in replacements_add:
        minimal = minimal.replace(r[0], r[1])
    for r in replacements_sub:
        minimal = minimal.replace(r[0], r[1])
    ans += len(numeral) - len(minimal)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")