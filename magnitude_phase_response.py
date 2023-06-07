# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 04:49:03 2023

@author: Dell
"""

import numpy 
import matplotlib.pyplot as plt
from ipywidgets import interact
omega = numpy.logspace(1, 4, 100000); s = 1j*omega
def annotated_bode(ax_gain, ax_phase, H, K, tau1, tau2, order):
# Gain part
 ax_gain.semilogx(omega, 20*numpy.log10(numpy.abs(H)))
 ax_gain.axhline(20*numpy.log10(K)+20*order*numpy.log10(1/tau1), color='grey', linestyle=':')
 ax_gain.set_ylim([1e-1, 1e+1])
 ax_gain.set_ylabel('|H(w)|')
# Phase part
 ax_phase.axhline(0, color='grey', linestyle='--')
 ax_phase.semilogx(omega, numpy.unwrap(numpy.angle(H, deg=True)))
 ax_phase.axhline(-numpy.pi/2*order, color='grey',linestyle='--')
 ax_phase.set_ylim([-270, 180])
 ax_phase.set_ylabel(r'$\angle H(w)$')
def plotresponse(order, tau1, tau2, K):
 H = K * s**order/(((tau1*s + 1)**order)*(tau2*s +1)**order)
 fig, [ax_gain, ax_phase] = plt.subplots(2, 1)
 annotated_bode(ax_gain, ax_phase, H, K, tau1, tau2, order)
interact(plotresponse, order=2, tau1=0.01, tau2=0.000333, K=178e-6)
# magnitude and phase response