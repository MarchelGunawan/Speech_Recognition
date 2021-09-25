import numpy as np
from numpy.fft import fft
import pydub 
import matplotlib.pyplot as plt
from pathlib import Path

def Sort(sub_li):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of 
    # sublist lambda has been used
    sub_li.sort(key = lambda x: x[1])
    return sub_li

song = Path('merah_putih.ogg')
a = pydub.AudioSegment.from_ogg(song)
y = np.array(a.get_array_of_samples())

plt.plot(y)
# plt.show()

print(f"frame rate : {a.frame_rate}")
print(f"array of y : {y}")

yf = fft(y)
plt.plot(np.abs(yf))
# plt.show()

print(f"lenght of y : {len(y)}")

f = []
w = 128
for i in range(round(len(y)/w)-1):
    f.append(y[i*w:(i+1)*w-1])
print(f"length of f : {len(f)}")

# print list of f[0][i]
print("Array of f : ")
for i in range(w-1):
    print({i,f[0][i]})

# print the correlation 
print(f"The corelation :\n{np.corrcoef(f[0],f[1])}")