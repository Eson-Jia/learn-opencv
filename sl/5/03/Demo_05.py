import cv2

bgr_image = cv2.imread("D:/5.1.jpg")
cv2.imshow("5.1", bgr_image) # 显示图5.1
b, g, r = cv2.split(bgr_image) # 拆分图5.1中的通道
cv2.imshow("B", b) # 显示图5.1中的B通道图像
cv2.imshow("G", g) # 显示图5.1中的G通道图像
cv2.imshow("R", r) # 显示图5.1中的R通道图像
cv2.waitKey()
cv2.destroyAllWindows()