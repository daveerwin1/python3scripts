import os

# Use `rm **/temp.txt` to delete all the temp.txt files after running the script to generate html files.

for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if '.scss' in file:
            open(subdir + '/temp.txt', 'w').close()




