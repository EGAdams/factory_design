from handlers.FunctionHandler import FunctionHandler

class FileHandlerFactory:
    def create_read_handler( self ) -> FunctionHandler:
        raise NotImplementedError
