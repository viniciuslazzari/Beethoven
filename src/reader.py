class Reader:
    def __init__(self, beenput="", command=0, map={}):
        self.beenput = beenput
        self.command = command
        self.map = map

    def get_input(self):
        return self.beenput

    def set_input(self, input):
        self.beenput = input

    def get_command(self):
        return self.command

    def add_command(self, command):
        self.command = command

    def read_input(self):
        self.beenput = input("Enter the input: ")

    def decomposer(self):
        self.map = {}
        for char in self.input:
            if char not in self.map:
                self.map[char] = 1
            else:
                self.map[char] += 1

    def sequence_exists(self, sequence):
        return sequence in self.input

    def get_sequence_command(self, sequence):
        return self.command if self.sequence_exists(sequence) else None
