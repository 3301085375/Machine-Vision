# 1.载入一段视频，并识别出视频中的绿色圆环
import cv2 as cv
import numpy as np


def test_video_object():
    capture = cv.VideoCapture('sources/Test_Video.mp4')
    while True:
        ret, frame = capture.read()
        if ret is False:            # if not ret:
            print('未成功读取视频！')
            break
        # print('成功读取到视频！')
        # 转HSV图像，并设置绿色的HSV值
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([37, 43, 46])
        upper_hsv = np.array([77, 255, 255])
        mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
        cv.imshow('Test_Video', frame)

        # 绿圈显示为白色
        # cv.imshow('mask', mask)

        # 绿圈显示为原来的绿色
        dst = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow('mask', dst)
        c = cv.waitKey(40)
        if c == 27:
            break


def main():
    test_video_object()


if __name__ == '__main__':
    main()
