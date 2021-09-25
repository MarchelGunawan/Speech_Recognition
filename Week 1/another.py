import numpy as np
from numpy.fft import fft
import pydub as pd
import matplotlib.pyplot as plt
# from ffprobe import FFProbe

a = pd.AudioSegment.from_ogg('merah_putih.ogg')
y = np.array(a.get_array_of_samples())
yf = fft(y)
plt.plot(np.abs(yf))
plt.show()

