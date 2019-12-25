# -*- coding: utf-8 -*-

from skimage.measure import compare_ssim as ssim
from skimage.measure import compare_mse as mse

def compareImage(imageA,imageB,title):
    m1 = mse(imageA,imageB) # 构造函数
    # m2 = mse_ski