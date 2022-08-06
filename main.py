import cv2 as cv

cap = cv.VideoCapture(0)
#cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
#cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)


while(cap.isOpened()):
    _, frame = cap.read()
    hsvFrame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    height, width, _ = frame.shape
    centerX = int(width / 2)
    centerY = int(height / 2)

    centerPixel = hsvFrame[centerY, centerX]
    #print(centerPixel)

    hVal = centerPixel[0]
    centerPixelBGR = frame[centerY, centerX]
    b, g, r = int(centerPixelBGR[0]), int(centerPixelBGR[1]), int(centerPixelBGR[2])

    color = 'Undefined'
    if(hVal < 5):
        color = 'Red'
    elif(hVal < 22):
        color = 'Orange'
    elif(hVal < 32):
        color = 'Yellow'
    elif(hVal < 78):
        color = 'Green'
    elif(hVal < 130):
        color = 'Blue'
    elif(hVal < 170):
        color = 'Violet'
    else:
        color = 'Red'

    cv.putText(frame, color, (10, 50), 0, 1, (b, g, r), 2)
    cv.circle(frame, (centerX, centerY), 5, (0, 0, 0), 3)


    cv.imshow('frame', frame)

    key = cv.waitKey(1)
    if(key == 27):
        print('bye')
        break

cap.release()
cv.destroyAllWindows()