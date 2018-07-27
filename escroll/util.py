import sys, tempfile, os, datetime
from subprocess import call
from cmd import Cmd
from argparse import ArgumentParser

# Sets up the argument parser and returns the user parsed args
def parsed_args(args):
    parser =  ArgumentParser(description="")
    parser = ArgumentParser(description="")
    parser.add_argument("-i", "--init", help="Creates a file")
    parser.add_argument("-fd", "--find-date",  help="Find all entries at a specific date")
    parser.add_argument("-w", "--write", help="Write a new entry", action="store_true")
    parser.add_argument("-t", "--todo", help="Manage your To-Do list", action="store_true")

    return parser.parse_args(args)

#Initialize a scroll file
def init(argname):
    # Check for exisiting scroll file
    for filename in os.listdir('.'):
        if filename.endswith('.scroll'):
            print("A scroll file has already been initialized in this project! \n",
            "The file: {} is currently the main scroll file.".format(filename),
            "There can only be one scroll file in a project.")
            return False
    else:
        # Create the new scroll file
        with open('{}.scroll'.format(argname), 'w+') as scroll_file:
            lines = ["~{}~\n", "&{}&\n", "?{}?\n"]
            scroll_file.writelines(lines)
            print("{}.scroll has been created successflly!".format(argname))
            return True


#Main append funtion to edit the .scroll file
def write():
    # Check if .scroll file exists
    file_exists = False
    for fname in os.listdir('.'):
        if fname.endswith('.scroll'):
            file_exists = True
            # Load up Vim for editing

            EDITOR = os.environ.get('EDITOR','vim') 
            initial_message = b"" #b is for buffered

            with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
                tf.write(initial_message)
                tf.flush()
                call([EDITOR, tf.name])

                tf.seek(0)
                edited_message = tf.read()
                
                scroll_file = open(fname, "a")
                scroll_file.write(edited_message.decode("utf-8"))
                scroll_file.close()
            break
    if not file_exists:
        print("Could not find .scroll file. Have you tried running escroll -i?")

# Opens to ToDo prompt
def open_todo():
    prompt = ToDoPrompt()
    prompt.prompt = '> '
    prompt.cmdloop('Welcome to the To-Do interface!')


################################ Classes #################################

class ToDoPrompt(Cmd):
    
    tasks = [] # Read from .scroll file to get existing tasks

    def do_add(self, args):
        """ Adds a new task to your To-Do list """
        if len(args) == 0:
            print("Error: Task cannot be blank!")
        else:
             #TODO implement multiple tasks at once as well as entry through vim
            self.tasks.append(args)
            self.print_tasks()

    def do_quit(self, args):
        """ Quits the To-Do shell """
        raise SystemExit



    #Auxillary functions
    def print_tasks(self):
        i = 1
        print("To Do: \n")
        for task in self.tasks:
            print("{}. {}".format(i, task))
            i = i + 1        
                
