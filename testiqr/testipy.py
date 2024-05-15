import cv2
# from pyzbar.pyzbar import decode
import time
import json
from qrdet import QRDetector
from qreader import QReader


def get_id(qrcode):
    json_qr = json.loads(qrcode)

    if json_qr['elem']['u']:
        u_value = json_qr['elem']['u']
        after_dot = u_value.split('.')[1]
        peppi_id = int(after_dot)

        return peppi_id


cam = cv2.VideoCapture(0)
detector = QRDetector(model_size='s')
qreader = QReader(model_size='s')
cv_decoder = cv2.QRCodeDetector()

camera = True
while camera == True:
    success, frame = cam.read()

    if success:
        outputs = qreader.detect_and_decode(frame)
        print(outputs)
        # detections = detector.detect(image=frame, is_bgr=True)
        # print(detections)
        # # print(data)
        # for detection in detections:
        #     x1, y1, x2, y2 = detection['bbox_xyxy']
        #     im = frame[x1:x2, y1:y2]
        #     data, bbox = cv_decoder.decode(im)

        # # for i in decode(frame):
        # #     qrcode = i.data.decode("utf-8")
        for data in outputs:
            try:
                w = get_id(data)
                print(w)
                time.sleep(1)
            except:
                print("not correct qrcode")

    cv2.imshow("scan qrcode", frame)
    if cv2.waitKey(1) == ord("q"): 
        break


