# -*- coding=GBK -*-
import cv2 as cv


# 打开摄像头获取图片
def video_demo():
    capture = cv.VideoCapture(0)  # 打开摄像头，0代表的是设备id，如果有多个摄像头，可以设置其他数值
    while True:
        ret, frame = capture.read()  # 读取摄像头,它能返回两个参数，第一个参数是bool型的ret，其值为True或False，代表有没有读到图片；第二个参数是frame，是当前截取一帧的图片
        frame = cv.flip(frame, 1)  # 翻转 0:上下颠倒 大于0水平颠倒   小于180旋转
        cv.imshow("video", frame)
        if cv.waitKey(10) & 0xFF == ord('q'):  # 键盘输入q退出窗口，不按q点击关闭会一直关不掉 也可以设置成其他键。
            break


video_demo()
cv.destroyAllWindows()  # 删除建立的全部窗口，释放资源
