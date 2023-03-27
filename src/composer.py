import random
import pygame
from midiutil import MIDIFile
from src.player import Player

harpa = ["I", "i", "O", "o", "U", "u"]
repete = ["a", "b", "c", "d", "e", "f", "g"]
digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

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

    def note_exists(self, note):
        return note in notes

    def compose(self):
        pygame.midi.init()
        output = pygame.midi.Output(0)
        # output = 1
        escala = 12

        midi_file = MIDIFile(1)

        midi_file.addTempo(self.track, self.time, self.bpm)

        nota_atual = ''

        for note in self.text:
            volume_atual = self.volume
            final_note = 0

            # Dobra o volume e continua o loop
            if note == " ":
                self.double_volume()
                continue
            
            # Aumenta a oitava e continua o loop
            if note == "?" or note == ".":
                self.increase_octave()
                continue

            # Troca o instrumento sem tocar nada e continua o loop
            if note == "!" or note in harpa or note == "\n" or note == ";" or note == ",":
                self.player.play_instrument(note, self.instrument, output)

                time.sleep(60 / self.bpm)
                self.time += 1

                continue

            # Se a nota atual existir, toca ela
            if self.note_exists(note):
                final_note = self.player.play_note(note, self.bpm, self.instrument, self.octave, volume_atual, escala, output)
            # Senão, repete a ultima nota
            else:
                final_note = self.player.repeat_note(self.instrument, self.octave, volume_atual, escala, output)
            
            time.sleep(60 / self.bpm)
            midi_file.addNote(self.track, self.channel, final_note, self.time, self.duration, volume_atual)

            self.time += 1

        output_file = "output/output.mid"

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

    def double_volume(self):
        self.volume *= 2

    def reset_volume(self):
        self.volume = 50

    def increase_octave(self):
        self.octave += 1

    def get_random_note(self):
        notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        return random.choice(notes) + str(self.octave)
