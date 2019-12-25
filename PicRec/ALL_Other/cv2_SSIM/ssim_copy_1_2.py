# -*- coding: utf-8 -*-

import numpy
import scipy.ndimage
from scipy.ndimage import imread
from numpy.ma.core import exp
from scipy.constants.constants import pi

img1 = imread("C:\\Users\\ADMIN\\Desktop\\w9.png", flatten=True)
img2 = imread("C:\\Users\\ADMIN\\Desktop\\w1.png", flatten=True)

'''
The function to compute SSIM     计算SSIM的函数
@param param: img_mat_1 1st 2D matrix     参数:img mat 1 1 2D矩阵
@param param: img_mat_2 2nd 2D matrix     参数:img mat 2二维矩阵
'''


def compute_ssim(img_mat_1, img_mat_2):
    # Variables for Gaussian kernel definition
    # 变量的高斯核定义
    gaussian_kernel_sigma = 1.5
    gaussian_kernel_width = 11
    gaussian_kernel = numpy.zeros((gaussian_kernel_width, gaussian_kernel_width))

    # Fill Gaussian kernel 填补高斯核
    for i in range(gaussian_kernel_width):
        for j in range(gaussian_kernel_width):
            gaussian_kernel[i, j] = \
                (1 / (2 * pi * (gaussian_kernel_sigma ** 2))) * \
                exp(-(((i - 5) ** 2) + ((j - 5) ** 2)) / (2 * (gaussian_kernel_sigma ** 2)))

    # Convert image matrices to double precision (like in the Matlab version)
    # 将图像矩阵转换为双精度(如Matlab版本)
    img_mat_1 = img_mat_1.astype(numpy.float)
    img_mat_2 = img_mat_2.astype(numpy.float)

    # Squares of input matrices 输入矩阵的平方
    img_mat_1_sq = img_mat_1 ** 2
    img_mat_2_sq = img_mat_2 ** 2
    img_mat_12 = img_mat_1 * img_mat_2

    # Means obtained by Gaussian filtering of inputs
    # 通过输入的高斯滤波得到的平均值
    img_mat_mu_1 = scipy.ndimage.filters.convolve(img_mat_1, gaussian_kernel)
    img_mat_mu_2 = scipy.ndimage.filters.convolve(img_mat_2, gaussian_kernel)

    # Squares of means
    img_mat_mu_1_sq = img_mat_mu_1 ** 2
    img_mat_mu_2_sq = img_mat_mu_2 ** 2
    img_mat_mu_12 = img_mat_mu_1 * img_mat_mu_2

    # Variances obtained by Gaussian filtering of inputs' squares
    # 输入平方的高斯滤波得到的方差
    img_mat_sigma_1_sq = scipy.ndimage.filters.convolve(img_mat_1_sq, gaussian_kernel)
    img_mat_sigma_2_sq = scipy.ndimage.filters.convolve(img_mat_2_sq, gaussian_kernel)

    # Covariance    协方差
    img_mat_sigma_12 = scipy.ndimage.filters.convolve(img_mat_12, gaussian_kernel)

    # Centered squares of variances  方差的平方居中
    img_mat_sigma_1_sq = img_mat_sigma_1_sq - img_mat_mu_1_sq
    img_mat_sigma_2_sq = img_mat_sigma_2_sq - img_mat_mu_2_sq
    img_mat_sigma_12 = img_mat_sigma_12 - img_mat_mu_12;

    # c1/c2 constants c1 / c2不变
    # First use: manual fitting  首次使用:手动安装
    c_1 = 6.5025
    c_2 = 58.5225

    # Second use: change k1,k2 & c1,c2 depend on L (width of color map)
    # 二次使用: 根据L改变k1、k2、c1、c2(彩色地图宽度)
    l = 255
    k_1 = 0.01
    c_1 = (k_1 * l) ** 2
    k_2 = 0.03
    c_2 = (k_2 * l) ** 2

    # Numerator of SSIM  分子的SSIM
    num_ssim = (2 * img_mat_mu_12 + c_1) * (2 * img_mat_sigma_12 + c_2)
    # Denominator of SSIM  分母的SSIM
    den_ssim = (img_mat_mu_1_sq + img_mat_mu_2_sq + c_1) * \
               (img_mat_sigma_1_sq + img_mat_sigma_2_sq + c_2)
    # SSIM
    ssim_map = num_ssim / den_ssim
    index = numpy.average(ssim_map)

    print(index)

    return index


compute_ssim(img1, img2)
compute_ssim(img2, img1)
