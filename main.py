import matplotlib.pyplot as plt
import numpy as np
import qiskit as qi
import time



b = input("Podaj liczbe: ")


xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.plot(ypoints, xpoints)
plt.plot([6,250], [250,6])
plt.show()

def silnia(a):
    temp = 1
    for i in range(a+1):
        if i!=0:
         temp = temp*i
    return(temp)


def fibo(n):
    temp = ""
    if n==0: return 0
    if n==1: return 1
    if n>1:
        a, b = 1,1
        for i in range(n-1):
            temp = temp + str(str(a) + " ")
            b += a
            a = b - a
            
    return a



def silnia_rek(n):
    if n==1:
        return 1
    return n*silnia_rek(n-1)

def fibo_rek(n):
    if n < 0: raise NotImplementedError
    if n == 0: return 1
    if n == 1: return 1
    return fibo_rek(n-1) * fibo_rek(n-2)

L_rek = []
L_it = []
for i in range(36):
    t1 = time.time()
    fibo_rek(i)
    t2= time.time()
    L_rek.append(t2-t1)
    t1 = time.time()
    fibo(i)
    t2= time.time()
    L_it.append(t2-t1)

plt.plot(range(36), L_rek, "b+", label="rekurencja")
plt.plot(range(36), L_it, "r+", label="iteracja")
plt.legend()
plt.show()
