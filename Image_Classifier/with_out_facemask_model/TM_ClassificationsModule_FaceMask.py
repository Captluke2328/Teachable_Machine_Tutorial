"""
Author : Lukas Johnny
Module Title : FaceMaskClassifier
File Name : TM_ClassificationsModule_FaceMask.py
Date : 28-June-2021

"""
import tensorflow.keras
import numpy as np
import cv2

class FaceMaskClassifier():
    def __init__(self, modelPath, labelPath, threshold=0.5):
        self.modelPath = modelPath
        self.labelPath = labelPath
        self.confThreshold = threshold
        self.font = cv2.FONT_HERSHEY_SIMPLEX

        # Disable scientific notation for clarity
        np.set_printoptions(suppress=True)

        # Load the model
        self.model = tensorflow.keras.models.load_model(modelPath)

        """
        Create the array of the right shape to feed into the keras model
        The 'length' or number of images you can put into the array is
        determined by the first position in the shape tuple, in this case 1.
        """
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # Read the label Text
        if self.labelPath:
            self.list_labels = {}
            with open(self.labelPath, "r") as label:
                text = label.read()
                lines = text.split("\n")
                for line in lines[0:-1]:
                    hold = line.split(" ", 1)
                    self.list_labels[hold[0]] = hold[1]
        else:
            print("No Labels Found")

    def getPrediction(self, img):

        hT, wT, cT = img.shape

        # resize the image to a 224x224 with the same strategy as in TM2:
        # resizing the image to be at least 224x224 and then cropping from the center
        frame = cv2.resize(img, (224, 224))

        # turn the image into a numpy array
        image_array = np.asarray(frame)

        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

        # Load the image into the array
        self.data[0] = normalized_image_array

        # Run the inference
        pred = self.model.predict(self.data)
        index = np.argmax(pred[0])

        # Check for confidence
        confidence = pred[0][index]

        print(pred, hT, wT)

        # if confidence > self.confThreshold:

        # Draw a label in the frame
        cv2.putText(img, "Label : " + (self.list_labels[str(index)]), (280, 400), self.font, 1, (0, 255, 0), 2,
                    cv2.LINE_AA)

        # Draw a rectangle in the frame
        # frame = cv2.rectangle(img, (220, 80), (530, 360), (0, 0, 255), 3)

        return list(pred[0]), index, confidence

def main():
    cap = cv2.VideoCapture(0)
    #detector = FaceMaskClassifier(r'C:\Users\Lukas\Desktop\My Projects\Teachable_Machine\with_out_facemask_model\keras_model.h5', r'C:\Users\Lukas\Desktop\My Projects\Teachable_Machine\with_out_facemask_model\labels.txt')
    detector = FaceMaskClassifier(r'/Users/jlukas/Desktop/My_Project/Teachable_Machine_Tutorial/Image_Classifier/with_out_facemask_model/keras_model.h5', r'/Users/jlukas/Desktop/My_Project/Teachable_Machine_Tutorial/Image_Classifier/with_out_facemask_model/labels.txt')

    while True:
        success, img = cap.read()
        prediction = detector.getPrediction(img)

        cv2.imshow("Result", img)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break

if __name__ == "__main__":
    main()
