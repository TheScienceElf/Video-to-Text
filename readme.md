# Color Video to Text Conversion

A few tools to convert video and images into ASCII art in an ANSI terminal. These tools support color output using the ANSI 256 color set, as well as the creation of a self-contained playback executable for video converted to text, with compression able to fit 4 minutes of 80 column 15 FPS video onto a single floppy disk!

 ## Check out [this video](https://www.youtube.com/watch?v=rY413t5fArw) for more information and to see sample output for video to text conversion.

![Screenshot](screenshot.png)

A sample image converted to text and printed to the terminal.

**Note:** To run these programs, you will need Python 3 installed, alongside NumPy and OpenCV (for image io).

## Displaying Images as Text
The python script imageToTextColor.py will print an image file provided as an argument as text to the terminal.

`python3 imageToTextColor.py your_image_here.jpg`

The width of the output can be configured in the header of the python file.

## Displaying Videos as Text
The python script videoToTextColor.py will play back a video provided as an argument as text to the terminal.

`python3 videoToTextColor.py your_video_here.mp4`

The width and aspect ratio of the output can be configured in the header of the python file.


## Creating Video Playback Executables






**Warning:** This program takes a while to complete, and once started cannot be interrupted until it is finished. Every once in a while, it can also freeze up. If for any reason you need to quit the program, **you will need to reset your calculator**, which will clear any unarchived data in RAM. Make sure you don't have anything unarchived that you wouldn't be willing to lose before running this program.

## Building Locally
This program appears to have some compatibility issues with the latest version of the toolchain, however version 9.1 still appears to be functional.