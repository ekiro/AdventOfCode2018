import itertools, sys

with open('inp.txt') as f:
    data = f.readlines()

sq = [
    [0 for _ in range(2000)] for _ in range(2000)
]

for i in range(len(data)):
    id_, _, pos, siz = data[i].split()
    sx, sy = pos.strip(':').split(',')
    x = int(sx)
    y = int(sy)
    sw, sh = siz.strip().split('x')
    w = int(sw)
    h = int(sh)
    
    data[i] = (id_, x, y, w, h)


for d in data:
    id_, x, y, w, h = d
    for i in range(w):
        for j in range(h):
            sq[x + i][y + j] += 1
            
for d in data:
    id_, x, y, w, h = d

    run = True
    for i in range(w):
        for j in range(h):
            if sq[x + i][y + j] != 1:
                run = False
                break
        if not run:
            break
    if run:
        print(id_)
