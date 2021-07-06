"""
Author : Lukas Johnny
Module Title : FaceMaskClassifier
File Name : TM_ClassificationsModule_FaceMask.py
Date : 28-June-2021

"""

import numpy as np
import cv2

class FaceMaskClassifier():
    def __init__(self,modelPath, labelPath, threshold=0.5):
        self.modelPath = modelPath
        self.labelPath = labelPath
        self.confThreshold = threshold
        self.font = cv2.FONT_HERSHEY_SIMPLEX


def main():
    cap = cv2.VideoCapture(0)
    detector = FaceMaskClassifier('Teachable_Machine_Tutorial/with_out_facemask_model/keras_model.h5','Teachable_Machine_Tutorial/with_out_facemask_model/labels.txt')

    while True:
        success, img = cap.read()
        cv2.imshow("Result",img)
        if cv2.waitKey(1) & 0XFF==ord('q'):
            break

if __name__ == "__main__":
    main()