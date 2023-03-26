import pygame.midi
import time

class Player:
    def __init__(self):
        self.notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        self.sounds = ["sound1.wav", "sound2.wav", "sound3.wav"]
        self.instrument = 0
        self.octave = 4
        self.volume = 127
        self.bpm = 120
 
    def note_exists(self, note):
        return note in self.notes

    def play_note(self, text, instrument, octave, volume, bpm):

        pygame.midi.init()
        output = pygame.midi.Output(0)
        escala = 12
        bpm_base = 60
        nota_atual = "C#"
        volume_aux = int(volume/2)

        for note in text:
            print(note)
            if not self.note_exists(note):
                final_note = (octave * escala) + (self.notes.index(nota_atual))
                volume_atual = volume_aux

            else :
                final_note = (octave * escala) + (self.notes.index(note))
                nota_atual = note
                volume_atual = volume
                
            # set the instrument to acoustic grand piano
            output.set_instrument(instrument)
            output.note_on(final_note, volume_atual)
            time.sleep(bpm_base/bpm)
            
        # send a "note off" message with the MIDI note number 69 and a velocity of 0
        output.note_off(final_note, 0)

        # close the MIDI output device and quit the library
        del output
        pygame.midi.quit()