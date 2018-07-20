#!/usr/bin/env python3  
# encoding: utf-8   

""" 
@author: Elon kou 
@contact: koudongliang@regiontec.com 
@file: display_dicom.py 
@time: 18-7-20 下午6:16 
"""
import cv2
import pydicom
import matplotlib as plt
import SimpleITK as sitk
import numpy as np


def read_dicom(file_path):
    reader = sitk.ImageSeriesReader()
    dicom_names = reader.GetGDCMSeriesFileNames(file_path)
    reader.SetFileNames(dicom_names)
    image = reader.Execute()
    data = sitk.GetArrayFromImage(image)
    return data


def read_window(file_path):
    ds = pydicom.read_dcm(file_path)


if __name__ == "__main__":
    path = "/home/elonkou/Desktop/reg_data/8_HEAD_MOVING_MR"
    data = read_dicom(path)
    # print(data.shape)
    img = data[15, :, :]
    print(np.max(img))
    print(np.min(img))

    cv2.imshow("image", data[15, :, :] * 30)
    cv2.waitKey(0)

    sitk.

    # plt.figure(figsize=(12, 12))
    # plt.subplot(131)
    # plt.imshow(slices[int(len(slices) / 2)].image, 'gray')
    # plt.title('Original')
    # plt.subplot(132)
    # plt.imshow(img, 'gray')
    # plt.title('Mask')
    # plt.subplot(133)
    # plt.imshow(img2, 'gray')
    # plt.title('Result')
    # plt.show()
