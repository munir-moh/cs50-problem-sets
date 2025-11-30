"""Even so, in a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. 
If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank."""

import sys
import os

if len(sys.argv) != 2:
    sys.exit("Too few command-line arguments" if len(sys.argv) < 2 else "Too many command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".py"):
    sys.exit()

if not os.path.isfile(filename):
    sys.exit()

count = 0

with open(filename) as f:
    for line in f:
        stripped = line.strip()
        if stripped == "" or stripped.startswith("#"):
            continue
        count += 1

print(count)
