import os

for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if 'config.js' in file:
            open(subdir + '/temp.txt', 'w').close()




