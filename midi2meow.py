#!/usr/bin/env python3

import mido
from sys import stderr, stdout
from time import sleep

def pitch_to_command(freq, phoneme):
    return f'[:rate 600 _<0,{freq}>{phoneme}<400,{freq}>]'

def midi_to_pitch(note):
    return 440 * (2**((note-69)/12))

last_note = -1
if __name__ == '__main__':
    print('[:phoneme on]')
    #print('[:phoneme on]', file=stderr)
    stdout.flush()
    inport = mido.open_input('Midi Through:Midi Through Port-0 14:0')
    for msg in inport:
        if msg.type == 'note_on':
            last_note = msg.note
            freq = midi_to_pitch(msg.note)
            print(pitch_to_command(int(freq), 'miyaw'))
            #print(pitch_to_command(int(freq), 'meow'), file=stderr)
            stdout.flush()
        elif msg.type == 'note_off' and msg.note == last_note:
            print('') # newline to stop current note
            #print('', file=stderr) # newline to stop current note
            stdout.flush()
