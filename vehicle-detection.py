import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

cap=cv2.VideoCapture(0)

while True:

    ret,frame=cap.read()

    if not ret:
        break


    bbox,label,conf = cv.detect_common_objects(
        frame,
        confidence=0.3,
        model='yolov4-tiny'
    )


    vehicle_count=0

    vehicle_labels=[

    "car",
    "bus",
    "truck",
    "motorcycle"

    ]


    for x in label:

        if x in vehicle_labels:

            vehicle_count+=1


    output=draw_bbox(
        frame,
        bbox,
        label,
        conf
    )


    cv2.putText(

        output,

        f"Vehicles: {vehicle_count}",

        (20,40),

        cv2.FONT_HERSHEY_SIMPLEX,

        1,

        (0,255,0),

        2

    )


    if vehicle_count>10:

        level="Heavy Traffic"

    elif vehicle_count>5:

        level="Moderate Traffic"

    else:

        level="Low Traffic"


    cv2.putText(

        output,

        level,

        (20,80),

        cv2.FONT_HERSHEY_SIMPLEX,

        1,

        (0,0,255),

        2

    )


    cv2.imshow(
        "Smart Traffic Detection",
        output
    )


    key=cv2.waitKey(1)

    if key==27:
        break


cap.release()

cv2.destroyAllWindows()