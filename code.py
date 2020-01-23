import time
from adafruit_circuitplayground import cp
from random import randint

cp.pixels.brightness = 0.3
powerRangersCommunicatorMelody = [
("c#8", 1),(None, 2),("c#8", 1),(None, 2),("b7", 1),("c#8", 1),(None, 2),("e8", 1),(None, 2),("c#8", 1)
]
def clear_neopixels():
    cp.pixels.fill((0, 0, 0))

def light_random_neopixel():
    clear_neopixels()
    cp.pixels[randint(0,9)] = (randint(0,255), randint(0,255), randint(0,255))

def note(name):
    octave = int(name[-1])
    PITCHES = "c,c#,d,d#,e,f,f#,g,g#,a,a#,b".split(",")
    pitch = PITCHES.index(name[:-1].lower())
    sound = 440 * 2 ** ((octave - 4) + (pitch - 9) / 12.)
    sound = int(round(sound))
    return sound

def play_melody(melody):
    for (notename, eigths) in melody:
       length = eigths * 0.1
       if notename:
         light_random_neopixel()
         cp.play_tone(note(notename), length)
       else:
         time.sleep(length)

while True:
    if cp.button_a:
        play_melody(powerRangersCommunicatorMelody)
    else:
        clear_neopixels()
