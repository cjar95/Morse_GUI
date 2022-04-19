#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from gpiozero import LED
import RPi.GPIO
from tkinter import *
import tkinter.font
from guizero import App, Text, TextBox, PushButton
from time import sleep
RPi.GPIO.setmode(RPi.GPIO.BCM)

##LED PIN SETUP
led1 = LED(21)
led2 = LED(7)
led3 = LED(27)

##MORSE CODE DICTIONARY
Morse_Code_Dictionary = {
    '': '/',
    'A' : '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.---',
    '2': '..--',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': ' ',
    ',': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    ';': '-.-.-.',
    ':': '---...',
    "'": '.----.',
    '-': '-....-',
    '/': '-..-.',
    '(': '-.--.-',
    ')': '-.--.-',
    '_': '..--.-'

}

##GUI DEFINITIONS
win = Tk()
win.title("Text to Morse Converter")
myFont = tkinter.font.Font(family = 'Helvetica', size = 18, weight = "bold")

##LENGTH OF A DOT IS 1 UNIT, SPACE BETWEEN PARTS OF THE SAME LETTER IS 1 UNIT
def dot():
    led1.on(), led2.on(), led3.on()
    sleep(1)
    led1.off(), led2.off(), led3.off()
    sleep(1)

##LENGTH OF A DASH IS 3 UNITS
def dash():
    led1.on(), led2.on(), led3.on()
    sleep(3)
    led1.off(), led2.off(), led3.off()
    sleep(1)
    
##CONVERTS INPUT TO MORSE
def convert():
    input = user_text.get()
    for letter in input:
        for symbol in Morse_Code_Dictionary[letter.upper()]:
            if symbol == '-':
                dash()
            elif symbol == '.':
                dot()
            else:
                sleep(3)##SPACE BETWEEN LETTERS IS 3 UNITS

##USER DEFINITIONS
user_text = Entry(win, font = myFont, width = 30, bg= 'bisque2')
user_text.grid (row = 0, column = 0)

##WIDGETS
button = Button(win, text = 'Convert Your Text (12 characters max)', font = myFont, command = convert, bg = 'bisque2', height = 1, width = 30) 
button.grid(row = 1, column = 0)

