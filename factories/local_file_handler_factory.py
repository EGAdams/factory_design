#
#
#
from factories.file_handler_factory import FileHandlerFactory
from handlers.FunctionHandler       import FunctionHandler
from handlers.ReadFileHandler       import ReadFileHandler

class LocalFileHandlerFactory( FileHandlerFactory ):
    def create_read_handler( self ) -> FunctionHandler:
        return ReadFileHandler()
