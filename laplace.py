# -*- coding: utf-8 -*-
"""
Created on Mon May  8 00:21:52 2023

@author: Dell
"""

import sympy as sp
t, s = sp.symbols("t,s")
x=sp.inverse_laplace_transform((2*s**2 + s)/(s**2 + 4), s, t)
print('x(t)=',x)

a=t*(sp.Heaviside(t)- sp.Heaviside(t-10))
y=sp.laplace_transform(a, t, s)
print('y(t)=', y)
