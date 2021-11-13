import numpy as np
import cv2

# img = cv2.imread('new.png', -1)  # display image
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) # resize image
# img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # rotate image

vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = vid.read()

    
    # img = cv2.resize(frame, (0, 0), fx=0.5, fy=1)
    frame = cv2.flip(frame, 1) # flip image
    # frame = cv2.line(frame, (0, 0), (width, height), (0, 255, 0), 1) # draw line on screen 
    # frame = cv2.rectangle(frame, (0, 0), (width, height), (0, 255, 0), 1) # draw rectangle on screen 
    # frame = cv2.circle(frame, (200, 200), 100, (0, 0, 0), -1) # draw circle on screen 
    # font = cv2.FONT_HERSHEY_SIMPLEX # initalize font
    # img = cv2.putText(frame, 'your mom', (100, 100), font, 1, (75, 95, 61), 1, cv2.LINE_AA)  # put text on screen

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ey, ey+eh), (0, 255, 0), 5)


    cv2.imshow('frame', frame) # show video on screen
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # close window if button pressed
        break
    if cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) <1:
        break


vid.release()

# cv2.imshow('Image', img)
# cv2.waitKey(0) # wait till any key pressed
cv2.destroyAllWindows() # close window


