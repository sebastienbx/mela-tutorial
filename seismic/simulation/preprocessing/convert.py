import matplotlib.pyplot as plt
import numpy as np
import obspy

files = ["1.mseed", "2.sac", "3.wav"]

for file in files:
    st = obspy.read(file)

    data = np.array(st[0].data)
    data.astype(np.int32)
    
    date = st[0].stats.starttime
    fs = st[0].stats.sampling_rate
    print("Start date: " + str(date))
    print("Sampling frequency: " + str(fs))

    y = data.tofile("../Input/" + file + ".bin")
