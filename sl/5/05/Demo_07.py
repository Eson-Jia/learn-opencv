import cv2

bgr_image = cv2.imread("D:/5.1.jpg")
b, g, r = cv2.split(bgr_image) # 拆分图5.1中的通道
bgr = cv2.merge([b, g, r]) # 按B→G→R的顺序合并通道
cv2.imshow("BGR", bgr)
cv2.waitKey()
cv2.destroyAllWindows()