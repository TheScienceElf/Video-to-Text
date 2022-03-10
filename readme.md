# Color Video to Text Conversion

A few tools to convert video and images into ASCII art in an ANSI terminal. These tools support color output using the ANSI 256 color set, as well as the creation of a self-contained playback executable for video converted to text, with compression able to fit 4 minutes of 80 column 15 FPS video onto a single floppy disk!

 ## Check out [this video](https://www.youtube.com/watch?v=uGoR3ZYZqjc) for more information and to see sample output for video to text conversion.

![Screenshot](screenshot.png)

A sample image converted to text and printed to the terminal.

---

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
The provided makefile allows building programs which will play the compressed text encoding of the video stored in the executable. The target video should be named `vid.mp4`, otherwise the path to the video can be changed in the header of convert.py.

To build for Linux targets (using GCC) run 

`make playback`

Otherwise to build for Windows targets (using MinGW) run 

`make playback.exe`

Other aspects of the video encoding, such as character width and framerate can be adjusted in both convert.py and playback.c. **Be sure to update these parameters in both files.**
