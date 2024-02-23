'''
Michelle Luo
Cmdr. Schenk
Final Graded Experience: Pixel Printer/Inverter
May 16 2023
AP CS50
'''

# PROGRAM DESCRIPTION
# This program take 2 or 3 arguments in the command line.
# The 1st argument is the python file name (i.e. fge.py)
# The 2nd argument is the path to a PNG image file, in the form of a string
# The 3rd argument is optional. If the third argument is specified as "invert", then the program will return an inverted color image, which looks like an x-ray effect.
# The return of this program is a PNG image being printed to the command line.
# Please keep in mind that larger PNG images will take a longer time to load, and may appear differently depending on the size capacity of a user's terminal.
# BEFORE RUNNING: pip install matplotlib, sty, and PIL
# USES: steganography, creating an x-ray filter, loading up a larger version of small image files, printing PNG image files in a command line Terminal.

# for copy and paste
# & C:/Users/miche.MICHYLAPTOP/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/miche.MICHYLAPTOP/Downloads/ALL_PROJECTS/pixel image printer/fge.py" "C:\Users\miche.MICHYLAPTOP\Desktop\micheelArt\moon.png" invert

# C:/Users/miche.MICHYLAPTOP/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/miche.MICHYLAPTOP/Downloads/ALL_PROJECTS/pixel image printer/fge.py" "C:\Users\miche.MICHYLAPTOP\Desktop\micheelArt\oceanside.png" invert

#Import sys, os, matplotlib, sty, and PIL modules
import sys, os
from matplotlib import image as imgMPL
from sty import fg, bg, ef, rs, Style, RgbFg
from PIL import Image as pilmager

#main method
def main():
    #define variables
    pixelString = ""
    index = 0
    #clear the Screen
    # clearScreen()
    #get rgb values in three different arrays for r, g, b respectively
    r,g,b = load_rgb()
    #find the dimensions of the image used
    width, height = findWidth()
    #for each pixel in the image...
    for x in range(0, len(r)):
        #add ASCII characters in colored strings to variable pixelString
        pixelString = pixelString + get_color_escape(r[x], g[x], b[x]) + get_color_escape(r[x], g[x], b[x], True)+ "  " + '\033[0m'
        #if the width dimension is reached using the index counter, insert a new line character into the pixelString variable
        if (index == width - 1):
            pixelString = pixelString + "\n"
            #revert index back to beginning
            index = -1
        #add 1 to index counter
        index += 1
    print(pixelString)

#load the image's rgb values and save them in arrays r, g, b
def load_rgb():
    #define variables and arrays
    mode = ""
    r = []
    g = []
    b = []
    #define imageAddress using the 2nd argument (including the python file argument)
    imageAddress = sys.argv[1]
    #if there is a third argument, set that equal to the variable 'mode'
    if (len(sys.argv) > 2):
        mode = sys.argv[2]
    #read the file for rgb data
    myFile = imgMPL.imread(imageAddress)
    for blob in myFile:
        #try to run the analyzation of 'blob'
        try:
            for temp_r, temp_g, temp_b, temp_o in blob:
                #if the 'mode' is set to inversion, append inverted values to the lists r, g, b
                if (mode == "invert"):
                    #temp_r is multiplied from its float value and rounded to fit the 0-225 rgb format
                    r.append(255 - round(temp_r * 255))
                    g.append(255 - round(temp_g * 255))
                    b.append(255 - round(temp_b * 255))
                #if the program is not set to inversion mode, append the normal rgb values to r, g, b
                else:
                    #temp_r is multiplied from its float value and rounded to fit the 0-225 rgb format
                    r.append(round(temp_r * 255))
                    g.append(round(temp_g * 255))
                    b.append(round(temp_b * 255))
        #if the above code doesn't work, it is because the file is either not a png, or has no opacity value in rgb
        except:
            #return an error message and end the program
            print("File not Supported")
            sys.exit(1)
    #return the arrays r, g, b if the program runs smoothly
    return r, g, b

#find the dimensions of the image
def findWidth():
    #find the dimensions of the image that was specified in argument 1
    img = pilmager.open(sys.argv[1])
    return img.size

#get the ansi string for the specific RGB color and return it.
def get_color_escape(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

#clear the screen of any previous commands and text on the terminal
def clearScreen():
    os.system('cls')

#run the main method.
if (__name__ == "__main__"):
  main()