
def feb(n):
    a, b = 0, 1
    for i in range(2, n):
        c = a+b
        a, b = b, c
        print(c)

lst = [10,20,50,60]
fib(lst)
