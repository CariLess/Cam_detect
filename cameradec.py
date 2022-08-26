import cv2

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
   
    cv2.imshow('Input', frame)

    if cv2.waitKey(25) == 32:
        break

cap.release()
cv2.destroyAllWindows()