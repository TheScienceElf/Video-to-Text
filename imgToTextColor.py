import numpy as np
import cv2
import pickle
import sys

# Width of the output in terminal characters
WIDTH = 80
HEIGHT = 1 


# Our characters, and their approximate brightness values
CHARSET = " ,(S#g@@g#S(, "

def setColor (bg, fg):
    """
        Generates a character sequence to set the foreground and background colors
    """
    return "\u001b[48;5;%s;38;5;%sm" % (bg, fg)

BLACK = setColor(16, 16)

# Load in color lookup table data
with open("colors.pkl", "rb") as f:
    LERPED = pickle.load(f)
LUT = np.load("LUT.npy")

def convertImg(img):
    """
        Convert an RGB image to a stream of text with ANSI color codes
    """
    
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
    img = cv2.imread(sys.argv[1])

    # Match the aspect ratio to that of the provided image
    src_height, src_width, _ = img.shape

    aspect_ratio = src_width / src_height
    HEIGHT = int(WIDTH / (2 * aspect_ratio))

    img = cv2.resize(img, (WIDTH, HEIGHT))
    print(convertImg(img))
else:
    print("Expected image file as argument.")
