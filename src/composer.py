import random
import pygame
from midiutil import MIDIFile
from src.player import Player

class Composer:
    def __init__(self, text, bpm, instrument):
        self.text = text
        self.bpm = bpm
        self.instrument = instrument
        self.volume = 50
        self.octave = 4
        self.track = 0
        self.channel = 0
        self.time = 0
        self.duration = 1
        self.player = Player()

    def get_bpm(self):
        return self.bpm

    def set_bpm(self, bpm):
        self.bpm = bpm

    def get_instrument(self):
        return self.instrument

    def set_instrument(self, instrument):
        self.instrument = instrument

    def get_volume(self):
        return self.volume

    def get_octave(self):
        return self.octave

    def compose(self):
        pygame.midi.init()
        output = pygame.midi.Output(0)
        # output = 1
        escala = 12
        nota_atual = "C"
        repete = ["a", "b", "c", "d", "e", "f", "g"]

        midi_file = MIDIFile(1)

        midi_file.addTempo(self.track, self.time, self.bpm)

        for note in self.text:
            final_note = self.player.play_note(note, self.instrument, self.octave, self.volume, escala, midi_file, output)

            midi_file.addNote(self.track, self.channel, final_note, self.time, self.duration, self.volume)

        with open(output_file, "wb") as output_file:
            midi_file.writeFile(output_file)

        output.note_off(final_note, 0)

        del output
        pygame.midi.quit()

        pygame.init()
        pygame.mixer.music.load("output/output.mid")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.wait(100)

    def generate_random_bpm(self):
        self.bpm = random.randint(60, 180)

    def increase_bpm(self):
        self.bpm += 10

    def double_volume(self):
        self.volume *= 2

    def reset_volume(self):
        self.volume = 50

    def increase_octave(self):
        self.octave += 1

    def get_random_note(self):
        notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        return random.choice(notes) + str(self.octave)
