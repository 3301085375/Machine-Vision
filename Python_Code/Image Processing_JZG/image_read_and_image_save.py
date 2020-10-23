# 加载一张图片，读取图片属性等信息，保存图片
import cv2 as cv
import numpy as np


# 方法：打印图片属性，计算像素平均值
def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pic_data = np.array(image)
    print(pic_data)


def run():
    # cv.namedWindow('Butterfly', cv.WINDOW_AUTOSIZE)
    img = cv.imread('sources/butterfly.jpg')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow('Butterfly', img)
    cv.imshow('Butterfly_Gary.jpg', gray)

    cv.imwrite('out/Butterfly.png', img)
    cv.imwrite('out/Butterfly_Gary.jpg', gray)
    get_image_info(img)
    get_image_info(gray)

    while True:
        k = cv.waitKey(0)
        if k == 27:
            cv.destroyAllWindows()
            break


if __name__ == '__main__':
    print('Start!')
    run()
    print('End!')
