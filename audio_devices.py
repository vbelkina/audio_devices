# small tool to help find what audio devices are available and what their index is.

# import speech_recognition as sr  
import pyaudio

r = sr.Recognizer()
r.dynamic_energy_threshold = False
r.energy_threshold = 400

index = 2

p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')

for i in range(0, numdevices):
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))


# # for i in range(0, 7):
# i = 5 
# try:
#     with sr.Microphone(device_index=i) as source:
#         # print("hello there")
#         audio = r.listen(source, timeout=1, phrase_time_limit=1)
# except: 
#     print(f"{i} didn't work")

# # with sr.Microphone(device_index=index) as source: 
# #     audio = r.listen(source)

# try: 
#     result = r.recognize_whisper(audio)
#     print(result)
# except sr.UnknownValueError: 
#     print("whisper could not understand")
# except sr.RequestError as e:  
#     print("whisper error; {0}".format(e))  