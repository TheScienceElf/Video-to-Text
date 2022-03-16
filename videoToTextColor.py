from imgToTextColor import convert_img

if __name__ == '__main__':
    import cv2
    import sys

    ASPECT_RATIO = 16 / 9

    # Dimensions of the output in terminal characters
    WIDTH = 80
    HEIGHT = int(WIDTH / (2 * ASPECT_RATIO))

    if len(sys.argv) == 2:
        if sys.argv[1].startswith("cam:"):
            cap = cv2.VideoCapture(int(sys.argv[1][4:]))
        else:
            cap = cv2.VideoCapture(sys.argv[1])

        while cap.isOpened():
            ret, frame = cap.read()

            if frame is None:
                break

            img = cv2.resize(frame, (WIDTH, HEIGHT))
            print(convert_img(img, width=WIDTH, height=HEIGHT))
    else:
        print('Expected video file or webcam ID ("cam:n", \
              where n is the camera index, starting with 0) as argument.')
