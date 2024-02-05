# raspberryPi_camera_streanming
This is project using raspberry pi and python flask and camera pi
1. Init repo
   If this is first init, please follow step below
   ```bash
     cd pi
     mkdir camera_stream
     cd camera_stream
     git clone "https://github.com/Xuantuanncth/raspberryPi_camera_streanming.git"
   ```
2. Setup enviroiment
 - Install python
 - Install opencv for raspberry pi
   https://raspberrypi-guide.github.io/programming/install-opencv
 - Install face recognition
   https://github.com/ageitgey/face_recognition/tree/master
 - Install Imutils
   ```
   pip install imutils
   ```

3. Run
  ```
  cd camera_stream/raspberryPi_camera_streanming
  python main.py
  ```

4. Feature

5. Document 
  Face recognition:
  - https://face-recognition.readthedocs.io/en/latest/readme.html
  - https://vis-www.cs.umass.edu/lfw/

  Raspberry Pi + Camera Pi
  - https://projects.raspberrypi.org/en/projects/getting-started-with-picamera

  SMTP Server (Send mail)
  - https://docs.python.org/3/library/smtplib.html
  - https://randomnerdtutorials.com/raspberry-pi-send-email-python-smtp-server/

  Python Flask
  - https://flask.palletsprojects.com/en/3.0.x/

  Web API documentation
  - https://developer.mozilla.org/en-US/docs/Web/API/Document

