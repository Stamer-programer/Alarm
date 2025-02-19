import time
from playsound import playsound

seconds = int(input("How many time to wait: "))



while seconds:
    timer = f'{seconds:02d}'
    print(timer, end= "\r")
    time.sleep(1)
    seconds -= 1
  
playsound('Your file.wav')

print('playing sound using  playsound')
print("00")  
