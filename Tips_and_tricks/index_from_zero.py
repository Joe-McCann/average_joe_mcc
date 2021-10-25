import time
lst = [0] * 10_000_000
start = time.perf_counter()

for i in range(len(lst)):
    lst[~i]
print("Time using ~ notation:", time.perf_counter()-start)

start = time.perf_counter()
for i in range(len(lst)):
    lst[-1-i]
print("Time using - notation:", time.perf_counter()-start)


start = time.perf_counter()
for i in range(len(lst)):
    lst[len(lst)-1-i]
print("Time using length backwards:", time.perf_counter()-start)