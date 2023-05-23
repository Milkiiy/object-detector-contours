import cv2
from tracking import *

# membuat objek tracker

tracking = EuclideanDistTracker()


cap = cv2.VideoCapture("Videos/kendaraan2.mp4")

# Deteksi objek dari kamera

object_detector = cv2.createBackgroundSubtractorMOG2(
    history=100, varThreshold=40)

while True:
    ret, frame = cap.read()

    height, width, _ = frame.shape

    # Mengambil bagian yang diinginkan

    roi = frame[340:720, 100:1200]

    # MEndeteksi Objek
    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(
        mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []

    for cnt in contours:
        # MEnghitung area dan hapus element2 kecil

        area = cv2.contourArea(cnt)
        if area > 100:
             #cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)

            x, y, w, h = cv2.boundingRect(cnt)
            #cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)

            detections.append([x, y, w, h])

    # Menghitung Objek yang terdeteksi

    boxes_ids = tracking.update(detections)
    for box_id in boxes_ids:
         x, y, w, h, id = box_id
          #cv2.putText(frame, "Vehicle", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2, cv2.LINE_AA)

         #cv2.putText(roi, "Vehicle", (x, y - 5),
                     #cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
         cv2.putText(roi, str(id), (x, y - 15),
          cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
         cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("roi", roi)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(30)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
