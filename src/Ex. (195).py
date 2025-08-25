def stat(a):
    n = len(a)
    b = 0
    e = 0
    r = [0, 0, 0]  # AV, SD, CV

    for j in range(n):
        b += a[j]

    r[0] = b / n

    for j in range(n):
        e += (a[j] - r[0]) ** 2

    r[1] = (e / (n - 1)) ** 0.5
    r[2] = r[1] / r[0]

    return r

a = [5, 1, 8, 4, 6, 2, 8, 9]
b = stat(a)
print(b)

'''
Ex. (195) - Average, standard deviation and coefficient of variation.

References

Paul A. Gagniuc. Coding Examples from Simple to Complex - Applications in Python, Springer, 2024, pp. 1-245.
Paul A. Gagniuc. Coding Examples from Simple to Complex - Applications in MATLAB, Springer, 2024, pp. 1-255.
Paul A. Gagniuc. Coding Examples from Simple to Complex - Applications in Javascript, Springer, 2024, pp. 1-240.

'''