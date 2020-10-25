# 实现RGB, 灰度图, HSV, HLS, YCrCb, YUV等色彩空间的相互转换
import cv2 as cv


def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow('GRAY', gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow('HSV', hsv)
    hls = cv.cvtColor(image, cv.COLOR_BGR2HLS)
    cv.imshow('HIS', hls)
    YCrCb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow('YCrCb', YCrCb)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow('YUV', yuv)


img = cv.imread('sources/butterfly.jpg')
cv.namedWindow('picture', cv.WINDOW_AUTOSIZE)
cv.imshow('picture', img)

color_space_demo(img)

cv.waitKey(0)
cv.destroyWindow('picture')
