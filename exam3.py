n = int(input())
m = int(input())

found = False

for banana in range(1, n):
    for diamond in range(1, n):
        for deer in range(1, n):
            if banana + 3 * diamond + 2 * deer == m:
                print(f"{banana} + 3×{diamond} + 2×{deer} = {m}")
                found = True

if not found:
    print("При заданных n и m решений не существует.")
