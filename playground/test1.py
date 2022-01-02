
# n = 10
# for i in range(1, 10):
#     print(i)


def extraLongFactorials(n):
    f = n
    for i in range(1, n):
        f = f * (n-i)
    return f


t = extraLongFactorials(3)
print(t)
