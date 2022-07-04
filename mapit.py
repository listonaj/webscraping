#! /usr/bin/env python3
# mapit.py - Launches a map in the browser using an adress from the 
# command line or clipboard
# 
# <chmod u+x mapit.py> to make the file executable
# to run : ./mapit.py <address>.

import webbrowser,sys,pyperclip

if len(sys.argv) >1:
    #Get address from command line.
    address = ' '.join(sys.argv[1:])
    print(address)

else:
    #get the address from the clipboard
    address = pyperclip.paste

webbrowser.open('https://www.google.com/maps/place/'+ address)