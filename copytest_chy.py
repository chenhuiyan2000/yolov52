import cv2
import numpy as np

# 假设已经加载了图像并且有一个名为segments的轮廓列表

# 创建一个空的图像用于绘制轮廓
im_new = np.zeros_like(im)  # 使用与原始图像相同大小的黑色图像
# 遍历segments中的每个轮廓并绘制它们
for contour in segments:
    cv2.drawContours(im_new, [contour.astype(np.int32)], -1, (1, 1, 1), cv2.FILLED)
output_path = "path_to_output_folder/filled_contours.png"  # 替换为您希望保存的路径和文件名
cv2.imwrite(output_path, im_new)
print("Image saved successfully!")