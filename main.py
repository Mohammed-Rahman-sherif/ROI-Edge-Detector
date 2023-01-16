import cv2
from rembg import *

img_path = "TEST_IMAGES/2.jpg"
output_path = 'output.png'

img = cv2.imread(img_path, 1)
img = cv2.resize(img, (1080, 720),
           interpolation = cv2.INTER_NEAREST)

while True:  
    r = cv2.selectROI("select the area", img)
    cropped_image = img[int(r[1]):int(r[1]+r[3]),
                          int(r[0]):int(r[0]+r[2])]
    #print(r)
    cv2.imshow("A_img", cropped_image)

    output = remove(cropped_image)
    copy = cropped_image.copy()
    cv2.imwrite(output_path, output)

    cv2.imshow("B_bgremoved", output)

    gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (15,15), 0)
    canny = cv2.Canny(blurred, 30, 150)
    cnts, _ = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #print(cnts)
    result = copy.copy()
    #print(result)
    cv2.drawContours(result, cnts, -1, (0, 255, 0), 2)

    org = img.copy()

    org[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2]),:] = result
    cv2.imshow('C_Output', org)
    #print(img.shape)
    #print(r[0])
    k = cv2.waitKey(0)
    if k == ord('q'):
        cv2.destroyAllWindows()
    elif k == ord('c'):
        cv2.destroyAllWindows()
        cv2.imshow('Image', img)


