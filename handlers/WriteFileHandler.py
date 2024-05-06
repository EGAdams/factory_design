# cinco de mayo
from handlers.FunctionHandler import FunctionHandler
from input_output.tests.TestFileWriter import FileWriter


class WriteFileHandler(FunctionHandler):
    """
    Concrete class implementing file writing functionality.
    """
    
    def __init__(self):
        # Initialize FileWriter as a component of WriteFileHandler
        self.file_writer = FileWriter()

    def execute(self, parameters: dict) -> str:
        """
        Execute the file writing function by utilizing the FileWriter component.

        Args:
            parameters (dict): Parameters required for writing to the file.
                - filename (str): Name of the file to write to.
                - content (str): Content to be written to the file.
        
        Returns:
            str: Confirmation message indicating success or an error message.
        """
        try:
            filename = parameters['filename']  # Assume filename is always provided
            content = parameters.get('content', '')  # Default to empty string if no content provided
            return self.file_writer.write(filename, content)
        except KeyError:
            return "Error: 'filename' parameter is missing."
        except Exception as e:
            return f"Error: An unexpected error occurred: {e}"
