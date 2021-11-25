# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 14:41:01 2021

@author: faris
"""

# Metode Simpson 1/3

from math import e # Untuk memanggil bilangan eksponen natural (e)
# Definisikan Fungsi yang akan di integralkan
def f(x):
    return e**x

# Implementasi Metode Simpson 1/3
def simpson13(x0,xn,n):
    # hitung ukuran h/ selisih x1 dan x1+1
    h = (xn - x0) / n
    
    # Tentukan Jumlah
    integration = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        
        if i%2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 4 * f(k)
            
    # Final Integrasi
    integration = integration * h/3
    
    return integration
# Sesi Input
lower_limit = float(input("Masukan Batas Bawah aaerah Integral: "))
upper_limit = float(input("Masukan Batas Atas Daerah Integral: "))
sub_interval =  int(input("Masukan Jumlah Pias: "))

# Memanggil Trapezoidal
result = simpson13(lower_limit, upper_limit, sub_interval)
print("\nHasil Integral dengan Metode Simpson 1/3 : %0.6f" % (result))