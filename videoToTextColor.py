import numpy as np
import cv2
import pickle
import sys

aspect_ratio = 16 / 9

# Dimensions of the output in terminal characters
width = 80
height = int(width / (2 * aspect_ratio))


# Our characters, and their approximate brightness values
charSet = " ,(S#g@@g#S(, "

# Generates a character sequence to set the foreground and background colors
def setColor (bg, fg):
    return "\u001b[48;5;%s;38;5;%sm" % (bg, fg)

black = setColor(16, 16)

# Load in color lookup table data
lerped = pickle.load(open("colors.pkl", "rb"))
LUT = np.load("LUT.npy")

# Convert an RGB image to a stream of text with ANSI color codes
def convertImg(img):
    line = ""
    for row in img:
        for color in row:
            color = np.round(color).astype(int)

            b, g, r = color[0], color[1], color[2]

            # Lookup the color index in the RGB lookup table
            idx = LUT[b, g, r]
        
            # Get the ANSI color codes and lerp character
            bg, fg, lerp, rgb = lerped[idx]

            char = charSet[lerp]
        
            line += "%s%c" % (setColor(bg, fg), char)
        # End each line with a black background to avoid color fringe
        line += "%s\n" % black
    
    # Move the cursor back to the top of the frame to prevent rolling
    line += "\u001b[%iD\u001b[%iA" % (width, height + 1)
    return line


if len(sys.argv) == 2:
    cap = cv2.VideoCapture(sys.argv[1])

    while(cap.isOpened()):  
        ret, frame = cap.read()

        if frame is None:
            break
        
        img = cv2.resize(frame, (width, height))
        print(convertImg(img))
else:
  print("Expected video file as argument.")

