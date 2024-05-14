import cv2
from pyzbar.pyzbar import decode
import time
import json


def get_id(qrcode):
    json_qr = json.loads(qrcode)

    if json_qr['elem']['u']:
        u_value = json_qr['elem']['u']
        after_dot = u_value.split('.')[1]
        peppi_id = int(after_dot)

        return peppi_id


cam = cv2.VideoCapture(0)

camera = True
while camera == True:
    suceess, frame = cam.read()

    for i in decode(frame):
        qrcode = i.data.decode("utf-8")

        try:
            w = get_id(qrcode)
            print(w)
            time.sleep(1)
        except:
            print("not correct qrcode")

    cv2.imshow("scan qrcode", frame)
    cv2.waitKey(1)


