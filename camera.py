import cv2 as cv
from imutils.video.pivideostream import PiVideoStream
import imutils
from imutils import paths
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
    def __init__(self, flip = False, file_type  = ".jpg", photo_string= "stream_photo", video_type=".mp4"):
        # self.vs = PiVideoStream(resolution=(1920, 1080), framerate=30).start()
        self.vs = PiVideoStream().start()
        self.flip = flip # Flip frame vertically
        self.file_type = file_type # image type i.e. .jpg
        self.photo_string = photo_string # Name to save the photo
        self.is_streaming = True
        self.is_recoding = False
        self.send_message_counters = 0
        self.out = None
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
    def take_picture(self, path):
        frame = self.flip_if_needed(self.vs.read())
        ret, image = cv.imencode(self.file_type, frame)
        today_date = datetime.now().strftime("%m%d%Y-%H%M%S") # get current time
        if path:
            file_path = path + f"{self.photo_string}_{today_date}{self.file_type}"
            print("File path: " + file_path)
        else:
            file_path = f"./picture/stranger_people{self.file_type}"
        cv.imwrite(file_path,frame)

    def check_time(self, start_time, end_time):
        _start_time = datetime.strptime(start_time, "%H:%M").time()
        _end_time = datetime.strptime(end_time, "%H:%M").time()
        current_time = datetime.now().time()
        if _start_time < current_time < _end_time:
            return True
        else:
            return False

    def start_recording(self):
        print("Starting recording")
        is_recoding = True
        # today_date = datetime.now().strftime("%m%d%Y") # get current time
        # video_path = f"./video/{today_date}{self.file_type}"
        # fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # You can change the codec as needed
        # self.out = cv2.VideoWriter(video_path, fourcc, 20.0, (640, 480))  # Adjust parameters accordingly
    
    def stop_recording(self):
        print("Stop recording")
        # if self.out:
        #     self.out.release()

    def is_sendEmails(self):
        if (self.send_message_counters > 5)
            return True
        else:
            return False
    def clear_flag_sendMails(self):
        self.send_message_counters = 0

    # Detect faces
    def detect_faces(self, start_time, end_time):
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
                self.send_message_counters += 1
                print("Nguoi la xuat hien")
        if (check_time(start_time,end_time)):
            # Record video while face is detected
            if not self.out:
                self.start_recording()

            # Write the frame to the video file
            self.out.write(frame)
        else:
            if is_recoding
                stop_recording()
                is_recoding = False
