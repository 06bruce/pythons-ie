# Importing the required packages
import pyautogui
import cv2
import numpy as np

# Define constants
RESOLUTION = (1920, 1080)
CODEC = cv2.VideoWriter_fourcc(*"XVID")
FILENAME = "Recording.avi"
FPS = 60.0

# Create a VideoWriter object
out = cv2.VideoWriter(FILENAME, CODEC, FPS, RESOLUTION)

# Create a window with a title and resize it
cv2.namedWindow("Screen Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Screen Recording", 480, 270)

while True:
    # Take a screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Convert it from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write it to the output file
    out.write(frame)

    # Display the recording screen
    cv2.imshow('Screen Recording', frame)

    # Check for the 'q' key press to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the Video writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()