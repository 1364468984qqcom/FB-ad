# -*- coding=GBK -*-
import cv2 as cv


# ������ͷ��ȡͼƬ
def video_demo():
    capture = cv.VideoCapture(0)  # ������ͷ��0��������豸id������ж������ͷ����������������ֵ
    while True:
        ret, frame = capture.read()  # ��ȡ����ͷ,���ܷ���������������һ��������bool�͵�ret����ֵΪTrue��False��������û�ж���ͼƬ���ڶ���������frame���ǵ�ǰ��ȡһ֡��ͼƬ
        frame = cv.flip(frame, 1)  # ��ת 0:���µߵ� ����0ˮƽ�ߵ�   С��180��ת
        cv.imshow("video", frame)
        if cv.waitKey(10) & 0xFF == ord('q'):  # ��������q�˳����ڣ�����q����رջ�һֱ�ز��� Ҳ�������ó���������
            break


video_demo()
cv.destroyAllWindows()  # ɾ��������ȫ�����ڣ��ͷ���Դ
