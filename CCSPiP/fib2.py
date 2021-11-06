def fib2(n: int) -> int:
    if n < 2: #base case
        return n
    return fib2(n - 2) + fib2(n - 1) #recuresive case

if __name__ == "__main__":
    print(fib2(2))
    print(fib2(6))