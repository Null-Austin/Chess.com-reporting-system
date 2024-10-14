import ast
import checkuser as check
def read(filename):
    """Reads the contents of a file."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"File {filename} not found."

def write(filename, content):
    """Writes content to a file, overwriting existing content."""
    with open(filename, 'w') as file:
        file.write(str(content))
    return f"Content written to {filename}."
def report(username): #{'test1':1,'test2':2,'test3':3,'test4':4,'test5':5}
    newdata=ast.literal_eval(read('reportedPlayers.txt'))#
    olddata=newdata
    newdata=ast.literal_eval(read('reportedPlayers.txt')).get(username)
    newdata += 1
    olddata[username] = newdata
    write('reportedPlayers.txt',olddata)