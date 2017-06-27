# Your task in this exercise is to write a procedure speak_ICAO() able to translate any text (i.e. any string) into spoken ICAO words. You need to import at least two libraries: os and time. On a mac, you have access to the system TTS (Text-To-Speech) as follows: os.system('say ' + msg), where msg is the string to be spoken. (Under UNIX/Linux and Windows, something similar might exist.) Apart from the text to be spoken, your procedure also needs to accept two additional parameters: a float indicating the length of the pause between each spoken ICAO word, and a float indicating the length of the pause between each word spoken.

import os
from time import sleep
from espeak import espeak


def translate_to_ICAO(input_str, ICAO_dict):
    result = []
    word_closing_list = " !,.?"
    word = []
    
    for char in input_str:
        if char.isalnum():
            word.append(ICAO_dict[char.lower()])
        elif char in word_closing_list:
            result.append(word)
            word = []
    result.append(word)
    return result

def speak_translation(word_list, char_pause_time, word_pause_time):
    for word in word_list:
        for char in word:
            espeak.synth(char)
            sleep(char_pause_time)
        sleep(word_pause_time)

if __name__ == "__main__":
    input_str = raw_input("enter your string   " )
    print "enter timing for ICAO word and natural word"
    input_timings = raw_input().split()
    
    if len(input_timings) < 2:
        print "timing for pause betn word"
        pause_timing = raw_input()
    else:
        pause_timing = input_timings[1]

    char_pause_time = float(input_timings[0])
    word_pause_time =  float(pause_timing)

    d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
         'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
         'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
         's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 
         'x':'x-ray', 'y':'yankee', 'z':'zulu'}

    output_str = translate_to_ICAO(input_str, d)
    speak_translation(output_str, char_pause_time, word_pause_time )
