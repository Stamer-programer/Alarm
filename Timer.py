import time
from playsound import playsound

seconds = int(input("How many time to wait: "))



while seconds:
    timer = f'{seconds:02d}'
    print(timer, end= "\r")
    time.sleep(1)
    seconds -= 1
  
playsound('C:/Users/User/Music/acoustic-guitar-loop-f-91bpm-132687.wav')

print('playing sound using  playsound')
print("00")  