import numpy as np

import cv2
import pickle

from utils import CFEVideoConf, image_resize

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascades/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascades/haarcascade_eye.xml')
# smile_cascade = cv2.CascadeClassifier('cascades/data/haarcascades/haarcascade_smile.xml')
nose_cascade = cv2.CascadeClassifier('cascades/third-party/Nose18x15.xml')
glasses = cv2.imread("images/fun/glasses.png", -1);
mustache = cv2.imread("images/fun/mustache.png", -1);

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"person_name": 1}
with open("labels.picle", "rb") as f: 
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

cap = cv2.VideoCapture(0) 

while(True) :
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    for(x, y, w, h) in faces:
        # print(x, y, w, h)
        roi_gray = gray[y:y+h, x:x+w] #(ycord1_start, ycord_end)
        roi_color = frame[y:y+h, x:x+w]
        # cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 3)

        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=5)
        for (ex, ey, ew, eh) in eyes:
            # cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 255), 3)
            roi_eyes = roi_gray[ey: ey + eh, ex: ex + ew]
            glasses2 = image_resize(glasses.copy(), width = ew)

            gw, gh, gc = glasses2.shape
            for i in range(0, gw):
                for j in range(0, gh):
                    if glasses2[i, j][3] != 0: # alpha 0 
                        roi_color[ey + int(eh/4.0) + i, ex + j] = glasses2[i, j]

        nose = nose_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=5)
        for (nx, ny, nw, nh) in nose:
            # cv2.rectangle(roi_color, (nx, ny), (nx + nw, ny + nh), (255, 0, 0), 3)
            roi_nose = roi_gray[ny: ny + nh, nx: nx + nw]
            mustache2 = image_resize(mustache.copy(), width = nw)
            
            mw, mh, mc = mustache2.shape
            for i in range(0, mw):
                for j in range(0, mh):
                    if mustache2[i, j][3] != 0: # alpha 0 
                        roi_color[ny + int(nh/2.0) + i, nx + j] = mustache[i, j]
            break;

        # recognize? deep learned model predict keras tensorflow pytorch scikit learn.
        id_, conf = recognizer.predict(roi_gray)

        if conf >= 4:
            print(id_)
            print(labels[id_])
            font = cv2.FONT_HERSHEY_COMPLEX
            name = labels[id_]
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

        # img_item = "5.png"
        # cv2.imwrite(img_item, roi_color)

        color = (255, 0, 0) #BGR 0-255
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        # cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
        # smiles = smile_cascade.detectMultiScale(roi_gray)
        # for(smx, smy, smw, smh) in smiles:
        #     cv2.rectangle(roi_color, (smx, smy), (smx+smw, smy+smh), (0, 255, 0), 2)
        # eyes = eye_cascade.detectMultiScale(roi_gray)
        # for(ex, ey, ew, eh) in eyes:
        #     cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    #Display the resulting frame
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


# When everything done, realease the capture
cap.release()
cv2.destroyAllWindows