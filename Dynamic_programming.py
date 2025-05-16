###exemple one using fibonancy suite

def fib(n):
    if n <= 1 :
        return 1 
    return fib (n-1) + fib (n-2)

def dynamicfib (n , numb = {}):
    if n <= 1 :
        return 1
    if n not in numb:
        numb[n] = dynamicfib(n-1, numb) + dynamicfib(n-2, numb)

