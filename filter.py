import speech_recognition as sr

from scipy.io import wavfile
import noisereduce as nr
import soundfile as sf
data, samplerate = sf.read('Noisy.wav')

import noisereduce as nr
# load data
rate, data = wavfile.read("Noisy.wav")
# select section of data that is noise
noisy_part = data[10000:15000]
# perform noise reduction
reduced_noise = nr.reduce_noise(audio_clip=data, noise_clip=noisy_part, verbose=True)

r = sr.Recognizer()

audio = 'Noisy.wav'

with sr.AudioFile(audio) as source:
    audio = r.record(source)
    print ('Done!')

try:
    text = r.recognize_google(audio)
    print (text)
    
except Exception as e:
    print (e)
