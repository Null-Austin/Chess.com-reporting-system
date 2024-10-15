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
    if check.requestuser(username) == True:
        olddata = ast.literal_eval(read('reportedPlayers.txt'))
        newdata = olddata.get(username, 0)  # Get current data or default to 0

        newdata += 1  # Increment the report count
        olddata[username] = newdata  # Update the old data with the new count
        write('reportedPlayers.txt', olddata)  # Write back to the file

        return 'Report sent'
    else:
        return 'No such user found.'
def getreports(username):
    if ast.literal_eval(read('reportedPlayers.txt')).get(username) == None:
        return(0)
    else:
        return(ast.literal_eval(read('reportedPlayers.txt')).get(username))
print(getreports('test8'))