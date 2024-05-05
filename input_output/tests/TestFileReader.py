import os
import sys
sys.path.append( '/home/adamsl/factory_design/' )
from input_output.FileReader import FileReader

class TestFileReader:
    def __init__(self, file_reader):
        self.file_reader = file_reader

    def execute(self):
        test_filename = 'test_file.txt'
        test_content = 'Hello, this is a test.'
        try:
            with open(test_filename, 'w') as file:
                file.write(test_content)
            
            read_content = self.file_reader.read(test_filename)
            assert read_content == test_content, "Test failed: Content does not match."
            print("Test passed: Content matches.")
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if os.path.exists(test_filename):
                try:
                    os.remove(test_filename)
                    if not os.path.exists(test_filename):
                        print("Cleanup successful: File removed.")
                    else:
                        print("Cleanup failed: File still exists.")
                except OSError as e:
                    print(f"Error removing file: {e}")

file_reader = FileReader()
tester = TestFileReader(file_reader)
tester.execute()
