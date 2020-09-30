import md_toc
import sys
import argparse
import os
import pyperclip


###############################################################################
###############################################################################
#                              SUBROUTINES
###############################################################################
###############################################################################

# prompts user for the filename if one was not provided in the arguments
def getFileName():
    if args.file != None:
        return args.file[0]
    else:
        return input('\nFile name: ')

# checks if the file exists
def doesFileExist(file):
    return os.path.exists(file)

# displays a message and quits the program
def quitProgram(message):
    print('\n' + message)
    quit()

# get the generated toc
def getToc(fileName):
    return md_toc.build_toc(fileName)

# enclose the toc in a details tag
def encloseTocInDetails(toc, displayText = 'Click me to open'):
    output = '<details>\n<summary>' + displayText + '</summary>\n\n'
    output += toc + '\n\n</details>'
    return output


###############################################################################
###############################################################################
#                              MAIN LOGIC
###############################################################################
###############################################################################

# setup argument parser
parser = argparse.ArgumentParser(description="Generate a table of contents for your markdown file.")
parser.add_argument('-d', '--details', action="store_true", help="Enclose the toc in a <details> html tag")
parser.add_argument('-f', '--file', nargs=1, help="Name of the markdown file")
parser.add_argument('-c', '--copy', action="store_true", help="Copy output to clipboard")
args = parser.parse_args()


# get the filename
fileName = getFileName()

# quit program if file does not exist
if not doesFileExist(fileName):
    quitProgram('File does not exist')

# generate the toc
toc = getToc(fileName)

# enclose the toc in a details tag if the user elected to
if args.details == True:
    toc = encloseTocInDetails(toc)

# print output
print('\n' + toc)

# copy output to clipboard
if args.copy == True:
   pyperclip.copy(toc)
   print('\n\n\nCopied to clipboard') 