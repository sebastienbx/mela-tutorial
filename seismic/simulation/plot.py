import matplotlib.pyplot as plt
import numpy as np

# Plot input file
y = np.fromfile("input/2018-11-30T07_31_32.525000.bin", dtype=np.int32)
x = range(len(y))

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.grid()
plt.savefig("input.png")

# Close before new plot
plt.close()

# Plot output file
y = np.fromfile("output/2018-11-30T07_31_32.525000.bin.out", dtype=np.int32)
x = range(len(y))

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.grid()
plt.savefig("output.png")
