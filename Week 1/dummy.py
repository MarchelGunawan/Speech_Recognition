from os import path
import numpy as np
from numpy.fft import fft
import pydub as pd
import matplotlib.pyplot as plt
from pathlib import Path
# from ffprobe import FFProbe
song = Path('merah-putih.mp3')
a = pd.AudioSegment.from_mp3(song)
y = np.array(a.get_array_of_samples())

yf = fft(y)
plt.plot(y)
plt.show()
plt.plot(np.abs(yf))
plt.show()
