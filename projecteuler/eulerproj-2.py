fnumbers = [1, 2]
while fnumbers[-1] <= 4000000:
    fnumbers.append(fnumbers[-1] + fnumbers[-2])
y = 0
for x in fnumbers:
    if x % 2 != 0:
        fnumbers.remove(x)
    y = y + x
print(y)
#solved
