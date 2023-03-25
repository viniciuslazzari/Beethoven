from kivy.app import App

class Interface(App):
    pass

    def say_hello(self):
        instrument = self.root.ids.instrument.text
        bpm = self.root.ids.bpm.text
        text = self.root.ids.text.text
        file_path = self.root.ids.file.selection[0]

        print(instrument, bpm, text, file_path)