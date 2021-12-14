import numpy as np
from numpy.fft import fft,ifft
import argparse
import matplotlib.pyplot as plt
import librosa
import matplotlib
from scipy import signal


# parser = argparse.ArgumentParser()

# parser.add_argument('--sweep_rec', type=str,
#                         help='provide the path to the recorded wav file of the response of the speaker to the sweep signal (output)')

# parser.add_argument('--sweep', type=str,
#                         help='provide the path to the sweep wav file that your speaker will play (input) ')       

# parser.add_argument('--win_dur', type=float, default=0.01,
#                         help='provide the window duration in time (seconds) in order to window the impulse response (avoding distortion related to early reflactions) ')                                        




# args, _ = parser.parse_known_args()

sweep = str( input( 'provide the path to the sweep wav file that your speaker will play (input) ' ) )
sweep_rec = str(input("provide the path to the recorded wav file of the response of the speaker to the sweep signal (output)"))
win_dur = str(input( 'provide the window duration in time (seconds) in order to window the impulse response (avoding distortion related to early reflactions) ' ) )

#load the sweep sine stimuli
x,s=librosa.load(sweep, sr=44100)
#load the recorded response of the filter(speaker) to the swept sine stimuli
x_rec,s=librosa.load(sweep_rec, sr=44100)


#get inverse filter for deconv:
f_x = fft(x)
inv_f_x = 1/f_x
x_inv = np.real(ifft(inv_f_x))

#Calcultaing the impulse response throughout deconvolution:
h_est = np.convolve(x_inv,x_rec)


#WINDOWING OF THE IMPULSE RESPONSE (AVOIDING REFLEXIONS)
time2ind = lambda time,s : time*s   
max_ind= np.argmax(h_est)
start = max_ind
win_dur = int(time2ind(win_dur,s))
end = start + win_dur
z = np.zeros(len(h_est))
window = np.roll(signal.tukey(win_dur*2) , win_dur )[:win_dur]
z[start:int(end)]=window*max(h_est)





#PLOTTING FREQ-IMP RESPONSES (the windowed response)
tmp = (h_est*z)[max_ind:end]
fk = np.arange(len(tmp))*(s/len(tmp))
f_h_est = 20*np.log10(np.abs(fft(tmp))[1:len(tmp)//2]/2e-5)


plt.semilogx(fk[1:len(fk)//2],f_h_est)


locs=np.arange(-10,170,10)
plt.yticks(locs)


loc = np.array([  100.,  1000., 10000.,20000.])
labels = [ matplotlib.pyplot.Text(100.0, 0, '$\\mathdefault{100}$') , matplotlib.pyplot.Text(1000.0, 0, '$\\mathdefault{1000}$') , matplotlib.pyplot.Text(10000.0, 0, '$\\mathdefault{10000}$'), matplotlib.pyplot.Text(20000.0, 0, '$\\mathdefault{20000}$')  ]
plt.xticks(loc,labels)

plt.grid(True, which="both", ls="-")
plt.ylabel("dB-SPL")
plt.xlabel("Frequency [Hz]")
plt.title("Frequency Response")

plt.figure()


plt.plot(h_est)
plt.title("Impulse Response")
plt.plot(z)
plt.legend(['Impulse Response', 'Tukey Window' ])

plt.show()


