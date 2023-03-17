from kivy.app import App
from src.interface import Interface

class Beethoven():
    def main(self):
        inter = Interface()
        inter.run()

if __name__ == "__main__":
    bee = Beethoven()
    bee.main()