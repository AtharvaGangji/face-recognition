import numpy as np
import cv2

# img = cv2.imread('new.png', -1)  # display image
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) # resize image
# img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # rotate image

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    
    # img = cv2.resize(frame, (0, 0), fx=0.5, fy=1)
    frame = cv2.flip(frame, 1) # flip image

    cv2.imshow('frame', frame) # show video on screen
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # close window if button pressed
        break

cap.release()

# cv2.imshow('Image', img)
# cv2.waitKey(0) # wait till any key pressed
cv2.destroyAllWindows() # close window


