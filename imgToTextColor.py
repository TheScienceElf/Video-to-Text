import numpy as np
import pickle

# Load in color lookup table data
with open('colors.pkl', 'rb') as f:
    LERPED = pickle.load(f)
LUT = np.load('LUT.npy')


def set_color(bg, fg):
    '''
        Generates a character sequence to set the foreground
        and background colors
    '''
    return f'\u001b[48;5;{bg};38;5;{fg}m'


def convert_img(img, charset=' ,(S#g@@g#S(, ', width=80, height=1):
    '''
        Convert an RGB image to a stream of text with ANSI color codes
    '''

    line = ''

    for row in img:
        for color in row:
            color = np.round(color).astype(int)

            b, g, r = color[0], color[1], color[2]

            # Lookup the color index in the RGB lookup table
            idx = LUT[b, g, r]

            # Get the ANSI color codes and lerp character
            bg, fg, lerp, rgb = LERPED[idx]

            char = charset[lerp]

            line += set_color(bg, fg) + char
        # End each line with a black background to avoid color fringe
        line += '\u001b[48;5;16;38;5;16m\n'

    # Move the cursor back to the top of the frame to prevent rolling
    line += f'\u001b[{width}D\u001b[{height + 1}A'
    return line


if __name__ == '__main__':
    import cv2
    import sys

    # Width of the output in terminal characters
    WIDTH = 80
    HEIGHT = 1

    if len(sys.argv) == 2:
        img = cv2.imread(sys.argv[1])

        # Match the aspect ratio to that of the provided image
        src_height, src_width, _ = img.shape

        aspect_ratio = src_width / src_height
        HEIGHT = int(WIDTH / (2 * aspect_ratio))

        img = cv2.resize(img, (WIDTH, HEIGHT))
        print(convert_img(img, width=WIDTH, height=HEIGHT))
    else:
        print('Expected image file as argument.')
