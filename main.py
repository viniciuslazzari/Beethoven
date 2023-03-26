import pygame.midi #importada mesemo sem ser usada para ter o SDL correto
from src.templates.interface import Interface



class Beethoven():
    def main(self):
        interface = Interface()
        interface.run()


if __name__ == "__main__":
    bee = Beethoven()
    bee.main()