# nTerns = int(input("please enter the amount of numbers: "))
#
# n1, n2 = 0, 1
# counter = 0
#
# if nTerns <= 1:
#     print("the Fibonacci code is: ", nTerns)
#     print(n1)
# else:
#     print("the Fibonacci code is: ")
#     while counter < nTerns:
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         counter += 1
#         print(nth)

cache = {0: 0, 1: 1}

def fib(n):
    if n in cache:
        return cache[n]
    cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]


print([fib(n) for n in range(15)])
