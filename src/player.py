import time

class Player:
    def __init__(self):
        self.notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        self.harpa = ["I", "i", "O", "o", "U", "u"]
        self.nota_atual = 'A#'

    def get_instrument(self, char, instrument):
        if char == "!":
            return 113
        elif char in self.harpa:
            return 6
        elif char == "\n":
            return 14
        elif char == ";":
            return 75
        elif char == ",":
            return 19
        elif isnumeric(char):
            new_instrument = instrument + int(char)
            new_instrument = new_instrument if new_instrument < 127 else 0

            return new_instrument

    def play_instrument(self, note, instrument, output):
        new_instrument = self.get_instrument(note, instrument)

        self.nota_atual = "A#"

        output.set_instrument(new_instrument)

        return final_note  

    def repeat_note(self, instrument, octave, volume, escala, output):
        if self.nota_atual != "A#":
            final_note = (octave * escala) + (self.notes.index(nota_atual))
            self.nota_atual = "A#"

        output.set_instrument(instrument)
        output.note_on(final_note, volume)

        return final_note

    def play_note(self, note, bpm, instrument, octave, volume, escala, output):
        if not self.note_exists(note):
            final_note = (octave * escala) + (self.notes.index(self.nota_atual))
        else:
            final_note = (octave * escala) + (self.notes.index(note))
            self.nota_atual = note
            
        output.set_instrument(instrument)
        output.note_on(final_note, volume)

        return final_note