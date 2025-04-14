import cv2
import face_recognition
import pyttsx3
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
voicespeed = 150
engine.setProperty('rate', voicespeed)

def speak(audio) :
  engine.say(audio)
  engine.runAndWait()

authorized_images = [# add images to give access ]

known_face_encodings = []
known_face_names = []

for img_path in authorized_images:
    image = face_recognition.load_image_file(img_path)
    encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(encoding)
    known_face_names.append(img_path)  

face_locations = []
face_encodings = []
access_granted = False


video_capture = cv2.VideoCapture(0)


    
ret, frame = video_capture.read()

    
small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    
rgb_small_frame = small_frame[:, :, ::-1]

    
face_locations = face_recognition.face_locations(rgb_small_frame)
face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
print("done before loop")

for face_encoding in face_encodings:
        print("done after loop")
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"
        s_name = ""
        
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index] 
            access_granted = True
            print("Access Granted ")
            speak("welcome back")
           
        else:
            access_granted = False
            print("Access Denied")
            speak("who are you")
            speak("identify yourself")
            cv2.imwrite(f"{random.randint(1,9999999999999)}.jpg",frame)

video_capture.release()
cv2.destroyAllWindows()
