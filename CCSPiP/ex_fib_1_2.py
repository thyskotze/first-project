# Python fibornacci code with recursive function

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)

nterms = 12

# checking if the number of terms is valid

if nterms <= 0:
    print("please enter a positive number")
else:
    print("Fib code is: ")
    for i in range(nterms):
        print(recur_fibo(i))