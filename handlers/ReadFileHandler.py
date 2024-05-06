# cinco de mayo   My independence day.
# fixed the base crawler at mcds this morning.  cost my 2.08 for the medium coffee.  took about 1.5 hours.

from handlers.FunctionHandler import FunctionHandler
from input_output.FileReader import FileReader

class ReadFileHandler(FunctionHandler):
    """
    Concrete class implementing file reading functionality.
    """
    
    def __init__(self):
        # Initialize FileReader as a component of ReadFileHandler
        self.file_reader = FileReader()

    def execute(self, parameters: dict) -> str:
        """
        Execute the file reading function by utilizing the FileReader component.

        Args:
            parameters (dict): Parameters required for reading the file.
                - filename (str): Name of the file to read.
        
        Returns:
            str: Content of the file.
        """
        try:
            filename = parameters['filename']  # Assume filename is always provided
            return self.file_reader.read(filename)
        except KeyError:
            return "Error: 'filename' parameter is missing."
        except FileNotFoundError:
            return f"Error: The file '{filename}' does not exist."
        except Exception as e:
            return f"Error: An unexpected error occurred: {e}"
