# Who you are
You are an expert Python Developer and seasoned user of the Gang of Four Design Pattern Principals.

# Relevant Source Code
## ReadFileHandler class
```python
class ReadFileHandler(FunctionHandler):
    """
    Concrete class implementing file reading functionality.
    """
    
    def execute(self, parameters: dict) -> str:
        """
        Execute the file reading function.
        
        Args:
            parameters (dict): Parameters required for reading the file.
                - filename (str): Name of the file to read.
        
        Returns:
            str: Content of the file.
        """
        filename = parameters.get("filename")
        # Implement file reading logic here
        return "File content read successfully."
```
## FileReader class
```python
class FileReader:
    def read(self, filename):
        with open(filename, 'r') as file:
            return file.read()
```
## original_source class
```python
import json
import time
from time import sleep
from openai import OpenAI
GPT_MODEL = "gpt-3.5-turbo-0125"
from AssistantFactory import AssistantFactory
from HandleActionRequired import HandleActionRequired

def show_json(obj):
    json_obj = json.loads(obj.model_dump_json())
    pretty_json = json.dumps(json_obj, indent=4)  # Pretty print JSON
    print( pretty_json )

def write_file( filename, content ):  # write to hard drive
    """Writes content to a specified file.
    
    Args:
        filename (str): The name of the file to write to.
        content (str): The content to write to the file.
    """
    with open( filename, 'w' ) as file:
        file.write( content )
    return "File written successfully."

def read_file( filename ): # read from hard drive
    """Reads content from a specified file.
    
    Args:
        filename (str): The name of the file to read from.
    
    Returns:
        str: The content of the file.
    """
    
    # morph the file name since the assistant seems to be looking at it's sandbox
    filename = filename.replace( '/mnt/data/', '' )
    with open(filename, 'r') as file:
        return file.read()

assistantFactory = AssistantFactory()

# create an assistant asst_Zw3KYZUBFI9jZheRiVLkQAta MemGPT_Coder
# assistant = assistantFactory.createAssistant( nameArg="MemGPT_Coder" )
assistant =  assistantFactory.getExistingAssistant( assistant_id="asst_Zw3KYZUBFI9jZheRiVLkQAta" )

# create a thread
client = OpenAI()
thread = client.beta.threads.create()

# Add a message to a thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="What do you know about attached files that you have?"
)

# Create the run
run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
)

def execute_function( function_json ):
    """Parses a JSON object to execute a function based on the name and parameters.
    
    Args:
        function_json (str): A JSON string containing the function name and parameters.
        
    Returns:
        str: The result of the function execution.
    """
    
    # Parse the JSON string into a Python dictionary
    function_data = json.loads(function_json)
    
    # Extract the function name and parameters
    function_name = function_data.get("function")
    parameters = function_data.get("parameters", {})
    
    # Match the function name to the actual function and execute it
    if function_name == "write_file":
        return write_file(parameters.get("filename"), parameters.get("content"))
    elif function_name == "read_file":
        return read_file(parameters.get("filename"))
    else:
        return "Function not recognized."

def wait_on_run( run, thread ):
    print ( "entering while.  run status is: " + run.status )
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep( 0.5 )
        print( "done sleeping.  checking for any action required..." )
        if run.status == "requires_action":
            print( "found action required.  sending the run for processing..." )
            available_functions = {
                "read_file": read_file,
                "write_file": write_file
            }
            messages = client.beta.threads.messages.list( thread_id=thread.id )
            handleActionRequired = HandleActionRequired( messages, available_functions, run )
            return handleActionRequired.execute( thread.id ) # returns run for now...
    
    print(f"Run {run.id} is {run.status}.")
    return run

run = wait_on_run( run, thread )
show_json( run )

messages = client.beta.threads.messages.list(thread_id=thread.id)
show_json(messages) # display the assistant's response
print ( "\n" )

def pretty_print(messages):
    print( "\n\n")
    print( "# Messages" )
    for m in messages:
        print(f"{m.role}: {m.content[0].text.value}")
    print()
    
while ( True ):
    new_message = input( "Enter a message to send to the assistant: " )
    # Add a message to a thread
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=new_message )
   
    run = client.beta.threads.runs.create( # create a run
    thread_id=thread.id,                   # that we will
    assistant_id=assistant.id )            # be waiting on.
    
    # get the run steps so that we can look at them
    run_steps = client.beta.threads.runs.steps.list(
        thread_id=thread.id, run_id=run.id, order="asc" )
    
    for step in run_steps.data:
        step_details = step.step_details                        # look at them
        print(json.dumps(show_json(step_details), indent=4))

    wait_on_run( run, thread )   # we will be back...
    messages = client.beta.threads.messages.list( thread_id=thread.id )
    # reverse the order so that the most recent message is at the top of the list
    # Convert to list if it's not already one, assuming messages is iterable
    messages_list = list(messages)
    reversed_messages = messages_list[::-1] # Reverse the list
    pretty_print( reversed_messages )

```
# Context
We have the source code for a system that works fine, it just has too many responsibilities.  I need you to help me break the original Python file into parts.  I have already had a meeting with our other developers and they have agreed that the design depicted in the Mermaid Class Diagram is the one that we are going to use as a guide when refactoring.  We are going to incrementally build each object and eventually we will replace the entire original source code with all of our new objects.


# Mermaid class diagram for the system that we are building
```mermaid
classDiagram
    class FileHandlerFactory {
        <<interface>>
        +createReadHandler(): FunctionHandler
        +createWriteHandler(): FunctionHandler
    }
    class LocalFileHandlerFactory {
        +createReadHandler(): FunctionHandler
        +createWriteHandler(): FunctionHandler
    }
    class RemoteFileHandlerFactory {
        +createReadHandler(): FunctionHandler
        +createWriteHandler(): FunctionHandler
    }
    class FunctionHandler {
        <<interface>>
        +execute(parameters: dict): str
    }
    class ReadFileHandler {
        +execute(parameters: dict): str
    }
    class WriteFileHandler {
        +execute(parameters: dict): str
    }
    class FileReader {
        +read(filename: str): str
    }
    class FileWriter {
        +write(filename: str, content: str): str
    }
    LocalFileHandlerFactory --|> FileHandlerFactory
    RemoteFileHandlerFactory --|> FileHandlerFactory
    ReadFileHandler --> FileReader : uses
    WriteFileHandler --> FileWriter : uses
    WriteFileHandler --|> FunctionHandler
    ReadFileHandler --|> FunctionHandler
    LocalFileHandlerFactory --> ReadFileHandler : creates
    LocalFileHandlerFactory --> WriteFileHandler : creates
    RemoteFileHandlerFactory --> ReadFileHandler : creates
    RemoteFileHandlerFactory --> WriteFileHandler : creates
```


# Your Task
Please show me how I can incrementally integrate the ReadFileHandler class into the original_source class.