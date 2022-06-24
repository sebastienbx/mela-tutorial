import numpy as np
import obspy
import scipy.signal

files = ["8800201M.wav"]
decimation_factor = 4

for file in files:
    st = obspy.read(file)

    data = np.array(st[0].data, np.int32)
    data = data.astype(np.float32)

    data = scipy.signal.decimate(data, decimation_factor)

    date = st[0].stats.starttime
    fs = st[0].stats.sampling_rate/decimation_factor

    print("Start date: " + str(date))
    print("Sampling frequency: " + str(fs))

    y = data.tofile(file + ".bin")
