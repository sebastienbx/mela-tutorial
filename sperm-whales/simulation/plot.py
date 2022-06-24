import matplotlib.pyplot as plt
import numpy as np
import scipy.signal


def plot_spectrogram():
    # Sampling frequency
    fs = 20000.

    # Plot spectrogram from input data
    y = np.fromfile("input/8800201M.wav.bin", dtype=np.float32)
    fSpec, tSpec, Sxx = scipy.signal.spectrogram(y, fs, window="hanning", nperseg=128, noverlap=32)
    plt.figure(figsize=(10, 4))
    plt.pcolormesh(tSpec, fSpec, Sxx, shading='gouraud', vmin=1e-2, vmax=1.)
    plt.grid()
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.savefig("input/8800201M-input-spectro.png")
    plt.close()

    # Plot spectrogram computed with MeLa
    y = np.fromfile("output/8800201M.wav.bin.fspectrum_spermWhales.out", dtype=np.float32)
    plt.figure(figsize=(10, 4))
    y = [y[i*65:(i+1)*65] for i in range(0, int(len(y)/65))]
    y = [list(i) for i in zip(*y)]
    plt.pcolormesh(tSpec, fSpec, y, shading='gouraud', vmin=1e1, vmax=1.e3)
    plt.grid()
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.savefig("output/8800201M-output-spectro.png")
    plt.close()


def plot_mean_level():
    # Read mean level file
    y = np.fromfile("output/8800201M.wav.bin.flevel_spermWhales.out", dtype=np.float32)
    plt.plot(y)
    plt.grid()
    plt.savefig("output/8800201M-output-level.png")
    plt.close()


def plot_recorded_clicks():
    # Read sample index file
    si = np.fromfile("output/8800201M.wav.bin.fsampleIndex_spermWhales.out", dtype=np.int32)
    for s in si:
        print(s)
    # Read last 50 ms file
    y = np.fromfile("output/8800201M.wav.bin.flast50ms_spermWhales.out", dtype=np.float32)
    plt.plot(y)
    plt.grid()
    plt.savefig("output/8800201M-output-last50ms.png")
    plt.close()


plot_spectrogram()
#plot_mean_level()
#plot_recorded_clicks()
