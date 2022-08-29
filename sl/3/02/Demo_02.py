import cv2

image = cv2.imread("3.1.jpg")  # 读取3.1.jpg
cv2.imshow("flower", image)  # 在名为flower的窗口中显示3.1.jpg
cv2.waitKey()  # 按下任何键盘按键后
cv2.destroyAllWindows()  # 销毁所有窗口