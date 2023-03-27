class Reader:
    def __init__(self, file):
        self.file = file

    def file_is_txt(self):
        return self.file.endswith('.txt')

    def read_file(self):
        if (not self.file_is_txt()):
            print('Error opening file!')
            return ''

        fl = open(self.file, 'r')

        text = fl.read()

        return text