import os
import numpy as np
import cv2


filename = 'video.avi'
frames_per_seconds = 24.0
my_res = '720p' #1080p

def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

STD_DIMENSION = {
    "480p" : (640, 480),
    "720p" : (1280, 720),
    "1080p" : (1920, 1080),
    "4K":   (3340, 2160),
}

def get_dims(cap, res='1080p'):
    width, height = STD_DIMENSION['480p']
    if res in STD_DIMENSION:
        width, height = STD_DIMENSION[res]
    change_res(cap, width, height)
    return width, height

VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc('M','J','P','G'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
    # 'avi': cv2.VideoWriter_fourcc(*'XVID'),
}

def get_video_type(filename) :
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']

cap = cv2.VideoCapture(0)
dims = get_dims(cap, res=my_res)
vidoe_type_cv2 = get_video_type(filename)

out = cv2.VideoWriter(filename, vidoe_type_cv2, frames_per_seconds, dims)
print ("this is a tuple: %s" %(dims,))

change_res(cap, dims[0], dims[1])

while(True):
    ret, frame = cap.read()
    out.write(frame)

    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()