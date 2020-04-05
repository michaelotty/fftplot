#!/usr/bin/python

import numpy as np
import pandas as pd

fs = 40e3  # Hz
T = 2.0
t = np.linspace(0.0, T, round(T*fs))
f = 100.0  # Hz
y = np.sin(2*np.pi*f*t)
data = np.array([t, y]).T
out_data = pd.DataFrame(data, columns=('t (s)', 'sin(t)'))

out_data.to_pickle('sin.pkl')

