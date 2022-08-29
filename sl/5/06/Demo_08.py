import cv2

bgr_image = cv2.imread("D:/5.1.jpg")
# 把图5.1从BGR色彩空间转换到HSV色彩空间
hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_image) # 拆分HSV图像中的通道
hsv = cv2.merge([h, s, v]) # 合并拆分后的通道图像
# 合并通道后的图像从HSV色彩空间转换到BGR色彩空间
bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("BGR", bgr) # 显示BGR图像
cv2.waitKey()
cv2.destroyAllWindows()