import time
from midiutil import MIDIFile

class Player:
    def __init__(self):
        self.notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        self.sounds = ["sound1.wav", "sound2.wav", "sound3.wav"]
 
    def note_exists(self, note):
        return note in self.notes

    def play_note(self, note, octave, volume, escala, midi_file, output):
        print(note)

        if not self.note_exists(note):
            final_note = (octave * escala) + (self.notes.index(nota_atual))
        else :
            final_note = (octave * escala) + (self.notes.index(note))
            nota_atual = note
            volume_atual = volume
            
        output.set_instrument(instrument)
        output.note_on(final_note, volume_atual)
        time.sleep(bpm_base/bpm)

        midi_file.addNote(self.track, self.channel, final_note, self.time, self.duration, volume_atual)