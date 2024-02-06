def partitions(n):
    f = [[1] * (n + 1)]
    for i in range(1, n + 1):
        f.append([0])
        for j in range(1, i + 1):
            t = f[i - j][i - j] if j > i - j else f[i - j][j]
            f[i].append(f[i][j - 1] + t)

    return f[n][n]


print(partitions(10))
