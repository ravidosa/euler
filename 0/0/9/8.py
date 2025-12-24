import time, math

words = open("words.txt", "r").read()
N = len(words)

t0 = time.time()
ans = 0
words = words[1:-1].split("\",\"")
anagrams = {}
for word in words:
    sort = "".join(sorted(word))
    anagrams[sort] = anagrams.get(sort, []) + [word]
filtered = {k: v for (k, v) in anagrams.items() if len(v) >= 2}
maxlen = len(max(filtered, key=len))
squares = [i ** 2 for i in range(math.floor(math.sqrt(10 ** maxlen)), 0, -1)]
for pair in filtered.values():
    for square in squares:
        if len(str(square)) == len(pair[0]):
            repl = {}
            for i in range(len(pair[0])):
                repl[int(str(square)[i])] = repl.get(int(str(square)[i]), []) + [pair[0][i]]
            if all(map(lambda i: len(repl[i]) <= 1, repl)):
                anasquare = pair[1]
                for rep in repl:
                    anasquare = anasquare.replace(repl[rep][0], str(rep))
                anasquare = int(anasquare)
                if len(str(anasquare)) == len(pair[1]) and math.sqrt(anasquare).is_integer():
                    ans = max(ans, square, anasquare)
t1 = time.time()
print(ans, str((t1 - t0) * 1000), "ms")