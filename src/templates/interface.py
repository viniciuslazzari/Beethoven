import pygame.midi
from kivy.app import App
from ..player import Player

possible_instruments = ['Sine', 'Triangle', 'Square']

class Interface(App):
    __is_loading = False
    __instrument_input = ''
    __bpm_input = ''
    __text_input = ''
    __file_input = ''

    def get_loading(self):
        return __is_loading

    def set_loading(self, loading):
        self.disable_button() if loading else self.enable_button()

        self.__is_loading = loading

    def disable_button(self):
        self.root.ids.main_button.disabled = True

    def enable_button(self):
        self.root.ids.main_button.disabled = False

    def get_instrument(self):
        instrument = self.root.ids.instrument.text

        if instrument not in possible_instruments:
            print("Error reading instrument!")
            return

        self.__instrument_input = instrument

    def get_bpm(self):
        bpm = self.root.ids.bpm.text

        if not bpm.isnumeric():
            print("Error reading BPM!")
            return

        self.__bpm_input = bpm

    def get_text(self):
        self.__text_input = self.root.ids.text.text

    def get_file(self):
        self.__file_input = self.root.ids.file.selection[0] if len(self.root.ids.file.selection) == 1 else ''
 
    def generate(self):
        self.get_instrument()
        self.get_bpm()
        self.get_text()
        self.get_file()

        self.set_loading(True)

        print(self.__instrument_input, self.__bpm_input, self.__text_input, self.__file_input)

        teste = Player()

        bpm = int(self.__bpm_input)

        volume = 127

        octave = 4

        instrument = 0

        teste.play_note(self.__text_input, instrument, octave, volume, bpm)