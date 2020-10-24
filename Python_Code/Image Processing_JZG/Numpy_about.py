# 1.加载一张图片，读取图片属性等信息，打印出图片的高，宽，通道数
# 2.遍历像素取反，计算显示遍历运算使用时间
# 3.利用逻辑运算快速高效像素取反
# 3.创建一个纯色的图片
# 4.纯数组操作
# 5.利用np.array定义一个数组
import cv2 as cv
import numpy as np


def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print('height: %s, width: %s, channels: %s' % (height, width, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("像素遍历取反", image)


def inverse_image(image):
    dst = cv.bitwise_not(image)
    cv.imshow('inverse_demo', dst)


def create_image():
    """
    #多通道图片
    img_1 = np.zeros([400, 400, 3], np.uint8)       # 8位整型0矩阵
    img_1[:, :, 0] = np.ones([400, 400]) * 255      # 1矩阵   全部像素0通道赋全值  即蓝色
    cv.imshow('new_img', img_1)
    """
    """
    # 单通道图片
    img_1 = np.zeros([400, 400], np.uint8)  # 8位整型0矩阵
    img_1[:, :] = np.ones([400, 400]) * 255  # 1矩阵 全部像素赋全值为白色，赋0值为黑色
    cv.imshow('new_img', img_1)
    """
    # 单通道图片简化写法
    img_1 = np.ones([400, 400], np.uint8)  # 8位整型0矩阵
    img_1[:, :] = img_1 * 255  # 1矩阵 全部像素赋全值为白色，赋0值为黑色
    cv.imshow('new_img', img_1)


def operation_array():
    m1 = np.ones([3, 3], np.float32)
    m1.fill(122.388)
    print(m1)

    # m2是m1的横写形式
    m2 = m1.reshape([1, 9])
    print(m2)

    # 利用np.array定义一个数组
    m3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], np.int32)
    m3.fill(9)
    print(m3)


def run():
    img = cv.imread('sources/butterfly.jpg')
    cv.namedWindow('picture', cv.WINDOW_AUTOSIZE)
    cv.imshow('picture', img)
    t1 = cv.getTickCount()
    access_pixels(img)  # 像素遍历取反
    t2 = cv.getTickCount()
    time = (t2 - t1) / cv.getTickFrequency()
    print('time: %s ms' % (time * 1000))

    # create_image()    # 创建图片
    # operation_array() # 操作数组
    # inverse_image()   # 逻辑运算像素取反

    cv.waitKey(0)
    cv.destroyWindow('picture')


if __name__ == '__main__':
    run()
