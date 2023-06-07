# -*- coding: utf-8 -*-
"""
Created on Mon May  8 01:59:27 2023

@author: Dell
"""

import sympy
exp = sympy.exp
j2pi = sympy.I*2*sympy.pi
def S(N):
 return sum(c(n)*exp(j2pi*n*t/T) for n in range(-N, N+1)).expand(complex=True).simplify()
def c(n):
 return (sympy.integrate(f(t)*exp((-j2pi * n * t)/T),(t, t0, t0 + T))/T)
a = sympy.Symbol('a', positive=True)
def f(t):
 return t
T = 10
t0 = -5
t = sympy.Symbol('t', real=True)
N = 5
analytic_app = S(N).expand()
interval = (t, t0-T, t0+2*T)
p1 = sympy.plot(f(t), (t, t0, t0+T), title='Fourier Series for the first '+str(N)+' harmonics',
show=False)
p2 = sympy.plot(analytic_app, interval, show=False)
p2[0].line_color = 'red'
p1.extend(p2)
p1.show()
print(sympy.N(analytic_app))