def power(a: int, b: int, p: int) -> int:
    ans = 1 % p
    while b:
        if b & 1:
            ans = ans * a % p
        a = a * a % p
        b = b >> 1
    return ans


x, y, z = input().split()
x, y, z = int(x), int(y), int(z)
print(power(x, y, z))
