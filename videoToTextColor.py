import numpy as np
import cv2
import pickle
import sys

ASPECT_RATIO = 16 / 9

# Dimensions of the output in terminal characters
WIDTH = 80
HEIGHT = int(WIDTH / (2 * ASPECT_RATIO))


# Our characters, and their approximate brightness values
CHARSET = " ,(S#g@@g#S(, "

# Generates a character sequence to set the foreground and background colors
def setColor(bg, fg):
    return "\u001b[48;5;%s;38;5;%sm" % (bg, fg)

BLACK = setColor(16, 16)

# Load in color lookup table data
with open("colors.pkl", "rb") as f:
    LERPED = pickle.load(f)
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
            bg, fg, lerp, rgb = LERPED[idx]

            char = CHARSET[lerp]
        
            line += "%s%c" % (setColor(bg, fg), char)
        # End each line with a black background to avoid color fringe
        line += "%s\n" % BLACK
    
    # Move the cursor back to the top of the frame to prevent rolling
    line += "\u001b[%iD\u001b[%iA" % (WIDTH, HEIGHT + 1)
    return line


if len(sys.argv) == 2:
    cap = cv2.VideoCapture(sys.argv[1])

    while(cap.isOpened()):  
        ret, frame = cap.read()

        if frame is None:
            break
        
        img = cv2.resize(frame, (WIDTH, HEIGHT))
        print(convertImg(img))
else:
  print("Expected video file as argument.")

