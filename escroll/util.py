import sys, tempfile, os, datetime
from subprocess import call

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
                # do the parsing with `tf` using regular File operations.
                # for instance:
                tf.seek(0)
                edited_message = tf.read()
                
                scroll_file = open(fname, "a")
                scroll_file.write(edited_message.decode("utf-8"))
                scroll_file.close()
            break
    if not file_exists:
        print("Could not find .scroll file. Have you tried running escroll -i?")
        