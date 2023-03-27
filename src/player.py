import pygame.midi
import time
from midiutil import MIDIFile

class Player:
    def __init__(self):
        self.notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        self.sounds = ["sound1.wav", "sound2.wav", "sound3.wav"]
        self.instrument = 0
        self.octave = 4
        self.volume = 127
        self.bpm = 120
        self.track = 0
        self.channel = 0
        self.time = 0
        self.duration = 1
 
    def note_exists(self, note):
        return note in self.notes

    def play_note(self, text, instrument, octave, volume, bpm, output_file):

        pygame.midi.init()
        output = pygame.midi.Output(0)
        escala = 12
        bpm_base = 60
        nota_atual = "C"
        repete = ["a", "b", "c", "d", "e", "f", "g"]

        midi_file = MIDIFile(1)

        midi_file.addTempo(self.track, self.time, self.bpm)

        for note in text:
            print(note)
            if not self.note_exists(note):
                #if note in repete:
                    #if not nota_atual in repete:
                        final_note = (octave * escala) + (self.notes.index(nota_atual))

            else :
                final_note = (octave * escala) + (self.notes.index(note))
                nota_atual = note
                volume_atual = volume
                
            # set the instrument to acoustic grand piano
            output.set_instrument(instrument)
            output.note_on(final_note, volume_atual)
            time.sleep(bpm_base/bpm)

            midi_file.addNote(
                self.track, self.channel, final_note,
                self.time, self.duration, volume_atual
            )

            self.time += 1

        with open(output_file, "wb") as output_file:
            midi_file.writeFile(output_file)
            
        # send a "note off" message with the MIDI note number 69 and a velocity of 0
        output.note_off(final_note, 0)

        # close the MIDI output device and quit the library
        del output
        pygame.midi.quit()

        pygame.init()
        pygame.mixer.music.load("output/output.mid")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.wait(100)
