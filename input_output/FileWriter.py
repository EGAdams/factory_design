# no imports
#
class FileWriter:
    def write(self, filename, content):
        with open(filename, 'w') as file:
            file.write(content)