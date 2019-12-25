import cv2 as cv


def face_detect_dome(src):
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier(
        'D:\\Language\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_alt_tree.xml')
    faces = face_detector.detectMultiScale(gray, 1.02,5)
    for x, y, w, h in faces:
        cv.rectangle(src, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv.imshow('result:', src)


src = cv.imread('D:\\Pro\\WorkPro\\DataAnalYsis\\face_pro\\jiejie.jpg')
cv.imshow('yuan_tu_1', src)
cv.namedWindow('yuan_tu_2', cv.WINDOW_NORMAL)
face_detect_dome(src)
cv.waitKey()
cv.destroyAllWindows()
