import numpy
import scipy.ndimage
from scipy.ndimage import imread
from numpy.ma.core import exp
from scipy.constants.constants import pi

img1 = imread("C:\\Users\\ADMIN\\Desktop\\w9.png", flatten=True)  # .reshape(395,931)
img2 = imread("C:\\Users\\ADMIN\\Desktop\\w9.png", flatten=True)


def compute_ssim(img1, img2):
    gaussian_kernel_sigma = 1.5
    gaussian_kernel_width = 11
    gaussian_kernel = numpy.zeros((gaussian_kernel_width, gaussian_kernel_width))

    for i in range(gaussian_kernel_width):
        for j in range(gaussian_kernel_width):
            gaussian_kernel[i, j] = (1 / (2 * pi * (gaussian_kernel_sigma ** 2))) * exp(
                -(((i - 5) ** 2) + ((j - 5) ** 2)) / (2 * (gaussian_kernel_sigma ** 2)))

    img_mat_1 = img1.astype(numpy.float)
    img_mat_2 = img2.astype(numpy.float)

    img1_sq = img_mat_1 ** 2
    img2_sq = img_mat_2 * 2
    img_12 = img1_sq * img2_sq

    img_mat_mu_1 = scipy.ndimage.filters.convolve(img_mat_1, gaussian_kernel)
    img_mat_mu_2 = scipy.ndimage.filters.convolve(img_mat_2, gaussian_kernel)

    img_mat_mu_1_sq = img_mat_mu_1 ** 2
    img_mat_mu_2_sq = img_mat_mu_2 ** 2
    img_mat_mu_12 = img_mat_mu_1 * img_mat_mu_2

    img_mat_sigma_1_sq = scipy.ndimage.filters.convolve(img_mat_mu_1_sq, gaussian_kernel)
    img_mat_sigma_2_sq = scipy.ndimage.filters.convolve(img_mat_mu_2_sq, gaussian_kernel)

    img_mat_sigma_12 = scipy.ndimage.filters.convolve(img_mat_mu_12, gaussian_kernel)

    img_mat_sigma_1_sq = img_mat_sigma_1_sq - img_mat_mu_1_sq
    img_mat_sigma_2_sq = img_mat_sigma_2_sq - img_mat_mu_2_sq
    img_mat_sigma_12 = img_mat_sigma_12 - img_mat_mu_12

    c_1 = 6.5025
    c_2 = 58.5225

    l = 255
    k_1 = .01
    c_1 = (k_1 * l) ** 2
    k_2 = .03
    c_2 = (k_2 * l) ** 2

    num_ssim = (2 * img_mat_mu_12 + c_1) * (img_mat_sigma_12 + c_2)

    den_ssim = (img_mat_mu_1_sq + img_mat_mu_2_sq + c_1) * (img_mat_sigma_1_sq + img_mat_sigma_2_sq + c_2)

    ssim_map = num_ssim / den_ssim
    index = numpy.average(ssim_map)
    print(index)

    return index


compute_ssim(img1, img2)
