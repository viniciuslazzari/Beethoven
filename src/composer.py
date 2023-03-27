import random
import pygame
from midiutil import MIDIFile
from src.player import Player
import time

harpa = ["I", "i", "O", "o", "U", "u"]
notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

class Composer:
    def __init__(self, text, bpm, instrument):
        self.text = text
        self.bpm = bpm
        self.instrument = instrument
        self.volume = 50
        self.octave = 1
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

    def __note_exists(self, note):
        return note in notes

    def compose(self):
        pygame.midi.init()
        output = pygame.midi.Output(0)
        escala = 12

        midi_file = MIDIFile(1)

        midi_file.addTempo(self.track, self.time, self.bpm)

        # Set the program change event to the selected instrument
        output.set_instrument(self.instrument)
        midi_file.addProgramChange(self.track, self.channel, self.time, self.instrument)

        for note in self.text:
            volume_atual = self.volume
            final_note = 0

            # Dobra o volume e continua o loop
            if note == " ":
                self.__double_volume()
                continue
            
            # Aumenta a oitava e continua o loop
            if note == "?" or note == ".":
                self.__increase_octave()
                continue

            # Troca o instrumento sem tocar nada e continua o loop
            if note == "!" or note in harpa or note == "\n" or note == ";" or note == "," or note.isnumeric():
                self.instrument = self.player.play_instrument(note, self.instrument, output)

                output.set_instrument(self.instrument)
                midi_file.addProgramChange(self.track, self.channel, self.time, self.instrument)

                time.sleep(60 / self.bpm)
                self.time += 1

                continue

            # Se a nota atual existir, toca ela
            if self.__note_exists(note):
                final_note = self.player.play_note(note, self.instrument, self.octave, volume_atual, escala, output)
            # Senão, repete a ultima nota
            else:
                final_note = self.player.repeat_note(self.instrument, self.octave, volume_atual, escala, output)
            
            time.sleep(60 / self.bpm)
            output.note_off(final_note, 0)

            if final_note == 10:
                volume_atual = 0
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

    def __double_volume(self):
        self.volume *= 2

        if self.volume > 127:
            self.__reset_volume()

    def __reset_volume(self):
        self.volume = 50

    def __increase_octave(self):
        self.octave += 1
