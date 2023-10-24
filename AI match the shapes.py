import cv2
import numpy as np


def getcontour(img):
    contours , hierarchy = cv2.findContours(img , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            cv2.drawContours(imgcontour , cnt , -1 , (255 , 0 , 0) , 1)
            per = cv2.arcLength(cnt , True)
            approx = cv2.approxPolyDP(cnt , 0.02*per , True)
            obj = len(approx)
            x , y , w , h = cv2.boundingRect(approx)
            objectal = "none"
            if obj ==3 :
                objectal = "tri"
            elif obj ==4 :
                asp = w/float(h) 
                if asp > 0.95 and asp < 1.05:
                    objectal = "square"
                else:
                    objectal = "rect"
            elif obj >4 :
                objectal = "circle"
            elif obj ==3 :
                objectal = "tri"
            cv2.rectangle(imgcontour , (x , y) , (x+w , y+h) , (0 , 150 , 255) , 1)
            cv2.putText(imgcontour, objectal , ( x + (w//2) -10 , y +(h//2) -10) , cv2.FONT_HERSHEY_COMPLEX , 0.5, (0 , 0 , 0) , 1)
            app = [x + (w//2) -10 , y +(h//2) -10 , objectal]
            try:
                shape.append(app)
            except:
                pass

def liner(img , shap):
    n = len(shap)
    e = n/2
    i = 1
    w = []
    sq = []
    while i <= n:
        w.append(shap[i-1][2])
        i+=1
    print(w)
    s = 1
    while s <= e:
        try:
            sq.append([w.index(w[s-1]) , w.index(w[s-1] , 4)])
        except:
            pass
        print(sq)
        s +=1
    for ss in sq:
        cv2.line(img , (shap[ss[0]][0],shap[ss[0]][1]) , (shap[ss[1]][0],shap[ss[1]][1]) ,(255 , 0 , 0) , 2)

shape = []
img = cv2.imread("shape.png")
imgo = cv2.resize(img , (200 , 400))
imgcontour = img.copy()
imggray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(imggray , (7,7) , 1)
cannyimg = cv2.Canny(imgblur, 50 , 50 )
getcontour(cannyimg)
print(shape)
liner(imgcontour , shape)
imgh = np.hstack((imggray , imgblur))
cv2.imshow("canny image" , cannyimg)
cv2.imshow("images"  , imgh)
cv2.imshow("image"  , imgcontour)
cv2.imshow("iage"  , img)
cv2.waitKey(0)

input()