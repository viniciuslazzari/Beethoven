import time
import pygame.midi

# initialize the MIDI library and open the default output device
pygame.midi.init()
output = pygame.midi.Output(0)

# set the instrument to acoustic grand piano
output.set_instrument(0)

# send a "note on" message with the MIDI note number 69 and a velocity of 127
output.note_on(67, 127) #SOL
time.sleep(0.5)
output.note_on(67, 127) #SOL
time.sleep(0.5)
output.note_on(65, 127) #FÁ
time.sleep(0.4)
output.note_on(64, 127) #MI
time.sleep(0.7)

output.note_on(67, 127) #SOL
time.sleep(0.5)
output.note_on(67, 127) #SOL
time.sleep(0.5)
output.note_on(65, 127) #FÁ
time.sleep(0.4)
output.note_on(64, 127) #MI
time.sleep(0.7)

output.note_on(67, 127) #SOL
time.sleep(0.5)
output.note_on(69, 127) #LÁ
time.sleep(0.5)
output.note_on(67, 127) #SOL
time.sleep(0.5)
output.note_on(65, 127) #FÁ
time.sleep(0.5)
output.note_on(64, 127) #MI
time.sleep(0.5)
output.note_on(62, 127) #RE
time.sleep(0.7)

output.note_on(62, 127) #RE
time.sleep(0.3)
output.note_on(64, 127) #MI
time.sleep(0.3)
output.note_on(65, 127) #FÁ
time.sleep(0.4)

output.note_on(62, 127) #RE
time.sleep(0.3)
output.note_on(64, 127) #MI
time.sleep(0.3)
output.note_on(65, 127) #FÁ
time.sleep(0.4)

output.note_on(62, 127) #RE
time.sleep(0.3)
output.note_on(64, 127) #MI
time.sleep(0.3)
output.note_on(65, 127) #FÁ
time.sleep(0.5)

output.note_on(67, 127) #SOL
time.sleep(0.5)
output.note_on(69, 127) #LÁ
time.sleep(0.5)
output.note_on(67, 127) #SOL
time.sleep(0.5)
output.note_on(65, 127) #FÁ
time.sleep(0.5)
output.note_on(64, 127) #MI
time.sleep(0.5)
output.note_on(62, 127) #RE
time.sleep(0.5)
output.note_on(60, 127) #DÓ
time.sleep(1)

# send a "note off" message with the MIDI note number 69 and a velocity of 0
output.note_off(60, 0)

# close the MIDI output device and quit the library
del output
pygame.midi.quit()