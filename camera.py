import cv2 as cv
from imutils.video.pivideostream import PiVideoStream
import imutils
import face_recognition
import pickle 
import time
from datetime import datetime
import numpy as np

#Determine faces from encodings.pickle file model created from train_model.py 
encodingsP = "encodings.pickle" 
# load the known faces and embeddings along with OpenCV's Haar # cascade for face detection 
print("[INFO] loading encodings + face detector...") 
data_model = pickle.loads(open(encodingsP, "rb").read()) 

class VideoCamera(object):
    def __init__(self, flip = False, file_type  = ".jpg", photo_string= "stream_photo"):
        # self.vs = PiVideoStream(resolution=(1920, 1080), framerate=30).start()
        self.vs = PiVideoStream().start()
        self.flip = flip # Flip frame vertically
        self.file_type = file_type # image type i.e. .jpg
        self.photo_string = photo_string # Name to save the photo
        self.is_streaming = True
        time.sleep(2.0)

    def __del__(self):
        self.vs.stop()

    def flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame

    def get_frame(self):
        frame = self.flip_if_needed(self.vs.read())
        ret, jpeg = cv.imencode(self.file_type, frame)
        self.previous_frame = jpeg
        return jpeg.tobytes()

    # Take a photo, called by camera button
    def take_picture(self, path=None):
        frame = self.flip_if_needed(self.vs.read())
        ret, image = cv.imencode(self.file_type, frame)
        today_date = datetime.now().strftime("%m%d%Y-%H%M%S") # get current time
         if path:
            file_path = path + f"{self.photo_string}_{today_date}{self.file_type}"
        else:
            file_path = f"{"./picture/"}{self.photo_string}_{today_date}{self.file_type}"
        cv.imwrite(str(self.photo_string + "_" + today_date + self.file_type), frame)

    # Detect faces
    def detect_faces(self):
        frame = self.flip_if_needed(self.vs.read())
        # Detect the fce boxes 
        boxes = face_recognition.face_locations(frame)
        # compute the facial embeddings for each face bounding box
        encodings = face_recognition.face_encodings(frame, boxes)
        names = []
        print("Beginning face detection")
        # loop over the facial embeddings
        for encoding in encodings:
            # attempt to match each face in the input image to our known
            # encodings
            matches = face_recognition.compare_faces(data_model["encodings"],encoding)
            name = "Unknown" #if face is not recognized, then print Unknown
            if True in matches:
                print("Có nguoi quen")
            else:
                take_picture()
                print("Nguoi la xuat hien")
    
