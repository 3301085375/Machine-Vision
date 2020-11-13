# 1.加载两张图片，对两张图片进行加减乘除
# 2.对每个图片的像素进行统计，计算平均值与方差值
# 3.利用numpy库创建一个0矩阵，展示为一张纯黑色图，并计算均值与方差
import cv2 as cv
import numpy as np


def add_demo(m1, m2):
    dst = cv.add(m1, m2)
    cv.imshow('add_demo', dst)
    cv.imwrite('out/Pixel_operation_mathematical_operation/add_demo.jpg', dst)


def subtract_demo(m1, m2):
    dst = cv.subtract(m1, m2)
    cv.imshow('subtract_demo', dst)
    cv.imwrite('out/Pixel_operation_mathematical_operation/subtract_demo.jpg', dst)


def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow('multiply_demo', dst)
    cv.imwrite('out/Pixel_operation_mathematical_operation/multiply_demo.jpg', dst)


def divide_demo(m1, m2):
    dst = cv.divide(m1, m2)
    cv.imshow('divide_demo', dst)
    cv.imwrite('out/Pixel_operation_mathematical_operation/divide_demo.jpg', dst)


def mean_StdDev_demo(m1, m2):
    M1, dev1 = cv.meanStdDev(m1)
    M2, dev2 = cv.meanStdDev(m2)

    # print(M1, M2, dev1, dev2)
    print(M1)
    print(M2)
    print(dev1)
    print(dev2)

    # 用0矩阵验证均值和方差都为0  其实只要图片为纯色，这两个之均为0，可用来有效检测是否为纯色图
    h, w = m1.shape[: 2]
    img = np.zeros([h, w], np.uint8)
    m, dev = cv.meanStdDev(img)
    cv.imshow('yanzheng', img)
    cv.imwrite('out/Pixel_operation_mathematical_operation/yanzheng.jpg', img)
    print(m)
    print(dev)


def main():
    img1 = cv.imread('sources/LinuxLogo.jpg')
    img2 = cv.imread('sources/WindowsLogo.jpg')
    cv.namedWindow('image1', cv.WINDOW_AUTOSIZE)
    cv.imshow('image1', img1)
    cv.imshow('image2', img2)
    print(img1.shape, img2.shape)

    add_demo(img1, img2)
    subtract_demo(img1, img2)
    multiply_demo(img1, img2)
    divide_demo(img1, img2)

    mean_StdDev_demo(img1, img2)

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
