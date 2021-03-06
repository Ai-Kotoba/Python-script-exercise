#!/usr/bin/env python3

# mcb.pyw - Saves and loads pieces of text to the clipboard.
import shelve
import pyperclip
import sys

mcbShelf = shelve.open("mcb")
# TODO: Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == "save":
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == "delete":
        mcbShelf.pop(sys.argv[2])
# TODO: List keywords and load content.
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == "delete":
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()
