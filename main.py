from flask import Flask, render_template, Response, request, send_from_directory, jsonify
from camera import VideoCamera
import cv2
import os
import json

pi_camera = VideoCamera(flip=False) # flip pi camera if upside down.

# App Globals (do not edit)
app = Flask(__name__)

#============================= Global Variables =======================#
configuration_path = os.path.join('./configuration.json')
video_path = os.path.join('./video')
image_path = os.path.join('./picture')

email =""
start_time = ""
end_time = ""
current_name = ""
is_train_model = False

#============================= App routes =============================#
@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Take a photo when pressing camera button
@app.route('/takePicture')
def take_picture():
    owner_pic_path = '/dataset/'+current_name + '/'
    pi_camera.take_picture(owner_pic_path)
    return 'OK',200

@app.route('/streaming')
def streaming():
    print('[INFO] App streaming')
    return render_template('streaming.html')

@app.route('/recording')
def recording():
    print('[INFO] App recording')
    return render_template('recording.html')

@app.route('/setting')
def setting():
    print('[INFO] App setting')
    return render_template('setting.html')

@app.route('/login', methods=['POST'])
def login():
    print('[INFO] App login')
    return render_template('streaming.html')

@app.route('/listVideo')
def listVideo():
    print('[INFO] App get listVideo')
    _list_video = getListVideo()
    return jsonify({'data': _list_video})

@app.route('/trainModel')
def trainModel():
    print('[INFO] App train model')
    return 'OK',200

@app.route('/settingTimes', methods=['GET'])
def settingTimes():
    print('[INFO] setting time')
    start_time = request.args.get('startTime')
    stop_time  = request.args.get('stopTime')
    update_config_time(start_time,stop_time)
    return 'OK',200

@app.route('/settingOwner', methods=['GET'])
def settingOwner():
    print('[INFO] App Setting owner')
    _user_name = request.args.get('name')
    _email = request.args.get('email')
    if(update_config_owner(_user_name,_email)):
        return 'OK',200
    else:
        return 'Owner exists',404

@app.route('/display_video', methods=['GET'])
def display_video():
    _video_name = request.args.get('video_name')
    _video = video_path + '/' + _video_name
    print('[INFO] display_video' , _video )
    return Response(generate_frames(_video), mimetype='multipart/x-mixed-replace; boundary=frame')


#============================= functions =============================#
def gen(camera):
    #get camera frame
    print("[INFO] Streaming camera")
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def generate_frames(video_path):
    print("[INFO] Streaming video")
    video_capture = cv2.VideoCapture(video_path)
    while True:
        success, frame = video_capture.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def read_config():
    print('[Info] reading config file')
    with open(configuration_path, 'r') as file:
        config = json.load(file)
    print('[Info] config file: {}'.format(config))

def update_config_owner(owner, email):
    print('[Info] updating config owner')
    ret_val = False
    with open(configuration_path, 'r') as file:
        config = json.load(file)
    
    config['email'] = email
    if(not_exists_name(owner))
        config['name'] = owner
        ret_val = True

    with open(configuration_path, 'w') as file:
        json.dump(config,file,indent=2)
    
    return ret_val
    

def not_exists_name(new_name):
    imagePaths = list(paths.list_images("dataset"))
    for (i, imagePath) in enumerate(imagePaths):
        # extract the person name from the image path
        print("[INFO] processing image {}/{}".format(i + 1,len(imagePaths)))
        name = imagePath.split(os.path.sep)[-2]
        if name == new_name
            return False
    return True


def update_config_time(start_time, end_time):
    print('[Info] updating config time')
    with open(configuration_path, 'r') as file:
        config = json.load(file)

    config['time']['start_time'] = start_time
    config['time']['end_time'] = end_time

    with open(configuration_path,'w') as file:
        json.dump(config,file,indent=2)

def save_video():
    print('[Info] Saving video')

def getListVideo():
    print('[Info] get list video')
    _list_video_path = os.listdir(video_path)
    print('List', _list_video_path)
    return _list_video_path

# def face_detect():
#     while True:
#         pi_camera.face_detect()
#         return "None"

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
