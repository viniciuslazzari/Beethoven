from kivy.app import App
from src.templates.interface import Interface

class Beethoven():
    def main(self):
        interface = Interface()
        interface.run()

if __name__ == "__main__":
    bee = Beethoven()
    bee.main()