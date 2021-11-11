import numpy as np
import cv2

# img = cv2.imread('new.png', -1)  # display image
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) # resize image
# img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # rotate image

vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = vid.read()
    width = int(vid.get(3))
    height = int(vid.get(4))
    
    # img = cv2.resize(frame, (0, 0), fx=0.5, fy=1)
    frame = cv2.flip(frame, 1) # flip image
    # frame = cv2.line(frame, (0, 0), (width, height), (0, 255, 0), 1) # draw line on screen 
    frame = cv2.rectangle(frame, (0, 0), (width, height), (0, 255, 0), 1) # draw rectangle on screen 
    frame = cv2.circle(frame, (200, 200), 100, (0, 0, 0), -1) # draw circle on screen 
    font = cv2.FONT_HERSHEY_SIMPLEX # initalize font
    img = cv2.putText(frame, 'your mom', (100, 100), font, 1, (75, 95, 61), 1, cv2.LINE_AA)  # put text on screen


    cv2.imshow('frame', frame) # show video on screen
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # close window if button pressed
        break

vid.release()

# cv2.imshow('Image', img)
# cv2.waitKey(0) # wait till any key pressed
cv2.destroyAllWindows() # close window


