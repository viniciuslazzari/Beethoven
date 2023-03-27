import time

class Player:
    def __init__(self):
        self.notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        self.nota_atual = 'C'
        self.bpm_base = 60
 
    def note_exists(self, note):
        return note in self.notes

    def play_note(self, note, instrument, octave, volume, escala, midi_file, output):
        print(note)

        if not self.note_exists(note):
            final_note = (octave * escala) + (self.notes.index(self.nota_atual))
        else:
            final_note = (octave * escala) + (self.notes.index(note))
            self.nota_atual = note
            
        output.set_instrument(instrument)
        output.note_on(final_note, volume)
        time.sleep(self.bpm_base / bpm)

        return final_note