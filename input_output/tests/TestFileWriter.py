import os

class FileWriter:
    def write(self, filename, content):
        with open(filename, 'w') as file:
            file.write(content)

class TestFileWriter:
    def __init__(self, file_writer):
        self.file_writer = file_writer

    def execute(self):
        test_filename = 'test_file.txt'
        test_content = 'Hello, this is a test.'
        try:
            self.file_writer.write(test_filename, test_content)
            with open(test_filename, 'r') as file:
                read_content = file.read()
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

# Example usage
file_writer = FileWriter()
tester = TestFileWriter(file_writer)
tester.execute()
