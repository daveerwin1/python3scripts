import os
import sys
from bs4 import BeautifulSoup
from bs4 import Comment

# Usage: make files named temp.html with the output from the html pane in fractal
# temp.html should be located in same dir as hbs files
# temp.html must have equal number of comments and html blocks
# file example:

#<!-- Button Icon -->
#<button></button>

#<!-- Is Disabled -->
#<button></button>

#<!-- Overflow -->
#<button></button>

#<!-- Overflow Is Disabled -->
#<button></button>

# Script will read this file and create 4 html files and an _index.md file



for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file == 'temp.txt':
            full_filepath = os.path.join(subdir, file)
            path = subdir

            current_dir = subdir.split(os.path.sep)[-1]
            with open(full_filepath, 'r') as f:
                contents = f.read()
                soup = BeautifulSoup(contents, 'lxml')
                body = soup.find("body")
                children = body.findChildren(recursive=False)
                comments = soup.findAll(text=lambda text:isinstance(text, Comment))
                for num, name in enumerate(children):
                    # Use the comment to name the html file.
                    filename = path + '/' + str(comments[num].lower().strip().replace(" ", "-")) + '.html'
                    file_contents = '---' + '\n'
                    file_contents += 'title: ' + comments[num].strip() + '\n'
                    file_contents += 'weight: ' + str(num + 1) + '\n'
                    file_contents += '---' + '\n'
                    file_contents += str(children[num].prettify().strip())

                    html_file = open(filename, 'w')
                    html_file.write(file_contents)
                    html_file.close()

                    index_file_contents = '---' + '\n'
                    index_file_contents += 'title: ' + current_dir.capitalize() + '\n'
                    index_file_contents += 'modaux:' + '\n'
                    index_file_contents += '  merge: true' + '\n'
                    index_file_contents += '---'


                    index_filename = path + '/' + '_index.md'
                    index_file = open(index_filename, 'w')
                    index_file.write(index_file_contents)
                    index_file.close()




