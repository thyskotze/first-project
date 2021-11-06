#fin(n) = fib(n-1) + fib(n-2)

def fib1(n: int) -> int:
    return fib1(n-1) + fib1(n-2)

#print(fib1(2))
if __name__ =="__main__":
    print(fib1(5))