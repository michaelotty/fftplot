#!/usr/bin/python

import argparse

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description='Plot the signal inputted to the script')
    parser.add_argument('-f', '--file', required=True, help='Filename of data to input')
    types = {'csv', 'excel', 'pickle'}
    parser.add_argument('-t', '--type', help='Type of file input', default='csv', choices=types)
    parser.add_argument('-n', '--fftsize', type=int, help='Length of fft, Default: 512', default=512)
    args = vars(parser.parse_args())

    if args['type'] == 'csv':
        data = pd.read_csv(args['file'])
    elif args['type'] == 'excel':
        data = pd.read_excel(args['file'])
    elif args['type'] == 'pickle':
        data = pd.read_pickle(args['file'])
    else:
        data = None

    cols = data.columns
    signal_count = data.shape[1] - 1
    n = args['fftsize']

    t = data.loc[:, cols[0]]
    t_s = (t.loc[t.size - 1] - t[0]) / t.size
    f = np.fft.rfftfreq(n, t_s)

    for i in range(signal_count):
        y = data.loc[:, cols[1 + i]]

        a = np.fft.rfft(y, n)

        plt.figure(i)

        plt.subplot(211)
        plt.plot(t, y, linewidth=0.5)
        plt.title(cols[i + 1])
        plt.xlabel('t (s)')
        plt.ylabel('Amplitude')

        plt.subplot(212)
        plt.plot(f, np.abs(a), linewidth=0.5)
        plt.xscale('log')
        plt.xlabel('f (Hz)')
        plt.ylabel('Amplitude')

    plt.show()


if __name__ == '__main__':
    main()
