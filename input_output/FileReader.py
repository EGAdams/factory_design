# no imports
#
class FileReader:
    def read(self, filename):
        with open(filename, 'r') as file:
            return file.read()
        