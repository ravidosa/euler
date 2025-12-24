import time, random

N = 4

def dice_roll(N):
    r1, r2 = random.randrange(1, N + 1), random.randrange(1, N + 1)
    if r1 == r2:
        r3, r4 = random.randrange(1, N + 1), random.randrange(1, N + 1)
        if r3 == r4:
            r5, r6 = random.randrange(1, N + 1), random.randrange(1, N + 1)
            if r5 == r6:
                return 0
            else:
                return r1 + r2 + r3 + r4 + r5 + r6
        else:
            return r1 + r2 + r3 + r4
    else:
        return r1 + r2

t0 = time.time()
rolls = 1000000
squares = ["GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3", "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3", "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3", "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"]
land = {square: 0 for square in squares}
square = 0
cc, ch = 0, 0
for _ in range(rolls):
    roll = dice_roll(N)
    if roll == 0:
        land["JAIL"] += 1
        square = squares.index("JAIL")
    else:
        square = (square + roll) % len(squares)
        if squares[square] == "G2J":
            land["JAIL"] += 1
            square = squares.index("JAIL")
        if squares[square][:2] == "CC":
            if cc == 0:
                land["GO"] += 1
                square = squares.index("GO")
            elif cc == 1:
                land["JAIL"] += 1
                square = squares.index("JAIL")
            else:
                land[squares[square]] += 1
            cc = (cc + 1) % 16
        elif squares[square][:2] == "CH":
            if ch == 0:
                land["GO"] += 1
                square = squares.index("GO")
            elif ch == 1:
                land["JAIL"] += 1
                square = squares.index("JAIL")
            elif ch == 2:
                land["C1"] += 1
                square = squares.index("C1")
            elif ch == 3:
                land["E3"] += 1
                square = squares.index("E3")
            elif ch == 4:
                land["H2"] += 1
                square = squares.index("H2")
            elif ch == 5:
                land["R1"] += 1
                square = squares.index("R1")
            elif ch == 6 or ch == 7:
                while squares[square][0] != "R":
                    square = (square + 1) % len(squares)
                land[squares[square]] += 1
            elif ch == 8:
                while squares[square][0] != "U":
                    square = (square + 1) % len(squares)
                land[squares[square]] += 1
            elif ch == 9:
                square = (square - 3) % len(squares)
                if squares[square][:2] == "CC":
                    if cc == 0:
                        land["GO"] += 1
                        square = squares.index("GO")
                    elif cc == 1:
                        land["JAIL"] += 1
                        square = squares.index("JAIL")
                    else:
                        land[squares[square]] += 1
                    cc = (cc + 1) % 16
            else:
                land[squares[square]] += 1
            ch = (ch + 1) % 16
        else:
            land[squares[square]] += 1
ans = "".join(map(lambda s: str(squares.index(s)).zfill(2), sorted(land, key=lambda s: land[s], reverse=True)[:3]))
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")