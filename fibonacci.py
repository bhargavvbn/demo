
def feb(n):
    a, b = 0, 1
    for i in range(2, n):
        c = a+b
        a, b = b, c
        print(c)


feb(10)