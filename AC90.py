def mul(a, b, p):
    ans = 0
    while b:
        if b & 1:
            ans = (ans + a) % p
        a = a * 2 % p
        b >>= 1
    return ans


x, y, z = int(input()), int(input()), int(input())
print(mul(x, y, z))
