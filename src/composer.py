import random

class Composer:
    def __init__(self, bpm, function_map):
        self.bpm = bpm
        self.instrument = 1  # default instrument is piano
        self.volume = 50  # default volume is 50%
        self.octave = 4  # default octave is 4
        self.player = Player()
        self.MAP = function_map

    def get_bpm(self):
        return self.bpm

    def set_bpm(self, bpm):
        self.bpm = bpm

    def get_instrument(self):
        return self.instrument

    def get_volume(self):
        return self.volume

    def get_octave(self):
        return self.octave

    def compose(self, notes):
        for note in notes:
            if note == 0:
                self.player.rest()
            else:
                func = self.get_command_function(note)
                func()

    def get_command_function(self, command):
        return self.MAP[command]

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
