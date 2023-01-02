import qrcode
'''pip install qrcode'''
import cv2
'''pip install opencv-python'''


def create_qr(file_name, qr_text):
    qr = qrcode.make(qr_text)
    qr.save(f'{file_name}.png')
    return f'{file_name}.png'


def read_qr(img_path):
    d = cv2.QRCodeDetector()
    url, _, _ = d.detectAndDecode(cv2.imread(img_path))
    return url

