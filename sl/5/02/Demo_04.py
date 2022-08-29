import cv2

image = cv2.imread("D:/5.1.jpg")
cv2.imshow("5.1", image) # 显示图5.1
# 将图5.1从BGR色彩空间转换到HSV色彩空间
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv_image) # 用HSV色彩空间显示的图像
cv2.waitKey()
cv2.destroyAllWindows()