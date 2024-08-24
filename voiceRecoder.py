import sounddevice as sd 
from scipy.io.wavfile import write
import wavio as wv 

#sampling frequency 
freq = 44100

#recording duration
duration = 9

#start to record with the given values
#of duration and sample frequency 
recording = sd.rec(int(duration * freq),
                samplerate=freq, channels=2)

#record audio for thee given number of seconds
sd.wait

#this will convert the numpy array to an audio
#file with the given sampling frequency
write("recording0.wav", freq, recording)

#convert the numpy array to audio file
wv.write("recording1,wav", recording, freq, sampwidth=2)

