import cv2

bgr_image = cv2.imread("D:/5.1.jpg")
# 把图5.1从BGR色彩空间转换到BGRA色彩空间
bgra_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2BGRA)
cv2.imshow("BGRA", bgr_image) # 显示BGRA图像
b, g, r, a = cv2.split(bgra_image) # 拆分BGRA图像中的通道
a[:, :] = 172 # 将BGRA图像的透明度调整为172（半透明）
bgra_172 = cv2.merge([b, g, r, a]) # 合并拆分后并将透明度调整为172的通道图像
a[:, :] = 0 # 将BGRA图像的透明度调整为0（透明）
bgra_0 = cv2.merge([b, g, r, a]) # 合并拆分后并将透明度调整为0的通道图像
cv2.imshow("A = 172", bgra_172) # 显示透明度为172的BGRA图像
cv2.imshow("A = 0", bgra_0) # 显示透明度为0的BGRA图像
cv2.waitKey()
cv2.destroyAllWindows()