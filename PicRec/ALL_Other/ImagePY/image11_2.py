import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont

if __name__ == '__main__':

    # opencv 读取本地图片文件, 数据类型是numpy.ndarray
    img_OpenCV = cv2.imread('D:\WorkProject\ImageProject\PicRec\ImagePY\img7.jpg')

    # 将opencv图像格式转换成PIL格式, 数据类型是PIL.Image.Image
    img_PIL = Image.fromarray(cv2.cvtColor(img_OpenCV, cv2.COLOR_BGR2RGB))

    # 字体，默认的路径/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc，我把它拷贝过来了
    font = ImageFont.truetype('NotoSansCJK-Black.ttc', 26)
    # 字体颜色
    fillColor = (0, 0, 255)
    # 文字输出位置
    position = (50, 50)
    # 输出内容
    str = '\t\t\t\t\t\t\t\t\t\t\t\t我的独立博客: \nhttps://xugaoxiang.com'

    draw = ImageDraw.Draw(img_PIL)
    draw.text(position, str, font=font, fill=fillColor)

    # 转换回OpenCV格式
    img_OpenCV = cv2.cvtColor(numpy.asarray(img_PIL), cv2.COLOR_RGB2BGR)

    # 在窗口中显示
    cv2.imshow("image", img_OpenCV)

    while True:
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break

    cv2.destroyAllWindows()
