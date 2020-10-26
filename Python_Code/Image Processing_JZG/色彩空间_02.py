# 实现图像通道的分离与合并
import cv2 as cv


# 图片分离
def split_img(image):
    b, g, r = cv.split(image)
    cv.imshow('blue', b)
    cv.imshow('green', g)
    cv.imshow('red', r)
    return b, g, r


# 图像合并
def merge_img(b, g, r):
    image = cv.merge([b, g, r])
    cv.imshow('merge', image)

    # 所有像素 第三通道赋0值
    image[:, :, 2] = 0
    cv.imshow('red = 0', image)


def main():
    img = cv.imread('sources/butterfly.jpg')
    cv.imshow('butterfly', img)

    b, g, r = split_img(img)
    merge_img(b, g, r)

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
