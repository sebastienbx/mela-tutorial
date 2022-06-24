import matplotlib.pyplot as plt
import numpy as np
import os

# Sampling frequency
fs = 20

# Read input file
y = np.fromfile("input/2018-11-30T07_31_32.525000.bin", dtype=np.float32)
x = np.arange(0, len(y)/fs, 1./fs)

# Plot input file
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.xlim(0, len(y)/fs)
plt.grid()
plt.savefig("input/input.png")

if os.path.exists("output/2018-11-30T07_31_32.525000.bin.f_Seismic.out"):
    # Read output file
    y = np.fromfile("output/2018-11-30T07_31_32.525000.bin.f_Seismic.out", dtype=np.float32)
    x = np.arange(0, len(y)/fs, 1./fs)

    # Plot output file
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.xlim(0, len(y)/fs)
    plt.grid()
    plt.savefig("output/output.png")

if os.path.exists("output/2018-11-30T07_31_32.525000.bin.f_SeismicDet.out"):
    # Read output file
    y = np.fromfile("output/2018-11-30T07_31_32.525000.bin.f_SeismicDet.out", dtype=np.float32)
    x = np.arange(0, len(y)/fs, 1./fs)

    # Plot output file
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.xlim(0, len(y)/fs)
    plt.grid()
    plt.savefig("output/2018-11-30T07_31_32.525000.bin.f_SeismicDet.out.png")