mem = {0: 0, 1: 1}

def fib_mem(n): 
    if n in mem:
        return mem[n]
    else:
        mem[n] = fib_mem(n - 1) + fib_mem(n - 2)
        return mem[n]
    



print(fib_mem(200))