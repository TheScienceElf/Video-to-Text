from imgToTextColor import set_color, convert_img

if __name__ == "__main__":
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

    BLACK = set_color(16, 16)

    # Load in color lookup table data
    with open("colors.pkl", "rb") as f:
        LERPED = pickle.load(f)
    LUT = np.load("LUT.npy")

    if len(sys.argv) == 2:
        cap = cv2.VideoCapture(sys.argv[1])

        while cap.isOpened():
            ret, frame = cap.read()

            if frame is None:
                break
            
            img = cv2.resize(frame, (WIDTH, HEIGHT))
            print(convert_img(img))
    else:
        print("Expected video file as argument.")
