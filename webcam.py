import cv2

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while(True):
	ret, frame = cap.read()
	f1 = cv2.flip(frame,1)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(
		gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30)
	)
	print("Found {0} faces!".format(len(faces)))
	for (x, y, w, h) in faces:
		cv2.rectangle(f1, (x, y), (x+w, y+h), (0, 255, 0), 2)
	cv2.imshow('frame', f1)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()