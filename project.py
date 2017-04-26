from music21 import *
from random import randint
import random
melody = stream.Stream()
noteList = ['C','D','E','F','G','A','B']
song = []
steps = 0
beats = 0
beatCounter = 0
octve = 3
#scale Index used to keep track which note we are adding to the song
scaleIndex = 0
songGenIndex = 0
eighthNote = False
halfNote = False
backEighthNote = False
song.append(noteList[scaleIndex])
def eigthNote(n):
    n.duration.quarterLength = 0.5
    return n
def halfNote(n):
    n.duration.quarterLength = 2
    return n
def repeatNote(n):
    s.repeatAppend(n,2)
def octaveUp(n):
    n.octave +1
    return n
def octaveDown(n):
    n.octave -1
    return n
def stepUp(lst):
    global scaleIndex
    global octve
    global eighthNote
    global halfNote
    global backEighthNote
    scaleIndex += 1
    if scaleIndex < 7:
        n1 = note.Note(noteList[scaleIndex])
        lst.append(n1)
        lst[len(lst) - 1].ocatave = octve
        if(halfNote == True):
            lst[len(lst)-1].duration.quarterLength =  2
            halfNote = False
        if(eighthNote == True):
            lst[len(lst)-1].duration.quarterLength =  0.5
            eighthNote = False
    else:
        octve += 1
        scaleIndex = 0
        n1 = note.Note(noteList[scaleIndex])
        lst.append(n1)
        lst[len(lst) - 1].ocatave = octve
        if(halfNote == True):
            lst[len(lst)-1].duration.quarterLength =  2
            halfNote = False
        if(eighthNote == True):
            lst[len(lst)-1].duration.quarterLength =  0.5
            eighthNote = False
            
def stepDown(lst):
    global scaleIndex
    global octve
    global eighthNote
    global halfNote
    global backEighthNote
    scaleIndex -= 1
    if scaleIndex >= 0:
        n1 = note.Note(noteList[scaleIndex])
        lst.append(n1)
        lst[len(lst) - 1].ocatave = octve
        if(halfNote == True):
            lst[len(lst)-1].duration.quarterLength =  2
            halfNote = False
        if(eighthNote == True):
            lst[len(lst)-1].duration.quarterLength =  0.5
            eighthNote = False
            
    else:
        octve -= 1
        scaleIndex = 6
        n1 = note.Note(noteList[scaleIndex])
        lst.append(n1)
        lst[len(lst) - 1].ocatave = octve
        if(halfNote == True):
            lst[len(lst)-1].duration.quarterLength =  2
            halfNote = False
        if(eighthNote == True):
            lst[len(lst)-1].duration.quarterLength =  0.5
            eighthNote = False
           
def leapUp(lst):
    global scaleIndex
    global octve
    global eighthNote
    global halfNote
    global backEighthNote
    scaleIndex += 2
    if scaleIndex < 7:
        n1 = note.Note(noteList[scaleIndex])
        lst.append(n1)
        lst[len(lst) - 1].ocatave = octve
        if(halfNote == True):
            lst[len(lst)-1].duration.quarterLength =  2
            halfNote = False
        if(eighthNote == True):
            lst[len(lst)-1].duration.quarterLength =  0.5
            eighthNote = False
            
    else:
        octve += 1
        scaleIndex = 0
        n1 = note.Note(noteList[scaleIndex])
        lst.append(n1)
        lst[len(lst) - 1].ocatave = octve
        if(halfNote == True):
            lst[len(lst)-1].duration.quarterLength =  2
            halfNote = False
        if(eighthNote == True):
            lst[len(lst)-1].duration.quarterLength =  0.5
            eighthNote = False
            

def leapDown(lst):
    global scaleIndex
    global octve
    global eighthNote
    global halfNote
    global backEighthNote
    scaleIndex -= 2
    if scaleIndex >= 0:
        n1 = note.Note(noteList[scaleIndex])
        lst.append(n1)
        lst[len(lst) - 1].ocatave = octve
        if(halfNote == True):
            lst[len(lst)-1].duration.quarterLength =  2
            halfNote = False
        if(eighthNote == True):
            lst[len(lst)-1].duration.quarterLength =  0.5
            eighthNote = False
          
    else:
        octve -= 1
        scaleIndex = 6
        n1 = note.Note(noteList[scaleIndex])
        lst.append(n1)
        lst[len(lst) - 1].ocatave = octve
        if(halfNote == True):
            lst[len(lst)-1].duration.quarterLength =  2
            halfNote = False
        if(eighthNote == True):
            lst[len(lst)-1].duration.quarterLength =  0.5
            eighthNote = False
            
            
while songGenIndex < 16:
    x = randint(1, 11)
    y = randint(1, 8)
    if backEighthNote == True:
        eighthNote = True
        if x > 7:
            stepUp(melody)
        elif x >= 0 and x <= 1:
            leapUp(melody)
        elif x >= 2 and x <= 3:
            leapDown(melody)
        else:
            stepDown(melody)
        backEighthNote = False
    else:
        if(y >= 7):
            
            if (songGenIndex <= 2 or songGenIndex >= 14):
                songGenIndex += 2
                eighthNote = False
                halfNote = True
            if(songGenIndex >= 7 and songGenIndex <= 8):
                songGenIndex += 2
                eighthNote = False
                halfNote = True   
        elif(y >= 0 and y <=3):
            eighthNote = True
            halfNote = False
            songGenIndex += 1
            backEighthNote = True
        else:
            eighthNote = False
            halfNote = False
            songGenIndex += 1
        if x > 7:
            stepUp(melody)
        elif x >= 0 and x <= 1:
            leapUp(melody)
        elif x >= 2 and x <= 3:
            leapDown(melody)
        else:
            stepDown(melody)
    
melody.append(note.Note('C4'))
melody[len(melody)-1].duration.quarterLength =  4
melody.show('midi')
