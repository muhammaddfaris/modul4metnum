# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 15:04:40 2021
@author: Muhammad Faris 202010225262 TF3A6 
"""
# Metode Simpson 3/8

from math import e #Untuk Memanggil bilangan eksponen natural (e)

# Definisikan fungsi yang akan diintegralkan
def f(x):
    return e**x

# Implementasi Metode Simpson 3/8
def simpson38(x0,xn,n):
    # hitung ukuran h/ selisih xi dan xi+1
    h = (xn - x0) / n

    # Tentukan Jumlah
    integration = f(x0) + f(xn)

    for i in range(1,n):
        k = x0 + i*h

        if i%2 == 0:
            integration  = integration + 2 * f(k)
        else:
            integration = integration + 3 * f(k)
    # Finding final integration value
    integration = integration * 3 * h / 8

    return integration

# Sesi Input
lower_limit = float(input("masukan Batas Bawah Daerah Integral: "))
upper_limit = float(input("Masukan Batas Atas Daerah Integral: "))
sub_interval = int(input("Masukan Jumlah Pias: "))

#Memanggil Simpson3/8
result = simpson38(lower_limit, upper_limit, sub_interval)
print("\nHasil Integral dengan Metode Simpson 3/8: %0.6f" % (result) )