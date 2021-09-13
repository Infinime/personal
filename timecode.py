now = time.perf_counter();
for x in range(100):
    print(x)
print(time.perf_counter()-now)