Act as an expert Python Developer and seasoned user of the Gang of Four Design Pattern Principals.

I want you to help me build a prompt builder using Python.

We start by making a clean prompt.md file that we can build upon.
Like this for example:
```bash
echo "# Who you are" > prompt.md;
echo "You are an expert Python Developer and seasoned user of the Gang of Four Design Pattern Principals." >> prompt.md;
echo "" >> prompt.md; # for readability.

echo "# Relevant Source Code" >> prompt.md;
```

Then we walk through the entire project tree and find all of the Python files that are not named '__init__.py' and are not in a 'tests' directory.

Once we have the list, we present the user with a menu like this:
```bash
1. main_python_file.py
2. input_output.FileReader.py
3. input_output.FileWriter.py
4. factories.LocalFileHandlerFactory
5. factories.RemoteFileHandlerFactory
...

```
Notice how I am using the directory as a label in the menu using dot notation so that it is clear what directory the file is in.


I want to be able to include some of these python scripts into the prompt that we are going to build.

So when I select "2.", The class in FileReader.py is added to the prompt.md file that we started building earlier.

Here is what FileReader.py looks like:
```python
# no imports
#
class FileReader:
    def read(self, filename):
        with open(filename, 'r') as file:
            return file.read()
```

After I press option "2.", this is what prompt.md should look like:
===== BEGIN PROMPT =====
# Who you are
You are an expert Python Developer and seasoned user of the Gang of Four Design Pattern Principals.

# Relavant Source Code
## FileReader class
```python
class FileReader:
    def read(self, filename):
        with open(filename, 'r') as file:
            return file.read()
```
===== END PROMPT =====


The menu should now look like this:
```bash
1. main_python_file.py
2. input_output.FileReader.py            SELECTED
3. input_output.FileWriter.py
4. factories.LocalFileHandlerFactory
5. factories.RemoteFileHandlerFactory
```

Make sure that the "SELECTED" text lines up with all of the others.  For example, If I type "3.", the menu should look like this:
```bash
1. main_python_file.py
2. input_output.FileReader.py            SELECTED
3. input_output.FileWriter.py            SELECTED
4. factories.LocalFileHandlerFactory
5. factories.RemoteFileHandlerFactory
```

After we are done presumably by typing "done.

Please write the Python script(s) that will accomplish this.

