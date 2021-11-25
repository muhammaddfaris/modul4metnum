# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 15:56:51 2021

@author: Muhammad faris 202010225262 TF3A6
"""
# Metode Trapezoidal

from math import e #Untuk memanggil bilangan eksponen natural (e)

# Definiskan fungsi yang akan diintegralkan
def f(x):
    return e**2*x

# Implementasi Metode Trapezoidal
def trapezoidal(x0,xn,n):
    # hitung ukuran h/ selisih xi dan xi+1
    h = (xn - x0) / n
    
    # Tentukan Jumlah
    integration = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        integration = integration + 2 * f(k)
        
    # Final Integrasi
    integration = integration * h/2
        
    return integration
     
# Sesi Input
lower_limit = float(input("Masukan Batas Bawah Daerah Integral: "))
upper_limit = float(input("Masukan Batas Atas Daerah Integral: "))
sub_interval = int(input("Masukan Jumlah Pias: "))

# Memanggil Trapezoidal
result = trapezoidal(lower_limit, upper_limit, sub_interval)
print("\nHasil Integral dengan Metode Trapezoidal : %0.6f" % (result) )