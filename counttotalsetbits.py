def nearest2power(n):
    c = 0
    i = 0
    while (1 << i) <= n:
        c += 1
        i += 1
    return c - 1

def countSetBits(n):
    if n == 0:
        return 0
    d = nearest2power(n)
    cnt = (d * ((2 ** d) // 2)) + 1 + (n - (2 ** d)) + countSetBits(n - (2 ** d))
    return cnt


n = int(input())
print(countSetBits(n))

