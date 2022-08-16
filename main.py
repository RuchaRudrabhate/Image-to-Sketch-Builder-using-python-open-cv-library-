import cv2
image = cv2.imread("pic.jpeg")
grey_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# imshow(image)
invert = cv2.bitwise_not(grey_img)
blurimg = cv2.GaussianBlur(invert, (21,21),0)
invertedblur = cv2.bitwise_not(blurimg)
sketch = cv2.divide(grey_img, invertedblur, scale = 256.0)

cv2.imwrite("sketch3.png" , sketch)


