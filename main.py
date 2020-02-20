import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sys import argv

if len(argv) > 1:
    file_name = argv[1]
else:
    file_name = input('Enter csv file name: ')

with open(file_name) as f:
    data = pd.read_csv(f)

cols = data.columns
signal_count = data.shape[1] - 1
N = 1000

t = data.loc[:, cols[0]]
Ts = (t.loc[t.size-1] - t[0])/t.size
f = np.fft.rfftfreq(N, Ts)

for i in range(signal_count):
    y = data.loc[:, cols[1+i]]

    A = np.fft.rfft(y, N)

    plt.figure(i)

    plt.subplot(211)
    plt.plot(t, y, linewidth=0.5)

    plt.subplot(212)
    plt.plot(f, np.abs(A), linewidth=0.5)
    plt.xscale('log')

plt.show()

