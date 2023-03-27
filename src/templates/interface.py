from kivy.app import App
from ..composer import Composer
from ..reader import Reader

class Interface(App):
    is_loading = False
    instrument_input = 0
    bpm_input = 0
    text_input = ''
    file_input = ''

    def get_loading(self):
        return self.is_loading

    def set_loading(self, loading):
        self.disable_button() if loading else self.enable_button()

        self.is_loading = loading

    def disable_button(self):
        self.root.ids.main_button.disabled = True

    def enable_button(self):
        self.root.ids.main_button.disabled = False

    def get_instrument(self):
        instrument = self.root.ids.instrument.text

        if not instrument.isnumeric():
            print("Error reading instrument!")
            return

        self.instrument_input = int(instrument)

    def get_bpm(self):
        bpm = self.root.ids.bpm.text

        if not bpm.isnumeric():
            print("Error reading BPM!")
            return

        self.bpm_input = int(bpm)

    def get_text(self):
        self.text_input = self.root.ids.text.text

    def get_file(self):
        self.file_input = self.root.ids.file.selection[0] if len(self.root.ids.file.selection) == 1 else ''

    def generate(self):
        self.get_instrument()
        self.get_bpm()
        self.get_text()
        self.get_file()

        self.set_loading(True)

        file_text = ''

        if (self.file_input != ''):
            reader = Reader(self.file_input)
            file_text = reader.read_file()

        generate_input = self.text_input + file_text

        composer = Composer(generate_input, self.bpm_input, self.instrument_input)

        composer.compose()

        self.set_loading(False)
