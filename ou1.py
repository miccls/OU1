"""
Solutions to module 1
Student: Martin Svärdsjö
Mail: martincsvardsjo@gmail.com
Reviewed by: Jesper Munkeby
Reviewed date: 6 - 4 - 2021
"""


import random
import time
import math

def power(x, n):         # Optional
    if n < 0:
        return power(x, n + 1)*(1/x)
    elif n > 0:
        return power(x, n - 1)*(x)
    else:
        return 1

def multiply(m, n):      # Compulsory
    return m + multiply(m, n - 1) if n != 0 else 0


def divide(t, n):        # Optional
    pass


def harmonic(n):         # Compulsory
    return 1/n + harmonic(n - 1) if n > 1 else 1


def digit_sum(x):        # Optional
    if x < 1:
        return 0
    else:
        return digit_sum(x // 10) + x % 10


def get_binary(x):       # Optional
    if (x/2)**2 < 1:
        return str(x)
    else:
        return str(get_binary(x//2)) + str(x%2)


def reverse(s):          # Optional
    if len(s) <= 1:
        return s
    else:
        mid = len(s)//2
        return reverse(s[mid:]) + reverse(s[:mid])


def largest(a):          # Compulsory
    if len(a) == 1:
        return a[0]
    lgst = largest(a[1:])
    return lgst if lgst > a[0] else a[0]


def count(x, s):         # Compulsory

    if len(s) == 0:
        return 0
    elif type(s[0]) is list:
        if s[0] != x:
            cnt = count(x, s[0])
        else:
            cnt = 1
    else:
        cnt = 1 if s[0] == x else 0
    return cnt + count(x, s[1:])

    # if len(s) == 0:
    #     return 0
    # else:
    #     cnt = 1 if s[0] == x else 0
    # return cnt + count(x, s[1:])

def zippa(l1, l2):       # Compulsory
    if len(l1) == 0 or len(l2) == 0:
        return [*l1, *l2]
    else:
        return [l1[0], *zippa(l2, l1[1:])]


def bricklek(f, t, h, n): # Compulsory
    '''Tanke bakom funktionen.
    Ge översiktlig struktur för hur allt ska gå
    till: Flytta n-1 till h, flytta sedan en till
    t och sedan n-1 till t. Om det är mer än 1 bricka
    som ska flyttas gör man detta, annars flyttar man brickan direkt.
    '''
    # Basfallet. Om det bara är en så vet vi vad vi ska göra!
    if n == 1: return [f'{f}->{t}',]
    instruction = bricklek(f, h, t, n-1)
    instruction += [f'{f}->{t}']
    return instruction + bricklek(h, t, f, n-1)

def makeList(s):
    if len(s) == 1:
        return [float(s)]
    else:
        return float(s[0]), *makeList(s[2:])



def timer(func):
    def wrap(a):
        start = time.perf_counter()
        func(a)
        return time.perf_counter() - start
    return wrap

memory = {0:0, 1:1}
#@timer
def  fib_mem(n):
    if n < 0:
        return 0
    elif n in  memory:
        return  memory[n]
    else:
        memory[n] = fib_mem(n-1) + fib_mem(n-2)
        return  memory[n]

def main():
    """ Demonstates my implementations """
    # Write your demonstration code here
    #print(multiply(2, 3))
    print(makeList('1,2,3,4,5'))
    #print(harmonic(10))

    #print(largest([1, 3, 5]))

    #print(count(1, [1, 3, [1, 3]]))

    #print(zippa([2, 4, 6],[1, 3, 5]))
    
    #print(bricklek('A', 'B', 'C', 5))

    #print(fib_mem(99))

if __name__ == "__main__":
    main()
    
####################################################    
    
"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 15: Time for bricklek with 50 bricks:
  
  It would take 2^50 - 1 seconds which is equal to approx 36 million years.
  
  
  
  
  Exercise 16: Time for Fibonacci:
  a)
def timer(func):
    def wrap(a):
        start = time.time()
        func(a)
        return time.time() - start
    return wrap


  @timer
    def fib(a):
        if a < 2:
            return a
        else:
            return fib(a - 1) + fib(a - 2)

    from math import log
    summa = 0
    for i in range(500):
        summa += log(fib(10)/fib(5),1.618034)
    print(summa/500)
  
  Ger ca, 5 när man kör detta. Måste räknas som verifiering tycker jag.
  
  b)
  Då använder vi den teoretiska formeln.
  Jag räknar ut tiden för fib(20) genom att köra programmet,  t_20 = c * 1.618^20 --> t_50 = t_20 * 1.618^30 = c * 1.618^20 * 1.618^30
  sedan så multiplicerar jag med (1.618)**30 och -||-**80 och får 
  resultaten 2.11 år respektive 45398 biljoner år för att räkna ut fib(100) med rekursion.
  Exercise 19: Comparison sorting methods:
  
  
  
  
  
  Exercise 20: Comparison Theta(n) and Theta(n log n)
  (och 19).
  19:
  Tiden det tar är av storleksordningen 1 sek * 10^6 eller 1 sek* 10^9 repsektive
  1 sek * 10^6*log(10^6, 2), 1 sek * 10^9*log(10^9, 2)   
  20:

  Detta räknas lätt ut algebraiskt. 
   B med n = 10 ger --> 1 = c * 10 * log(10) --> c = 1/10
   n = 1/10 * n * log(n) --> n = 10^10 (tio miljarder innan A är mer effektiv). 
  
  
  
  
  






"""