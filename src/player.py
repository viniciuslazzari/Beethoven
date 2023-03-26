import pygame.midi
import time
from midiutil import MIDIFile

class Player:
    def __init__(self):
        self.notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
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
        self.instrument = instrument
        self.octave = octave
        self.volume = volume
        self.bpm = bpm

        midi_file = MIDIFile(1)

        midi_file.addTempo(self.track, self.time, self.bpm)

        for note in text:
            if not self.note_exists(note):
                final_note = (self.octave * 12) + (self.notes.index("C#"))
                volume_atual = int(self.volume/2)

            else:
                final_note = (self.octave * 12) + (self.notes.index(note))
                volume_atual = self.volume

            midi_file.addNote(
                self.track, self.channel, final_note,
                self.time, self.duration, volume_atual
            )

            self.time += 1

        with open(output_file, "wb") as output_file:
            midi_file.writeFile(output_file)

        import pygame

        pygame.init()
        pygame.mixer.music.load("output/output.mid")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.wait(100)

