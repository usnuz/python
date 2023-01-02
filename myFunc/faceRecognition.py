import cv2
'''pip install opencv-python'''
import face_recognition
'''for linux or mac not windows
pip install face-recognition'''


def face(first_img, second_img):
    img = cv2.imread(first_img)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_encoding = face_recognition.face_encodings(rgb_img)[0]

    img2 = cv2.imread(second_img)
    rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

    result = face_recognition.compare_faces([img_encoding], img_encoding2)
    return result


a = "media/2.jpg"
b = "media/1.jpg"

print(face(a, b))
